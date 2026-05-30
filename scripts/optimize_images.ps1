param(
    [switch]$NoBackup
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$BackupRoot = Join-Path $Repo "_work\backup\image_opt_$Timestamp"
$ManifestPath = Join-Path $Repo "metadata\image-manifest.csv"
$Part1Dir = Join-Path $Repo "assets\images\part-1"
$Part2Dir = Join-Path $Repo "assets\images\part-2"
$RawDocxDir = Join-Path $Repo "_work\extracted\docx-images"
$RawExtractedDir = Join-Path $Repo "_work\extracted"

New-Item -ItemType Directory -Force -Path $Part1Dir, $Part2Dir, (Split-Path $ManifestPath) | Out-Null

function Get-RelativePath {
    param([string]$Path)
    $full = [System.IO.Path]::GetFullPath($Path)
    $root = [System.IO.Path]::GetFullPath($Repo)
    if ($full.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $full.Substring($root.Length).TrimStart([char[]]"\/").Replace("\", "/")
    }
    return $Path.Replace("\", "/")
}

function Backup-File {
    param([string]$Path)
    if ($NoBackup -or -not (Test-Path -LiteralPath $Path)) {
        return
    }
    $rel = Get-RelativePath -Path $Path
    $target = Join-Path $BackupRoot $rel
    New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
    Copy-Item -LiteralPath $Path -Destination $target -Force
}

function Get-ImageInfoSafe {
    param([string]$Path)
    try {
        Add-Type -AssemblyName System.Drawing -ErrorAction SilentlyContinue
        $img = [System.Drawing.Image]::FromFile($Path)
        try {
            return [pscustomobject]@{
                Width = [int]$img.Width
                Height = [int]$img.Height
                Readable = $true
            }
        }
        finally {
            $img.Dispose()
        }
    }
    catch {
        return [pscustomobject]@{
            Width = $null
            Height = $null
            Readable = $false
        }
    }
}

function Optimize-Raster {
    param(
        [string]$Source,
        [string]$Destination,
        [int]$MaxWidth = 1600,
        [int]$Quality = 84
    )

    Add-Type -AssemblyName System.Drawing -ErrorAction SilentlyContinue

    $srcFull = [System.IO.Path]::GetFullPath($Source)
    $dstFull = [System.IO.Path]::GetFullPath($Destination)
    New-Item -ItemType Directory -Force -Path (Split-Path $dstFull) | Out-Null

    $ext = [System.IO.Path]::GetExtension($dstFull).ToLowerInvariant()
    if ($ext -notin @(".jpg", ".jpeg", ".png")) {
        if ($srcFull -ne $dstFull) {
            Copy-Item -LiteralPath $srcFull -Destination $dstFull -Force
        }
        return
    }

    $readSource = $srcFull
    $cleanupSource = $null
    if ($srcFull -eq $dstFull) {
        $cleanupSource = "$srcFull.readtmp$ext"
        Copy-Item -LiteralPath $srcFull -Destination $cleanupSource -Force
        $readSource = $cleanupSource
    }

    $img = [System.Drawing.Image]::FromFile($readSource)
    try {
        $scale = 1.0
        if ($img.Width -gt $MaxWidth) {
            $scale = $MaxWidth / $img.Width
        }
        $newWidth = [Math]::Max(1, [int][Math]::Round($img.Width * $scale))
        $newHeight = [Math]::Max(1, [int][Math]::Round($img.Height * $scale))

        $bitmap = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
        try {
            $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
            try {
                $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
                $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
                $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
                if ($ext -in @(".jpg", ".jpeg")) {
                    $graphics.Clear([System.Drawing.Color]::White)
                }
                else {
                    $graphics.Clear([System.Drawing.Color]::Transparent)
                }
                $graphics.DrawImage($img, 0, 0, $newWidth, $newHeight)
            }
            finally {
                $graphics.Dispose()
            }

            $tmp = "$dstFull.tmp$ext"
            if ($ext -in @(".jpg", ".jpeg")) {
                $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" } | Select-Object -First 1
                $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
                $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [int64]$Quality)
                $bitmap.Save($tmp, $codec, $encoderParams)
                $encoderParams.Dispose()
            }
            else {
                $bitmap.Save($tmp, [System.Drawing.Imaging.ImageFormat]::Png)
            }
            if (Test-Path -LiteralPath $dstFull) {
                Remove-Item -LiteralPath $dstFull -Force
            }
            Move-Item -LiteralPath $tmp -Destination $dstFull -Force
        }
        finally {
            $bitmap.Dispose()
        }
    }
    finally {
        $img.Dispose()
        if ($cleanupSource -and (Test-Path -LiteralPath $cleanupSource)) {
            Remove-Item -LiteralPath $cleanupSource -Force
        }
    }
}

function Add-ManifestRow {
    param(
        [System.Collections.Generic.List[object]]$Rows,
        [string]$OldName,
        [string]$NewName,
        [string]$Source,
        [string]$TargetMarkdown,
        [string]$Caption,
        [string]$UseMode
    )
    $Rows.Add([pscustomobject]@{
        old_name = $OldName
        new_name = $NewName
        source = $Source
        target_markdown = $TargetMarkdown
        caption = $Caption
        use_mode = $UseMode
    }) | Out-Null
}

$publicImages = @(
    [pscustomobject]@{
        old_name = "image4.jpg"
        new_name = "siemens-energy-context.jpg"
        source = "_work/extracted/docx-images/image4.jpg"
        target = "assets/images/part-1/siemens-energy-context.jpg"
        target_markdown = "docs/internship-part-1.md"
        caption = "Staj bağlamında kullanılan Siemens Energy iş alanları görseli."
        use_mode = "replace"
    },
    [pscustomobject]@{
        old_name = "image5.jpg"
        new_name = "mcdonalds-burgernomics-concept.jpg"
        source = "_work/extracted/docx-images/image5.jpg"
        target = "assets/images/part-1/mcdonalds-burgernomics-concept.jpg"
        target_markdown = "docs/internship-part-1.md"
        caption = "Standardizasyon ve hizmet operasyonları fikrini anlatmak için kullanılan örnek görsel."
        use_mode = "replace"
    },
    [pscustomobject]@{
        old_name = "image6.jpeg"
        new_name = "disney-service-design-01.jpeg"
        source = "_work/extracted/docx-images/image6.jpeg"
        target = "assets/images/part-1/disney-service-design-01.jpeg"
        target_markdown = "docs/internship-part-1.md"
        caption = "Deneyim tasarımı ve hizmet sunumu örneği."
        use_mode = "replace"
    },
    [pscustomobject]@{
        old_name = "image7.jpeg"
        new_name = "disney-service-design-02.jpeg"
        source = "_work/extracted/docx-images/image7.jpeg"
        target = "assets/images/part-1/disney-service-design-02.jpeg"
        target_markdown = "docs/internship-part-1.md"
        caption = "Deneyim tasarımı ve hizmet atmosferi örneği."
        use_mode = "replace"
    },
    [pscustomobject]@{
        old_name = "image8.jpeg; image9.jpg; image10.jpeg; image11.jpg"
        new_name = "nusret-experience-economy-collage.jpg"
        source = "assets/images/part-1/nusret-experience-economy-collage.jpg"
        target = "assets/images/part-1/nusret-experience-economy-collage.jpg"
        target_markdown = "docs/internship-part-1.md"
        caption = "Hizmet deneyimi ve gösteri ekonomisi tartışmasını destekleyen kolaj."
        use_mode = "keep"
    },
    [pscustomobject]@{
        old_name = "redraw:image80.JPG"
        new_name = "intensity-functions-annotated.webp"
        source = "assets/images/part-2/intensity-functions-annotated.webp"
        target = "assets/images/part-2/intensity-functions-annotated.webp"
        target_markdown = "docs/internship-part-2.md"
        caption = "Makaledeki yoğunluk fonksiyonu fikrinin public repo için yeniden çizilmiş açıklayıcı versiyonu."
        use_mode = "redraw"
    },
    [pscustomobject]@{
        old_name = "redraw:image58.JPG"
        new_name = "response-times-high-workload.webp"
        source = "assets/images/part-2/response-times-high-workload.webp"
        target = "assets/images/part-2/response-times-high-workload.webp"
        target_markdown = "docs/internship-part-2.md"
        caption = "Yüksek iş yükünde emergency response proxy ilişkisini anlatan yeniden çizim."
        use_mode = "redraw"
    },
    [pscustomobject]@{
        old_name = "redraw:image68.JPG; image70.JPG; image71.JPG; image72.JPG"
        new_name = "availability-penalty-high-workload.webp"
        source = "assets/images/part-2/availability-penalty-high-workload.webp"
        target = "assets/images/part-2/availability-penalty-high-workload.webp"
        target_markdown = "docs/internship-part-2.md"
        caption = "Availability ve ceza puanı mantığını gösteren public repo için yeniden çizilmiş teknik grafik."
        use_mode = "redraw"
    }
)

$manifestRows = New-Object "System.Collections.Generic.List[object]"
$usedOldNames = New-Object "System.Collections.Generic.HashSet[string]"

foreach ($item in $publicImages) {
    foreach ($piece in ($item.old_name -split ";")) {
        $clean = $piece.Trim()
        if ($clean.StartsWith("redraw:")) {
            $clean = $clean.Substring(7)
        }
        if ($clean) {
            $null = $usedOldNames.Add($clean)
        }
    }

    $src = Join-Path $Repo $item.source
    $dst = Join-Path $Repo $item.target
    if (Test-Path -LiteralPath $src) {
        Backup-File -Path $dst
        Optimize-Raster -Source $src -Destination $dst
    }

    Add-ManifestRow -Rows $manifestRows -OldName $item.old_name -NewName $item.new_name -Source $item.source -TargetMarkdown $item.target_markdown -Caption $item.caption -UseMode $item.use_mode
}

function Get-DefaultDecision {
    param([System.IO.FileInfo]$File)

    $rel = Get-RelativePath -Path $File.FullName
    $name = $File.Name
    $ext = $File.Extension.ToLowerInvariant()
    $info = Get-ImageInfoSafe -Path $File.FullName

    if ($rel -like "*/page-images/*") {
        return [pscustomobject]@{
            new_name = ""
            target_markdown = "not-used"
            caption = "Tam sayfa PDF renderı; public repo'ya taşınmadı."
            use_mode = "omit"
        }
    }

    if ($rel -like "*/embedded-images/*") {
        $mode = "redraw"
        if ($rel -like "*/article-1/*") {
            $mode = "omit"
        }
        return [pscustomobject]@{
            new_name = ""
            target_markdown = "not-used"
            caption = "PDF içinden çıkarılmış figür parçası; doğrudan public asset olarak kullanılmadı."
            use_mode = $mode
        }
    }

    if ($name -in @("image1.png", "image2.svg", "image3.png")) {
        return [pscustomobject]@{
            new_name = ""
            target_markdown = "not-used"
            caption = "Kapak/form/placeholder niteliğinde olduğu için public repo'ya taşınmadı."
            use_mode = "omit"
        }
    }

    if ($ext -eq ".emf") {
        return [pscustomobject]@{
            new_name = ""
            target_markdown = "docs/internship-part-2.md"
            caption = "EMF denklem, tablo veya teknik grafik parçası; yanlışlıkla silinmedi, public sürümde metin/yeniden çizimle temsil edildi."
            use_mode = "redraw"
        }
    }

    if ($info.Readable -and (($info.Width -lt 80) -or ($info.Height -lt 80))) {
        return [pscustomobject]@{
            new_name = ""
            target_markdown = "docs/internship-part-2.md"
            caption = "Çok küçük denklem/sembol parçası; public görsel olarak taşınmadı."
            use_mode = "redraw"
        }
    }

    if ($name -match "^image(1[2-9]|2[0-9]|[3-7][0-9]|80)\.") {
        return [pscustomobject]@{
            new_name = ""
            target_markdown = "docs/internship-part-2.md"
            caption = "Makale 2 teknik grafik, denklem veya tablo adayı; public sürümde doğrudan kopya yerine yorum, LaTeX veya yeniden çizim kullanıldı."
            use_mode = "redraw"
        }
    }

    return [pscustomobject]@{
        new_name = ""
        target_markdown = "not-used"
        caption = "Kamuya açık repo için seçilmedi."
        use_mode = "omit"
    }
}

if (Test-Path -LiteralPath $RawExtractedDir) {
    $rawFiles = Get-ChildItem -LiteralPath $RawExtractedDir -Recurse -File | Where-Object {
        $_.Extension.ToLowerInvariant() -in @(".png", ".jpg", ".jpeg", ".webp", ".emf", ".svg")
    }

    foreach ($file in $rawFiles) {
        if ($usedOldNames.Contains($file.Name)) {
            continue
        }

        $decision = Get-DefaultDecision -File $file
        Add-ManifestRow `
            -Rows $manifestRows `
            -OldName $file.Name `
            -NewName $decision.new_name `
            -Source (Get-RelativePath -Path $file.FullName) `
            -TargetMarkdown $decision.target_markdown `
            -Caption $decision.caption `
            -UseMode $decision.use_mode
    }
}

$markdownReplacements = @{
    "docs/internship-part-1.md" = @{
        "../_work/extracted/docx-images/image4.jpg" = "../assets/images/part-1/siemens-energy-context.jpg"
        "../_work/extracted/docx-images/image5.jpg" = "../assets/images/part-1/mcdonalds-burgernomics-concept.jpg"
        "../_work/extracted/docx-images/image6.jpeg" = "../assets/images/part-1/disney-service-design-01.jpeg"
        "../_work/extracted/docx-images/image7.jpeg" = "../assets/images/part-1/disney-service-design-02.jpeg"
        "../_work/extracted/docx-images/image8.jpeg" = "../assets/images/part-1/nusret-experience-economy-collage.jpg"
        "../assets/images/part-1/siemens-energy-business-units.webp" = "../assets/images/part-1/siemens-energy-context.jpg"
    }
    "docs/internship-part-2.md" = @{
        "../_work/extracted/docx-images/image80.JPG" = "../assets/images/part-2/intensity-functions-annotated.webp"
        "../_work/extracted/docx-images/image58.JPG" = "../assets/images/part-2/response-times-high-workload.webp"
        "../_work/extracted/docx-images/image68.JPG" = "../assets/images/part-2/availability-penalty-high-workload.webp"
        "../figures/article2/intensity-functions-annotated.webp" = "../assets/images/part-2/intensity-functions-annotated.webp"
        "../figures/article2/response-times-high-workload.webp" = "../assets/images/part-2/response-times-high-workload.webp"
        "../figures/article2/availability-penalty-high-workload.webp" = "../assets/images/part-2/availability-penalty-high-workload.webp"
    }
}

foreach ($mdRel in $markdownReplacements.Keys) {
    $mdPath = Join-Path $Repo $mdRel
    if (-not (Test-Path -LiteralPath $mdPath)) {
        continue
    }
    Backup-File -Path $mdPath
    $text = Get-Content -LiteralPath $mdPath -Raw -Encoding UTF8
    foreach ($old in $markdownReplacements[$mdRel].Keys) {
        $text = $text.Replace($old, $markdownReplacements[$mdRel][$old])
    }
    Set-Content -LiteralPath $mdPath -Value $text -Encoding UTF8
}

Backup-File -Path $ManifestPath
$manifestRows |
    Sort-Object source, old_name |
    Export-Csv -LiteralPath $ManifestPath -NoTypeInformation -Encoding UTF8

Write-Host "Optimized/normalized public images under assets/images/part-1 and assets/images/part-2"
Write-Host "Wrote manifest: $ManifestPath"
if ((Test-Path -LiteralPath $BackupRoot) -and -not $NoBackup) {
    Write-Host "Backups: $BackupRoot"
}
