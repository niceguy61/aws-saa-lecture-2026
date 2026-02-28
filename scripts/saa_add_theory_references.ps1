param(
  [switch]$WhatIf
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Read-TextFileUtf8NoBom([string]$path) {
  return [System.IO.File]::ReadAllText($path, [System.Text.UTF8Encoding]::new($false))
}

function Write-TextFileUtf8NoBom([string]$path, [string]$content) {
  [System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))
}

function Get-NewLine([string]$content) {
  if ($content.Contains("`r`n")) { return "`r`n" }
  return "`n"
}

function Get-RelativePath([string]$fromDir, [string]$toPath) {
  $fromDirFull = [System.IO.Path]::GetFullPath($fromDir)
  $toPathFull = [System.IO.Path]::GetFullPath($toPath)

  if (-not $fromDirFull.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
    $fromDirFull = $fromDirFull + [System.IO.Path]::DirectorySeparatorChar
  }

  $fromUri = [System.Uri]::new($fromDirFull)
  $toUri = [System.Uri]::new($toPathFull)
  $rel = $fromUri.MakeRelativeUri($toUri).ToString()
  $rel = [System.Uri]::UnescapeDataString($rel)
  return $rel.Replace("\\", "/").Replace("/", "/")
}

function Build-ReferencesBlock([string]$fromDir, [string]$awsSaaRoot) {
  $referencesReadme = Join-Path $awsSaaRoot "references/README.md"
  $examGuide = Join-Path $awsSaaRoot "references/exam-guide.md"
  $glossary = Join-Path $awsSaaRoot "references/glossary.md"
  $awsServices = Join-Path $awsSaaRoot "references/aws-services.md"
  $examKeypoints = Join-Path $awsSaaRoot "exam-keypoints.md"
  $examTrapBank = Join-Path $awsSaaRoot "exam-trap-bank.md"

  return @(
    "## References",
    "",
    "- References index: ``$(Get-RelativePath -fromDir $fromDir -toPath $referencesReadme)``",
    "- Exam guide (SAA-C03): ``$(Get-RelativePath -fromDir $fromDir -toPath $examGuide)``",
    "- Glossary: ``$(Get-RelativePath -fromDir $fromDir -toPath $glossary)``",
    "- AWS services list: ``$(Get-RelativePath -fromDir $fromDir -toPath $awsServices)``",
    "- Exam keypoints: ``$(Get-RelativePath -fromDir $fromDir -toPath $examKeypoints)``",
    "- Exam trap bank: ``$(Get-RelativePath -fromDir $fromDir -toPath $examTrapBank)``"
  ) -join "`n"
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$awsSaaRoot = Join-Path $repoRoot "aws-saa"

if (-not (Test-Path $awsSaaRoot)) {
  throw "aws-saa root not found at: $awsSaaRoot"
}

$targets = @(Get-ChildItem -Recurse -File -Path $awsSaaRoot |
  Where-Object { $_.Extension -eq ".md" } |
  Where-Object {
    $_.FullName -like "*\week??\day??\??-*.md" -or
    ($_.FullName -like "*\special-lectures\*.md" -and $_.Name -ne "README.md")
  } |
  Where-Object { $_.Name -notmatch "(?i)quiz" })

$changed = 0
foreach ($file in $targets) {
  $path = $file.FullName
  $content = Read-TextFileUtf8NoBom $path
  $nl = Get-NewLine $content
  $lines = $content -split "\r?\n", -1

  $kept = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]

    if ($line -match "^(?i)##\s*References\s*$") {
      $i++
      while ($i -lt $lines.Length -and ($lines[$i] -notmatch "^##\s+")) {
        $i++
      }
      $i--
      continue
    }

    $kept.Add($line)
  }

  while ($kept.Count -gt 0 -and $kept[$kept.Count - 1] -eq "") {
    $kept.RemoveAt($kept.Count - 1)
  }

  $blockText = (Build-ReferencesBlock -fromDir $file.DirectoryName -awsSaaRoot $awsSaaRoot).TrimEnd()
  $blockLines = $blockText -split "\r?\n"

  $insertIndex = $kept.Count
  for ($i = 0; $i -lt $kept.Count; $i++) {
    if ($kept[$i] -match "^##\s*Back\s*$") { $insertIndex = $i; break }
    if ($kept[$i] -match "^-\\s*Back\\s*:") { $insertIndex = $i; break }
  }

  if ($insertIndex -gt 0 -and $kept[$insertIndex - 1] -ne "") {
    $kept.Insert($insertIndex, "")
    $insertIndex++
  }

  foreach ($bl in $blockLines) {
    $kept.Insert($insertIndex, $bl)
    $insertIndex++
  }

  $kept.Insert($insertIndex, "")

  $newContent = ($kept.ToArray() -join $nl).TrimEnd() + $nl

  if ($WhatIf) {
    Write-Host "[WhatIf] would update: $($file.FullName)"
    continue
  }

  Write-TextFileUtf8NoBom $path $newContent
  $changed++
}

Write-Host "Updated files: $changed / $($targets.Count)"
