# Main Agent Operating Notes (Cloud Native DevOps Materials)

This repository is now used to author a Cloud Native DevOps lecture track.
Previous AWS materials are archived under `archive/` and are not the active baseline.

## Source Of Truth

- Primary: Kubernetes official documentation, CNCF project documentation, Docker documentation, AWS official documentation, and production-grade cloud native operational practices.
- Secondary: course team decisions captured in `cloud-native/README.md`, `cloud-native/teams/README.md`, and agent role documents under `agents/`.
- Visual language: stickman-style scenario images plus clear Mermaid diagrams.

## Course Shape (Current Decisions)

- Learner-facing lecture materials under `cloud-native/` must be written in Korean.
- Keep file names, folder names, commands, and product names in English when that improves tool compatibility or technical accuracy.
- Target course: 6 weeks, 5 days per week, 30 full-day sessions total.
- Session length: 8 classroom hours, 09:00 to 18:00.
- Daily rhythm:
  - 50-minute lesson blocks
  - 10-minute breaks
  - Lunch starts at 13:00
  - Eight lesson blocks per day
- Default split:
  - Theory, concept building, and guided discussion: 5 to 6 hours
  - Instructor demo, video, or surprising application showcase: 30 to 60 minutes
  - Hands-on lab or mission: 1 to 2 hours
  - Review, quiz, and reflection: 30 minutes
- Every session must include:
  - A concrete production scenario
  - One architecture or flow diagram
  - One hands-on lab, playful mission, instructor demo, or curated media activity
  - Security, networking, and observability implications when relevant
  - A short instructor delivery note
- From week 2 onward:
  - Raise the expected learner level to university STEM majors and early junior engineers.
  - Increase material depth and volume to roughly twice the week 1 baseline.
  - Include hands-on labs as a primary learning surface, not a short add-on.
  - Verify hands-on labs with runnable commands, expected output, troubleshooting, and cleanup.
  - Include each service or technology's evolution, industry trend, or operational backstory when it helps students stay engaged.
  - Include architecture PNG diagrams in addition to any stickman scenario images.

## Active Course Domains

1. Docker and container foundations
2. Kubernetes core architecture and workloads
3. Kubernetes networking
4. Cloud native security
5. AWS cloud native computing
6. Observability and operations

## Output Layout

- Course root: `cloud-native/`
- Week folders: `cloud-native/weekNN/`
- Day folders: `cloud-native/weekNN/dayDD/`
- Recommended day files:
  - `README.md` for scenario, goals, timebox, and reading order
  - `01-theory.md` for core concepts and decision rules
  - `02-lab.md` for hands-on instructions
  - `03-instructor-notes.md` for facilitation, timing, and expected mistakes
  - `04-quiz.md` for review questions

## Quality Gates

- Accuracy: Use official docs as the default factual baseline.
- Practicality: Labs must be runnable on a realistic student machine or clearly state environment requirements.
- Safety: Labs must avoid real production credentials, unmanaged cloud spend, and destructive shared-cluster actions.
- Completeness: Labs must include expected output, verification commands, troubleshooting notes, and cleanup.
- Hands-on verification: Week 2+ lab steps must be checked for command order, prerequisites, expected state, failure modes, and cleanup.
- Cloud native fit: Each topic must connect to deployment, scaling, networking, security, or operations.
- Teaching fit: Each session must include instructor prompts and common learner failure modes.
- Schedule fit: Each day README must include the 09:00-18:00 block index.
- Visual fit: Each major concept should have either a Mermaid diagram or stickman scenario image prompt.
- Week 2+ visual fit: Student-facing materials must embed at least one architecture PNG per day, separate from stickman images.
- Learning design: Use See, Explain, Do, Diagnose, Reflect as the default teaching loop.
- Accessibility: Write for non-CS university students first, then provide optional deep-dive materials for advanced learners.

## Team Model

- Content Production Team owns curriculum, theory, labs, quizzes, and visual briefs.
- Instructor Team owns delivery flow, live demo reliability, classroom troubleshooting, and feedback loops.
- Design Partner owns the visual system, stickman image consistency, diagrams, slide readability, and worksheet layout.
- Main Agent coordinates scope, quality, and cross-team handoff.

## Mistake Prevention Log

### 2026-05-08

- Course direction changed from the previous AWS-focused track to Cloud Native DevOps.
- Archived old AWS materials under `archive/`.
- Active content now belongs under `cloud-native/`.
- Agent roles must be mapped to content production, instructor delivery, visual design, lab QA, and skill orchestration.
- VAKOG was removed from the active design method and archived under `archive/VAKOG.md`.
- Active teaching loop changed to See, Explain, Do, Diagnose, Reflect.
