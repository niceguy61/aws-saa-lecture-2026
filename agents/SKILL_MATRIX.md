# Agent And Skill Matrix

This matrix maps course agents to project Codex skills under `.codex/skills`.

For this desktop session, the same skills may also be mirrored to `C:\Users\sunny\.codex\skills` so they are visible to the current global skill discovery mechanism.

| Agent | Primary Responsibility | Skills |
|---|---|---|
| MAIN | Direction, consistency, handoff, quality gates | All course skills as needed |
| CURRICULUM_PLANNER | Scope, progression, pacing | `cloud-native-course-production` |
| TOPIC_DEEP_DIVE | Theory, tradeoffs, diagrams | `cloud-native-course-production`, `stickman-visual-brief` |
| HANDSON_LAB_DESIGNER | Labs, verification, cleanup | `cloud-native-course-production`, `cloud-native-lab-qa` |
| INSTRUCTOR_LEAD | Live delivery, demo flow, common mistakes | `cloud-native-course-production`, `cloud-native-lab-qa` |
| ASSESSMENT_AUTHOR | Quizzes, debrief prompts, answer keys | `cloud-native-course-production` |
| VISUAL_DESIGNER | Diagrams, stickman briefs, visual consistency | `stickman-visual-brief` |
| QA_REVIEWER | Runnable checks, safety, readiness | `cloud-native-lab-qa` |

## Recommended Agent Flow

1. MAIN confirms scope and output target.
2. CURRICULUM_PLANNER defines week/day outcomes.
3. TOPIC_DEEP_DIVE drafts theory and diagrams.
4. HANDSON_LAB_DESIGNER drafts labs.
5. INSTRUCTOR_LEAD adds delivery notes.
6. ASSESSMENT_AUTHOR adds quiz and debrief.
7. VISUAL_DESIGNER adds diagram polish and stickman briefs.
8. QA_REVIEWER checks links, labs, commands, safety, and readiness.
9. MAIN reconciles findings and updates durable operating notes.
