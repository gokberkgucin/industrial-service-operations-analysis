param(
    [Parameter(Mandatory=$true)][string]$RepoRoot,
    [Parameter(Mandatory=$true)][string]$DefaultBranch
)

[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [System.Text.UTF8Encoding]::new()

Set-Location -LiteralPath $RepoRoot

$remoteIndex = @{}
git ls-tree -r "origin/$DefaultBranch" | ForEach-Object {
    if ($_ -match '^[0-9]{6}\s+\w+\s+([a-f0-9]{40})\t(.+)$') {
        $remoteIndex[$matches[2]] = $matches[1]
    }
}

$localIndex = @{}
Get-ChildItem -LiteralPath $RepoRoot -Recurse -File -Force |
    Where-Object { $_.FullName -notmatch '\\.git\\' -and $_.FullName -notmatch '\\reports\\repo_compare\.(csv|md)$' } |
    ForEach-Object {
        $rel = $_.FullName.Substring($RepoRoot.Length + 1).Replace('\','/')
        $hash = (git hash-object -- $_.FullName).Trim()
        $localIndex[$rel] = $hash
    }

$rows = foreach ($path in (@($remoteIndex.Keys + $localIndex.Keys) | Sort-Object -Unique)) {
    $inRemote = $remoteIndex.ContainsKey($path)
    $inLocal  = $localIndex.ContainsKey($path)

    if ($inRemote -and $inLocal) {
        $status = if ($remoteIndex[$path] -eq $localIndex[$path]) { "identical" } else { "modified" }
        $direction = "both_present"
    }
    elseif ($inRemote -and -not $inLocal) {
        $status = "missing"
        $direction = "local_missing"
    }
    else {
        $status = "missing"
        $direction = "repo_missing"
    }

    [PSCustomObject]@{
        Path       = $path
        Status     = $status
        Direction  = $direction
        RemoteHash = if ($inRemote) { $remoteIndex[$path] } else { "" }
        LocalHash  = if ($inLocal)  { $localIndex[$path] }  else { "" }
    }
}

$reportsDir = Join-Path $RepoRoot "reports"
$csvPath = Join-Path $reportsDir "repo_compare.csv"
$mdPath  = Join-Path $reportsDir "repo_compare.md"

$rows | Sort-Object Direction, Status, Path | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $csvPath

$identical = ($rows | Where-Object Status -eq "identical").Count
$modified  = ($rows | Where-Object Status -eq "modified").Count
$missing   = ($rows | Where-Object Status -eq "missing").Count

$topMissing = $rows | Where-Object Status -eq "missing"  | Select-Object -First 25
$topModified = $rows | Where-Object Status -eq "modified" | Select-Object -First 25

$md = @()
$md += "# Repo karşılaştırma raporu"
$md += ""
$md += "- Default branch: ``origin/$DefaultBranch``"
$md += "- identical: $identical"
$md += "- modified: $modified"
$md += "- missing: $missing"
$md += ""
$md += "## İlk 25 missing"
$md += ""
$md += "| Path | Direction |"
$md += "|---|---|"
foreach ($r in $topMissing) { $md += "| $($r.Path) | $($r.Direction) |" }
$md += ""
$md += "## İlk 25 modified"
$md += ""
$md += "| Path | Direction |"
$md += "|---|---|"
foreach ($r in $topModified) { $md += "| $($r.Path) | $($r.Direction) |" }

$md -join "`r`n" | Set-Content -LiteralPath $mdPath -Encoding UTF8
Write-Host "Rapor üretildi:"
Write-Host $csvPath
Write-Host $mdPath
