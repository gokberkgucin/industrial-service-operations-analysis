param(
    [string]$SourceDocx,
    [string]$WorkPdf,
    [string]$PublicPdf
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RepoRoot = Split-Path -Parent $PSScriptRoot
if (-not $SourceDocx) {
    $SourceDocx = Join-Path $RepoRoot "EK-10_Siemens_Staj_Makale_Analizleri.docx"
}
if (-not $WorkPdf) {
    $WorkPdf = Join-Path $RepoRoot "_work\build\EK-10_Siemens_Staj_Makale_Analizleri.pdf"
}
if (-not $PublicPdf) {
    $PublicPdf = Join-Path $RepoRoot "docs\assets\staj\originals\EK-10_Siemens_Staj_Makale_Analizleri.pdf"
}

$SourceDocx = [System.IO.Path]::GetFullPath($SourceDocx)
$WorkPdf = [System.IO.Path]::GetFullPath($WorkPdf)
$PublicPdf = [System.IO.Path]::GetFullPath($PublicPdf)

if (-not (Test-Path -LiteralPath $SourceDocx)) {
    throw "Source DOCX not found: $SourceDocx"
}

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $WorkPdf) | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $PublicPdf) | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $RepoRoot "_work\logs") | Out-Null

$toolUsed = $null
$errors = New-Object System.Collections.Generic.List[string]

function Export-WithWord {
    param([string]$InputDocx, [string]$OutputPdf)

    $word = $null
    $doc = $null
    try {
        $word = New-Object -ComObject Word.Application
        $word.Visible = $false
        $doc = $word.Documents.Open($InputDocx, $false, $true)
        # 17 = wdExportFormatPDF
        $doc.ExportAsFixedFormat($OutputPdf, 17)
    }
    finally {
        if ($doc -ne $null) {
            $doc.Close($false) | Out-Null
        }
        if ($word -ne $null) {
            $word.Quit() | Out-Null
            [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
        }
    }
}

function Find-Soffice {
    $cmd = Get-Command "soffice.com" -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    $cmd = Get-Command "soffice.exe" -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }

    $candidates = @(
        "D:\LibreOffice\program\soffice.com",
        "D:\LibreOffice\program\soffice.exe",
        "C:\Program Files\LibreOffice\program\soffice.com",
        "C:\Program Files\LibreOffice\program\soffice.exe"
    )
    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    return $null
}

try {
    Export-WithWord -InputDocx $SourceDocx -OutputPdf $WorkPdf
    $toolUsed = "word-com"
}
catch {
    $errors.Add("Word COM export failed: $($_.Exception.Message)")
}

if (-not $toolUsed) {
    $soffice = Find-Soffice
    if (-not $soffice) {
        throw "Neither Word COM nor LibreOffice soffice is available. Errors: $($errors -join '; ')"
    }

    $loOutDir = Join-Path $RepoRoot "_work\build\libreoffice-export"
    New-Item -ItemType Directory -Force -Path $loOutDir | Out-Null

    $process = Start-Process -FilePath $soffice -WindowStyle Hidden -ArgumentList @(
        "--headless",
        "--convert-to", "pdf",
        "--outdir", $loOutDir,
        $SourceDocx
    ) -NoNewWindow -PassThru -Wait

    if ($process.ExitCode -ne 0) {
        throw "LibreOffice export failed with exit code $($process.ExitCode). Previous errors: $($errors -join '; ')"
    }

    $expected = Join-Path $loOutDir ([System.IO.Path]::GetFileNameWithoutExtension($SourceDocx) + ".pdf")
    if (-not (Test-Path -LiteralPath $expected)) {
        $found = Get-ChildItem -LiteralPath $loOutDir -Filter "*.pdf" | Select-Object -First 1
        if (-not $found) {
            throw "LibreOffice finished but produced no PDF in $loOutDir"
        }
        $expected = $found.FullName
    }

    Copy-Item -LiteralPath $expected -Destination $WorkPdf -Force
    $toolUsed = "libreoffice-soffice"
}

if (-not (Test-Path -LiteralPath $WorkPdf)) {
    throw "PDF export did not produce expected file: $WorkPdf"
}

Copy-Item -LiteralPath $WorkPdf -Destination $PublicPdf -Force

$hash = Get-FileHash -Algorithm SHA256 -LiteralPath $WorkPdf
$result = [ordered]@{
    generated_at = (Get-Date).ToString("s")
    tool = $toolUsed
    source_docx = $SourceDocx
    work_pdf = $WorkPdf
    public_pdf = $PublicPdf
    pdf_bytes = (Get-Item -LiteralPath $WorkPdf).Length
    sha256 = $hash.Hash
    warnings = $errors
}

$logPath = Join-Path $RepoRoot "_work\logs\export_docx_to_pdf.json"
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $logPath -Encoding UTF8
$result | ConvertTo-Json -Depth 5
