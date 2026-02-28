param(
  [string]$Path = "aws-saa",
  [switch]$Strict
)

$ErrorActionPreference = "Stop"

function Fail($msg) {
  Write-Host "FAIL: $msg"
  exit 1
}

if (-not (Test-Path -LiteralPath $Path)) {
  Fail "Path not found: $Path"
}

$theoryFiles = Get-ChildItem -LiteralPath $Path -Recurse -File -Filter "01-theory.md" | Select-Object -ExpandProperty FullName
if (-not $theoryFiles -or $theoryFiles.Count -eq 0) {
  Write-Host "OK: no 01-theory.md files found under: $Path"
  exit 0
}

$findings = New-Object System.Collections.Generic.List[object]

foreach ($file in $theoryFiles) {
  $lines = Get-Content -LiteralPath $file -Encoding UTF8

  $coreIdx = -1
  for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '^\s*##\s+Core Concepts\s*$') { $coreIdx = $i; break }
  }

  if ($coreIdx -lt 0) {
    $findings.Add([pscustomobject]@{ file=$file; issue="missing Core Concepts header (## Core Concepts)"; hint="Add the section header to match template." }) | Out-Null
    continue
  }

  $endIdx = $lines.Length
  for ($j = $coreIdx + 1; $j -lt $lines.Length; $j++) {
    if ($lines[$j] -match '^\s*##\s+Deep Dive\s*$') { $endIdx = $j; break }
  }

  $coreBlock = $lines[$coreIdx..($endIdx-1)] -join "`n"

  # Core Concepts must include at least one image (markdown image syntax).
  if ($coreBlock -notmatch '!\[[^\]]*\]\([^)]+\)') {
    $findings.Add([pscustomobject]@{ file=$file; issue="no image in Core Concepts"; hint="Add at least one image before ## Deep Dive (SVG/PNG/diagram)." }) | Out-Null
  }

  # Encourage 'Exam must-know' scaffolding for depth (warning unless strict).
  $hasExamMustKnow = $false
  if ($lines | Select-String -SimpleMatch "Exam must-know" -Quiet) { $hasExamMustKnow = $true }
  if (-not $hasExamMustKnow) {
    $sev = "WARN"
    if ($Strict) { $sev = "ERROR" }
    $findings.Add([pscustomobject]@{ file=$file; issue="${sev}: missing 'Exam must-know' blocks"; hint="Add Key point + Why + Alternative under major services/traps." }) | Out-Null
  }
}

if ($findings.Count -eq 0) {
  Write-Host "OK: Theory QA passed ($($theoryFiles.Count) files scanned under '$Path')."
  exit 0
}

Write-Host "Theory QA findings:"
($findings | Sort-Object file, issue) | Format-Table -AutoSize | Out-String | Write-Host

$errors = $findings | Where-Object { $_.issue -like "ERROR:*" -or $_.issue -like "missing*" -or $_.issue -like "no image*" }
if (@($errors).Count -gt 0) {
  exit 1
}

Write-Host "OK (with warnings): review WARN items to improve depth."
exit 0
