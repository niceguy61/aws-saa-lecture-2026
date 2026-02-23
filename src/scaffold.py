from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from .curriculum import CurriculumEntry, guess_domain, official_links_for_domain


@dataclass(frozen=True)
class ScaffoldConfig:
    lab_steps_min: int = 7
    quiz_questions_min: int = 5
    deep_dive_scenarios_min: int = 2


def _mermaid_placeholder(domain: str) -> str:
    if domain == "docker":
        return "\n".join(
            [
                "```mermaid",
                "flowchart TD",
                "  Dev[Developer] --> CLI[Docker CLI]",
                "  CLI --> Daemon[Docker Daemon]",
                "  Daemon --> Image[Image]",
                "  Daemon --> Container[Container]",
                "```",
            ]
        )
    if domain == "kubernetes":
        return "\n".join(
            [
                "```mermaid",
                "graph TD",
                "  User[User] -->|kubectl| API[API Server]",
                "  API --> Scheduler[Scheduler]",
                "  API --> Controller[Controller Manager]",
                "  API --> ETCD[(etcd)]",
                "  Scheduler --> Node[Node]",
                "  Node --> Pod[Pod]",
                "```",
            ]
        )
    return "\n".join(
        [
            "```mermaid",
            "flowchart TD",
            "  A[Topic] --> B[Key Concepts]",
            "  B --> C[Hands-on]",
            "  B --> D[Troubleshooting]",
            "```",
        ]
    )


def render_service_understanding(entry: CurriculumEntry, cfg: ScaffoldConfig) -> str:
    domain = guess_domain(entry.topic)
    links = list(official_links_for_domain(domain))
    links_md = "\n".join([f"- [{name}]({url})" for name, url in links]) or "- (Add official links)"
    return "\n".join(
        [
            "# 서비스 이해 (Service Understanding)",
            "",
            "## 1. 배경 정보",
            "",
            "<details>",
            "<summary>배경 정보 보기</summary>",
            "",
            "- (Why was it created?)",
            "- (What problem does it solve?)",
            "- (Historical context, evolution)",
            "",
            "### 인포그래픽",
            "",
            _mermaid_placeholder(domain),
            "",
            "</details>",
            "",
            "## 2. 핵심 개념",
            "",
            "<details>",
            "<summary>핵심 개념 보기</summary>",
            "",
            "- (Core concept 1)",
            "- (Core concept 2)",
            "- (Core concept 3)",
            "",
            "### 인포그래픽",
            "",
            _mermaid_placeholder(domain),
            "",
            "</details>",
            "",
            "## 3. 장단점",
            "",
            "<details>",
            "<summary>장단점 보기</summary>",
            "",
            "**장점**:",
            "- (Advantage 1)",
            "- (Advantage 2)",
            "- (Advantage 3)",
            "",
            "**단점**:",
            "- (Disadvantage 1)",
            "- (Disadvantage 2)",
            "",
            "</details>",
            "",
            "## 4. 자주 사용되는 사례",
            "",
            "<details>",
            "<summary>사용 사례 보기</summary>",
            "",
            "1. (Use case 1)",
            "2. (Use case 2)",
            "3. (Use case 3)",
            "",
            "</details>",
            "",
            "## 5. 연관 서비스",
            "",
            "<details>",
            "<summary>연관 서비스 보기</summary>",
            "",
            "- (Related service 1)",
            "- (Related service 2)",
            "- (Alternative 1)",
            "",
            "</details>",
            "",
            "## 6. 공식 문서 링크",
            "",
            links_md,
            "",
            "## 7. 추가 자료",
            "",
            "- (Optional: blog post, community resource)",
            "",
        ]
    )


def render_deep_dive(entry: CurriculumEntry, cfg: ScaffoldConfig) -> str:
    domain = guess_domain(entry.topic)
    lines: List[str] = ["# Deep Dive - 트러블슈팅", ""]
    for idx in range(1, cfg.deep_dive_scenarios_min + 1):
        lines.extend(
            [
                f"## 시나리오 {idx}: (Scenario title)",
                "",
                "### 트러블슈팅 흐름도",
                "",
                _mermaid_placeholder(domain),
                "",
                "### 시나리오 설명",
                "",
                "<details>",
                "<summary>문제 상황 보기</summary>",
                "",
                "- 증상:",
                "- 환경:",
                "- 에러 메시지(있다면):",
                "",
                "</details>",
                "",
                "### 원인 분석",
                "",
                "<details>",
                "<summary>원인 분석 보기</summary>",
                "",
                "- (Root cause analysis)",
                "",
                "</details>",
                "",
                "### 원인 확인 방법",
                "",
                "<details>",
                "<summary>진단 단계 보기</summary>",
                "",
                "```bash",
                "# Step 1:",
                "# Step 2:",
                "```",
                "",
                "</details>",
                "",
                "### 수정 방법",
                "",
                "<details>",
                "<summary>해결 단계 보기</summary>",
                "",
                "```bash",
                "# Fix step 1:",
                "# Fix step 2:",
                "```",
                "",
                "</details>",
                "",
                "### 정상 확인 방법",
                "",
                "<details>",
                "<summary>검증 단계 보기</summary>",
                "",
                "```bash",
                "# Verify step 1:",
                "# Verify step 2:",
                "```",
                "",
                "</details>",
                "",
                "---",
                "",
            ]
        )
    return "\n".join(lines)


