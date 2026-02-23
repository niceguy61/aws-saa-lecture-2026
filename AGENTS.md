# Repository Agent Instructions

This repo generates DevOps lecture materials from the steering rules in `.kiro/steering/`.

## Source Of Truth
- Curriculum: `DevOps_6개월_교육과정_커리큘럼.md`
- Steering (must follow): `.kiro/steering/devops-curriculum-guide.md`
- Content rules (must follow): `.kiro/steering/lecture-content-generation-rules.md`

## Output Layout
- Generate lecture files under `lectures/week{N}/day{M}/`.
- Required lecture artifacts:
  - `service_understanding.md`
  - `deep_dive.md`
  - `quiz.md`
  - `handson_step1.md` ... `handson_step7.md` (7+ steps)

## Key Steering Constraints (Practical)
- Each day must include 4 components: Service Understanding, Deep Dive, Hands-on Lab, Quiz.
- Hands-on Lab must be 7+ steps, each step includes: objective, commands, expected output, verification, troubleshooting.
- Service Understanding must include 7 elements and at least one Mermaid infographic.
- Deep Dive must include at least 2 troubleshooting scenarios with diagnosis/resolution/verification steps.
- Quiz must include at least 5 questions, each with choices, answer, explanation.

## Encoding / Console Safety
- Prefer plain ASCII in scripts output (avoid checkmarks like "✓", "✗") to prevent Windows console encoding crashes.

## Commands
- Generate scaffolds: `python -m src.cli generate --week 1 --day 2`
- Validate output folder: `python -m src.cli validate --week 1 --day 2`

