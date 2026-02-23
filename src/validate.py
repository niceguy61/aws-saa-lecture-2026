from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class ValidationIssue:
    severity: str  # "error" | "warning"
    message: str
    file: str


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_day_dir(day_dir: Path, lab_steps_min: int = 7, quiz_questions_min: int = 5) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []

    required = ["service_understanding.md", "deep_dive.md", "quiz.md"]
    for f in required:
        p = day_dir / f
        if not p.exists():
            issues.append(ValidationIssue("error", f"Missing required file: {f}", f))

    lab_steps = sorted(day_dir.glob("handson_step*.md"))
    if len(lab_steps) < lab_steps_min:
        issues.append(
            ValidationIssue(
                "error",
                f"Hands-on steps too few: {len(lab_steps)} (min {lab_steps_min})",
                "hands-on",
            )
        )

    su = day_dir / "service_understanding.md"
    if su.exists():
        su_text = _read(su)
        for key in [
            "배경 정보",
            "핵심 개념",
            "장단점",
            "자주 사용되는 사례",
            "연관 서비스",
            "공식 문서 링크",
            "인포그래픽",
        ]:
            if key not in su_text:
                issues.append(ValidationIssue("error", f"Service Understanding missing section: {key}", su.name))
        if "```mermaid" not in su_text:
            issues.append(ValidationIssue("warning", "Service Understanding missing mermaid diagram", su.name))

    dd = day_dir / "deep_dive.md"
    if dd.exists():
        dd_text = _read(dd)
        scenario_count = len(re.findall(r"(?m)^##\s+시나리오\s+\d+\s*:", dd_text))
        if scenario_count < 2:
            issues.append(ValidationIssue("warning", f"Deep Dive scenarios too few: {scenario_count} (min 2)", dd.name))

    quiz = day_dir / "quiz.md"
    if quiz.exists():
        quiz_text = _read(quiz)
        q_count = len(re.findall(r"(?m)^##\s+질문\s+\d+\s*$", quiz_text))
        if q_count < quiz_questions_min:
            issues.append(
                ValidationIssue(
                    "warning",
                    f"Quiz questions too few: {q_count} (min {quiz_questions_min})",
                    quiz.name,
                )
            )

    for step in lab_steps:
        step_text = _read(step)
        for key in ["목표", "명령어", "예상 출력", "확인 방법", "문제 해결"]:
            if key not in step_text:
                issues.append(ValidationIssue("warning", f"Hands-on step missing: {key}", step.name))
        if "```" not in step_text:
            issues.append(ValidationIssue("warning", "Hands-on step missing code block", step.name))

    return issues