def render_quiz(entry: CurriculumEntry, cfg: ScaffoldConfig) -> str:
    lines: List[str] = ["# 퀴즈 (Quiz)", ""]
    for i in range(1, cfg.quiz_questions_min + 1):
        lines.extend(
            [
                f"## 질문 {i}",
                "",
                "**(Write the question)**",
                "",
                "A) (choice A)",
                "B) (choice B)",
                "C) (choice C)",
                "D) (choice D)",
                "",
                "<details>",
                "<summary>정답 및 해설 보기</summary>",
                "",
                "**답**: (A/B/C/D)",
                "",
                "**설명**: (Write a detailed explanation, 100+ chars)",
                "",
                "</details>",
                "",
                "---",
                "",
            ]
        )
    return "\n".join(lines)


def render_handson_step(
    entry: CurriculumEntry,
    cfg: ScaffoldConfig,
    step_num: int,
    total_steps: int,
) -> str:
    domain = guess_domain(entry.topic)
    head = [f"# Hands-on Lab - Step {step_num}", ""]

    if step_num == 1:
        head.extend(
            [
                "## 실습 개요",
                "",
                f"**제목**: {entry.topic} 실습",
                "",
                "**목적**: (Why this lab matters)",
                "",
                "**학습 목표**:",
                "- (Objective 1)",
                "- (Objective 2)",
                "- (Objective 3)",
                "",
                "**예상 소요 시간**: 60-90분",
                "",
                "**난이도**: Beginner/Intermediate",
                "",
                "### 실습 흐름도",
                "",
                _mermaid_placeholder(domain),
                "",
                "## 사전 요구사항",
                "",
                "<details>",
                "<summary>사전 요구사항 보기</summary>",
                "",
                "- (Prerequisite 1) - Official link: (URL)",
                "- (Prerequisite 2) - Official link: (URL)",
                "",
                "</details>",
                "",
                "## 환경 설정",
                "",
                "<details>",
                "<summary>환경 설정 보기</summary>",
                "",
                "- (Setup step 1) - Official link: (URL)",
                "- (Setup step 2) - Official link: (URL)",
                "",
                "</details>",
                "",
                "---",
                "",
            ]
        )

    head.extend(
        [
            f"## Step {step_num}: (Step title)",
            "",
            "**목표**: (What you achieve in this step)",
            "",
            "**명령어**:",
            "<details>",
            "<summary>명령어 보기</summary>",
            "",
            "```bash",
            "# Command 1",
            "# Command 2",
            "```",
            "",
            "</details>",
            "",
            "**예상 출력**:",
            "<details>",
            "<summary>예상 출력 보기</summary>",
            "",
            "```",
            "(expected output snippet)",
            "```",
            "",
            "</details>",
            "",
            "**확인 방법**:",
            "<details>",
            "<summary>확인 방법 보기</summary>",
            "",
            "```bash",
            "# Verification command",
            "```",
            "",
            "</details>",
            "",
            "**문제 해결**:",
            "<details>",
            "<summary>문제 해결 보기</summary>",
            "",
            "- (Common error 1) -> (Fix)",
            "- (Common error 2) -> (Fix)",
            "",
            "</details>",
            "",
        ]
    )

    if step_num == total_steps:
        head.extend(
            [
                "---",
                "",
                "## 실습 완료",
                "",
                "- (Completion summary: what you learned)",
                "",
                "**다음 단계**:",
                "- (Next step 1)",
                "- (Next step 2)",
                "- (Next step 3)",
                "",
            ]
        )

    return "\n".join(head)


def build_scaffold_files(entry: CurriculumEntry, cfg: ScaffoldConfig) -> Dict[str, str]:
    files: Dict[str, str] = {}
    files["service_understanding.md"] = render_service_understanding(entry, cfg)
    files["deep_dive.md"] = render_deep_dive(entry, cfg)
    files["quiz.md"] = render_quiz(entry, cfg)
    for i in range(1, cfg.lab_steps_min + 1):
        files[f"handson_step{i}.md"] = render_handson_step(entry, cfg, i, cfg.lab_steps_min)
    return files


def write_scaffold(output_dir: Path, entry: CurriculumEntry, cfg: ScaffoldConfig) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written: List[Path] = []
    for name, content in build_scaffold_files(entry, cfg).items():
        path = output_dir / name
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written

