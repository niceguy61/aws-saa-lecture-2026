param(
  [int]$LabSteps = 7,
  [int]$QuizQuestions = 5
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot\..

for($week = 1; $week -le 4; $week++){
  for($day = 1; $day -le 5; $day++){
    python -m src.cli generate --week $week --day $day --lab-steps $LabSteps --quiz-questions $QuizQuestions
  }
}

