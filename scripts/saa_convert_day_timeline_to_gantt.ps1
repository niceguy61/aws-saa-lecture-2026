param(
  [string]$Root = "aws-saa",
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

function Normalize-TaskName([string]$raw) {
  $name = $raw.Trim()
  $name = $name -replace '<br\\s*/?>', ' '
  $name = $name -replace '\s+', ' '
  $name = $name -replace '^\d+\-\d+m:\s*', ''

  # Make it robust for gantt parsing: avoid ':' in task name.
  $name = $name -replace ':', ' -'

  # If it looks like 'A(B)' -> 'A - B'
  if ($name -match '^(?<a>[^()]+)\((?<b>[^()]+)\)$') {
    $name = ($Matches["a"].Trim() + " - " + $Matches["b"].Trim())
  }

  return $name.Trim()
}

function Minutes-ToTime([int]$minutes) {
  $h = [int]([math]::Floor($minutes / 60))
  $m = $minutes % 60
  return ("{0:D2}:{1:D2}" -f $h, $m)
}

function Build-GanttBlock([object[]]$segments, [string]$nl) {
  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add('```mermaid') | Out-Null
  $lines.Add('gantt') | Out-Null
  $lines.Add('  title Learning Timeline') | Out-Null
  $lines.Add('  dateFormat  HH:mm') | Out-Null
  $lines.Add('  axisFormat  %H:%M') | Out-Null
  $lines.Add('  section Day') | Out-Null

  for ($i = 0; $i -lt $segments.Count; $i++) {
    $seg = $segments[$i]
    $task = Normalize-TaskName $seg.title
    $id = ("t{0}" -f ($i + 1))
    $dur = ("{0}m" -f $seg.durationMin)

    if ($i -eq 0) {
      $start = Minutes-ToTime $seg.startMin
      $lines.Add(("  {0} :{1}, {2}, {3}" -f $task, $id, $start, $dur)) | Out-Null
    } else {
      $prevId = ("t{0}" -f $i)
      $lines.Add(("  {0} :{1}, after {2}, {3}" -f $task, $id, $prevId, $dur)) | Out-Null
    }
  }

  $lines.Add('```') | Out-Null
  return ($lines -join $nl)
}

function Extract-TimelineSegments([string[]]$blockLines) {
  $byKey = @{}
  $pattern = '(?<start>\d+)\-(?<end>\d+)m:\s*(?<title>[^"\]]+)'

  foreach ($line in $blockLines) {
    $matches = [regex]::Matches($line, $pattern)
    foreach ($m in $matches) {
      $start = [int]$m.Groups["start"].Value
      $end = [int]$m.Groups["end"].Value
      if ($end -le $start) { continue }

      $key = ("{0}-{1}" -f $start, $end)
      if ($byKey.ContainsKey($key)) { continue }

      $byKey[$key] = [pscustomobject]@{
        startMin = $start
        durationMin = ($end - $start)
        title = ("{0}-{1}m: {2}" -f $start, $end, $m.Groups["title"].Value.Trim())
      }
    }
  }

  return @($byKey.Values | Sort-Object startMin)
}

if (-not (Test-Path -LiteralPath $Root)) {
  throw "Root not found: $Root"
}

$targets = @(Get-ChildItem -LiteralPath $Root -Recurse -File -Filter README.md |
  Where-Object { $_.FullName -like "*\week??\day??\README.md" })

$updated = 0
foreach ($file in $targets) {
  $path = $file.FullName
  $content = Read-TextFileUtf8NoBom $path
  $nl = if ($content.Contains("`r`n")) { "`r`n" } else { "`n" }
  $lines = $content -split "\r?\n", -1

  $idxTimeline = -1
  for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^##\s+Timeline\b') { $idxTimeline = $i; break }
  }
  if ($idxTimeline -lt 0) { continue }

  $idxFenceStart = -1
  for ($i = $idxTimeline + 1; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^```mermaid\s*$') { $idxFenceStart = $i; break }
    if ($lines[$i] -match '^##\s+') { break }
  }
  if ($idxFenceStart -lt 0) { continue }

  $idxFenceEnd = -1
  for ($i = $idxFenceStart + 1; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^```\s*$') { $idxFenceEnd = $i; break }
  }
  if ($idxFenceEnd -lt 0) { continue }

  $block = $lines[($idxFenceStart + 1)..($idxFenceEnd - 1)]
  if (($block -join "`n") -match '^\s*gantt\b') { continue }

  $segments = Extract-TimelineSegments $block
  if (-not $segments -or $segments.Count -eq 0) {
    continue
  }

  $segments = $segments | Sort-Object startMin
  $gantt = Build-GanttBlock -segments $segments -nl $nl

  $newLines = @()
  $newLines += $lines[0..($idxFenceStart - 1)]
  $newLines += ($gantt -split "\r?\n", -1)
  $newLines += $lines[($idxFenceEnd + 1)..($lines.Length - 1)]

  $newContent = ($newLines -join $nl)
  if ($newContent -eq $content) { continue }

  if ($WhatIf) {
    Write-Host "[WhatIf] would update: $path"
  } else {
    Write-TextFileUtf8NoBom $path $newContent
  }
  $updated++
}

Write-Host "Updated day READMEs: $updated / $($targets.Count)"
