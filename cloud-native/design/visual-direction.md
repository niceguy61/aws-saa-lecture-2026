# Visual Direction

The course visual system should feel practical, readable, and memorable.
It should support technical understanding first and personality second.

## Core Idea

Use simple stickman workplace scenes to show the human side of cloud native engineering:

- deployment pressure
- broken networking
- unsafe secrets
- confusing dashboards
- incident response
- design tradeoff discussions

Pair those scenes with clean Mermaid diagrams and compact technical tables.

## Stickman Style

Use the existing stickman concept as the default illustration language.

Style rules:

- White or light background
- Black line art
- Minimal color accents for systems, warnings, traffic paths, and status
- Clear facial expressions and body posture
- Simple props: laptop, terminal, whiteboard, dashboard, cluster map
- No dense UI screenshots inside illustrations
- No decorative complexity that competes with the lesson

## Diagram Style

Mermaid diagrams should be plain and GitHub-safe:

- Prefer `flowchart LR` for paths and `sequenceDiagram` for request flow.
- Keep node labels short.
- Avoid slash-heavy labels, parentheses, smart quotes, and dense nested graphs.
- Use diagrams to answer one question, not every question.

## Slide And Document Tone

- Use direct headings that name the engineering decision.
- Keep tables compact and comparison-oriented.
- Use callouts for warnings, cost risks, security risks, and cleanup steps.
- Avoid decorative cards and marketing-style layouts.
- Keep screenshots and command output readable at classroom projector size.

## Image Brief Template

```md
### Image Brief

- Session:
- Scene:
- Characters:
- Technical object:
- Emotion:
- Must show:
- Must avoid:
- Prompt:
```

## Example Stickman Prompt

Simple black-and-white stickman illustration on a clean white background. A developer points at a Kubernetes service diagram on a whiteboard while another developer looks confused at a terminal showing a failed request. Add small blue arrows for traffic flow and one red warning marker near a blocked network policy. Minimal line art, classroom-friendly, no text labels inside the image.

