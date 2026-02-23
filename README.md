# DevOps Lecture Scaffold Generator

This repo produces daily DevOps lecture materials based on the steering rules in `.kiro/steering/`.

## What It Generates

For each day, it generates a scaffold that follows EARS rules:
- Service Understanding
- Deep Dive
- Hands-on Lab (7+ steps)
- Quiz (5+ questions)

Output layout:
- `lectures/week{N}/day{M}/`

## Commands

Generate scaffolds:
```bash
python -m src.cli generate --week 1 --day 2
```

Validate a day folder:
```bash
python -m src.cli validate --week 1 --day 2
```

PowerShell helpers:
```powershell
.\scripts\generate_scaffold.ps1 -Week 1 -Day 2
.\scripts\validate_scaffold.ps1 -Week 1 -Day 2
```

## Notes

- The scaffolds are intentionally lightweight templates to guarantee structure compliance.
- Fill in the content manually or extend the generator later with an LLM/RAG layer.

