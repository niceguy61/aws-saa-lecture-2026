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

function Format-TwoDigits([int]$n) {
  '{0:00}' -f $n
}

if (-not (Test-Path -LiteralPath $Root)) {
  throw "Root not found: $Root"
}

$dayDirs = @(Get-ChildItem -LiteralPath $Root -Recurse -Directory |
  Where-Object { $_.FullName -like "*\week??\day??" } |
  Sort-Object FullName)

$updated = 0
foreach ($dir in $dayDirs) {
  $mdFiles = @(Get-ChildItem -LiteralPath $dir.FullName -File -Filter '*.md')

  $numberedNonQuiz = @(
    $mdFiles |
      Where-Object { $_.Name -match '^\d{2}-.*\.md$' } |
      Where-Object { $_.Name -notmatch '(?i)quiz\.md$' }
  )

  $max = 0
  foreach ($f in $numberedNonQuiz) {
    if ($f.Name -match '^(\d{2})-') {
      $n = [int]$Matches[1]
      if ($n -gt $max) { $max = $n }
    }
  }

  $desiredQuizNo = $max + 1
  $desiredQuizName = "$(Format-TwoDigits $desiredQuizNo)-quiz.md"

  $quizFiles = @($mdFiles | Where-Object { $_.Name -match '(?i)quiz\.md$' -and $_.Name -match '^\d{2}-' })
  if ($quizFiles.Count -eq 0) {
    Write-Host "WARN: no quiz file found: $($dir.FullName)"
    continue
  }
  if ($quizFiles.Count -gt 1) {
    Write-Host "WARN: multiple quiz files found, skipping: $($dir.FullName) -> $($quizFiles.Name -join ', ')"
    continue
  }

  $quiz = $quizFiles[0]
  $currentQuizName = $quiz.Name
  $currentQuizPath = $quiz.FullName
  $desiredQuizPath = Join-Path $dir.FullName $desiredQuizName

  if ($currentQuizName -ne $desiredQuizName) {
    if ($WhatIf) {
      Write-Host "[WhatIf] rename quiz: $currentQuizName -> $desiredQuizName ($($dir.FullName))"
    } else {
      if (Test-Path -LiteralPath $desiredQuizPath) {
        throw "Target quiz already exists: $desiredQuizPath"
      }
      git mv -- $currentQuizPath $desiredQuizPath | Out-Null
    }
  }

  # Update quiz title line (# NN-quiz - ...)
  $quizPathToEdit = if ($WhatIf) { $currentQuizPath } else { $desiredQuizPath }
  if (-not (Test-Path -LiteralPath $quizPathToEdit)) { continue }

  $quizContent = Read-TextFileUtf8NoBom $quizPathToEdit
  $nl = if ($quizContent.Contains("`r`n")) { "`r`n" } else { "`n" }
  $quizLines = $quizContent -split "\r?\n", -1
  if ($quizLines.Length -gt 0) {
    $rest = $quizLines[0]
    $rest = [regex]::Replace($rest, '^(#\s*)?(\$?\d+|\d{2})-quiz\s*-\s*', '')
    if ([string]::IsNullOrWhiteSpace($rest)) {
      $quizLines[0] = "# $(Format-TwoDigits $desiredQuizNo)-quiz"
    } else {
      $quizLines[0] = "# $(Format-TwoDigits $desiredQuizNo)-quiz - $rest"
    }
    $newQuizContent = $quizLines -join $nl
    if (-not $WhatIf) { Write-TextFileUtf8NoBom $quizPathToEdit $newQuizContent }
  }

  # Update day README quiz link (e.g., (03-quiz.md) or `03-quiz.md`)
  $dayReadme = Join-Path $dir.FullName "README.md"
  if (Test-Path -LiteralPath $dayReadme) {
    $readmeContent = Read-TextFileUtf8NoBom $dayReadme
    $newReadme = $readmeContent
    $newReadme = [regex]::Replace($newReadme, '(?im)\((\d{2}-quiz\.md)\)', "($desiredQuizName)")
    $newReadme = [regex]::Replace($newReadme, '(?im)`(\d{2}-quiz\.md)`', ('`' + $desiredQuizName + '`'))
    if ($newReadme -ne $readmeContent) {
      if ($WhatIf) {
        Write-Host "[WhatIf] update README quiz link: $($dir.FullName)"
      } else {
        Write-TextFileUtf8NoBom $dayReadme $newReadme
      }
    }
  }

  $updated++
}

Write-Host "Processed day dirs: $updated / $($dayDirs.Count)"
