param(
  [string]$Path = "cloud-native",
  [switch]$Strict
)

$ErrorActionPreference = "Stop"

function Add-Finding {
  param(
    [System.Collections.Generic.List[object]]$List,
    [string]$File,
    [int]$Line,
    [string]$Severity,
    [string]$Rule,
    [string]$Message
  )
  $List.Add([pscustomobject]@{
    file = $File
    line = $Line
    severity = $Severity
    rule = $Rule
    message = $Message
  }) | Out-Null
}

if (-not (Test-Path -LiteralPath $Path)) {
  Write-Host "ERROR: Path not found: $Path"
  exit 2
}

$mdFiles = Get-ChildItem -LiteralPath $Path -Recurse -File -Filter *.md | Select-Object -ExpandProperty FullName
if (-not $mdFiles -or $mdFiles.Count -eq 0) {
  Write-Host "OK: no markdown files found under: $Path"
  exit 0
}

$findings = New-Object System.Collections.Generic.List[object]

foreach ($file in $mdFiles) {
  $lines = Get-Content -LiteralPath $file -Encoding UTF8
  $inMermaid = $false
  $fenceStartLine = 0

  for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]

    if (-not $inMermaid -and $line -match '^```mermaid\s*$') {
      $inMermaid = $true
      $fenceStartLine = $i + 1
      continue
    }

    if ($inMermaid -and $line -match '^```\s*$') {
      $inMermaid = $false
      $fenceStartLine = 0
      continue
    }

    if (-not $inMermaid) { continue }

    # Hard errors: these often break GitHub mermaid rendering.
    if ($line -match "`t") {
      Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "tab" -Message "Tab character inside mermaid block."
    }
    # Smart quotes U+201C/U+201D (avoid embedding unicode directly to prevent encoding issues)
    if ($line -match "[\u201C\u201D]") {
      Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "smart_quotes" -Message "Smart quotes inside mermaid block."
    }
    if ($line -match '\-\.\s*\(.*?\)\s*\.\-\>') {
      Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "edge_label_parentheses" -Message "Dashed edge label uses parentheses: '-. (text) .->' (often breaks)."
    }
    if ($line -match '^\s*participant\s+\w+\s+as\s+.*[()/].*') {
      Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "seq_alias_special" -Message "sequenceDiagram participant alias contains '(' or ')' or '/'."
    }

    # subgraph lines: common GitHub renderer failure when nodes are appended on the same line.
    # Bad: 'subgraph B[Title] SCP[Node]' or 'subgraph Title A[Node]'
    if ($line -match '^\s*subgraph\s+\S+\s+\w+\[') {
      Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "subgraph_inline_node" -Message "subgraph line includes a node definition on the same line. Put nodes on separate lines."
    }
    if ($line -match '^\s*subgraph\b.*\]\s+\S+') {
      Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "subgraph_trailing_tokens" -Message "subgraph line has trailing tokens after closing ']'. Keep subgraph header on its own line."
    }

    # Flowchart node labels: flag risky characters inside [label] unless quoted ["..."].
    $matches = [regex]::Matches($line, '(?<id>\b[A-Za-z0-9_]+)\[(?<label>[^\]]+)\]')
    foreach ($m in $matches) {
      $label = $m.Groups["label"].Value

      # Skip quoted labels like ["SCP: Org, OU, Account"]
      if ($label.StartsWith('"') -and $label.EndsWith('"')) { continue }

      if ($label -match '[()/]') {
        Add-Finding -List $findings -File $file -Line ($i + 1) -Severity "ERROR" -Rule "node_label_special" -Message "Node label contains '(' or ')' or '/': [$label]. Prefer plain text (e.g. 'A - B') or quoted label."
      } elseif ($label -match ':') {
        $sev = "WARN"
        if ($Strict) { $sev = "ERROR" }
        Add-Finding -List $findings -File $file -Line ($i + 1) -Severity $sev -Rule "node_label_colon" -Message "Node label contains ':' (can break on some renderers): [$label]."
      }
    }
  }

  if ($inMermaid) {
    Add-Finding -List $findings -File $file -Line $fenceStartLine -Severity "ERROR" -Rule "unclosed_fence" -Message "Unclosed mermaid fence (missing closing ```)."
  }
}

if ($findings.Count -eq 0) {
  Write-Host "OK: Mermaid lint passed ($($mdFiles.Count) files scanned under '$Path')."
  exit 0
}

$errors = $findings | Where-Object { $_.severity -eq "ERROR" }
$warns  = $findings | Where-Object { $_.severity -eq "WARN" }

Write-Host "Mermaid lint findings:"
($findings | Sort-Object file, line, severity, rule) | Format-Table -AutoSize | Out-String | Write-Host

Write-Host ("Summary: {0} error(s), {1} warning(s)." -f @($errors).Count, @($warns).Count)

if (@($errors).Count -gt 0) { exit 1 }
if (@($warns).Count -gt 0 -and $Strict) { exit 1 }
exit 0
