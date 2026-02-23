param(
  [Parameter(Mandatory=$true)][int]$Week,
  [Parameter(Mandatory=$true)][int]$Day,
  [int]$LabSteps = 7,
  [int]$QuizQuestions = 5
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot\..
python -m src.cli validate --week $Week --day $Day --lab-steps $LabSteps --quiz-questions $QuizQuestions

