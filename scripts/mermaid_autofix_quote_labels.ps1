param(
  [string]$Path = "cloud-native",
  [switch]$WhatIf
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Read-TextFileUtf8NoBom([string]$filePath) {
  [System.IO.File]::ReadAllText($filePath, [System.Text.UTF8Encoding]::new($false))
}

function Write-TextFileUtf8NoBom([string]$filePath, [string]$content) {
  [System.IO.File]::WriteAllText($filePath, $content, [System.Text.UTF8Encoding]::new($false))
}

if (-not (Test-Path -LiteralPath $Path)) {
  throw "Path not found: $Path"
}

$mdFiles = Get-ChildItem -LiteralPath $Path -Recurse -File -Filter *.md | Select-Object -ExpandProperty FullName
if (-not $mdFiles -or $mdFiles.Count -eq 0) {
  Write-Host "No markdown files found under: $Path"
  exit 0
}

$changedFiles = 0
$totalReplacements = 0

foreach ($file in $mdFiles) {
  $content = Read-TextFileUtf8NoBom $file
  $nl = if ($content.Contains("`r`n")) { "`r`n" } else { "`n" }
  $lines = $content -split "\r?\n", -1

  $inMermaid = $false
  $fileReplacements = 0

  for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]

    if (-not $inMermaid -and $line -match '^```mermaid\s*$') {
      $inMermaid = $true
      continue
    }
    if ($inMermaid -and $line -match '^```\s*$') {
      $inMermaid = $false
      continue
    }
    if (-not $inMermaid) { continue }

    $lines[$i] = [regex]::Replace(
      $lines[$i],
      '(?<id>\b[A-Za-z0-9_]+)\[(?<label>[^\]]+)\]',
      {
        param($m)
        $id = $m.Groups["id"].Value
        $label = $m.Groups["label"].Value

        if ($label.StartsWith('"') -and $label.EndsWith('"')) { return $m.Value }

        if ($label -match '[()/:\u201C\u201D]' -or $label.Contains("/")) {
          $script:fileReplacements++
          return "$id[`"$label`"]"
        }

        return $m.Value
      }
    )
  }

  if ($fileReplacements -eq 0) { continue }

  $newContent = $lines -join $nl
  if ($newContent -ne $content) {
    if ($WhatIf) {
      Write-Host "[WhatIf] $file : $fileReplacements replacement(s)"
    } else {
      Write-TextFileUtf8NoBom $file $newContent
    }
    $changedFiles++
    $totalReplacements += $fileReplacements
  }
}

Write-Host ("Updated files: {0}, replacements: {1}" -f $changedFiles, $totalReplacements)
