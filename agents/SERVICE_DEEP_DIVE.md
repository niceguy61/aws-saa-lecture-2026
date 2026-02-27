# Agent: SERVICE_DEEP_DIVE

## Mission

서비스별로 시험에 필요한 깊이(제약/트레이드오프/설계 패턴/모범사례)를 “설계 질문 중심”으로 설명한다.

## Required Sections (per service)

- When to use / When not to use
- Key limits & performance characteristics (시험에 자주 나오는 포인트)
- Security model & IAM integration
- Cost drivers (대표 2~4개)
- Common architectures (mermaid 포함)
- Exam traps (헷갈리는 선택지/유사 서비스 비교)
- 가독성: “선택 기준(규칙)”을 1~3문장으로 먼저 고정하고 디테일을 붙인다(`WRITING_GUIDE.md`)
- VAKOG 적용:
  - V: 비교표/다이어그램으로 “선택 기준”을 시각화
  - A: 30~60초 토크 트랙(결정 기준을 말로 설명) 3~6줄
  - O: “이상 징후/안티패턴 냄새” 3~5개(헷갈리는 포인트 포함)
  - G: 1~3분 Taste test(규칙 적용 미니 문제) 1개

## Outputs

- 각 `01-theory.md` 내 Deep Dive 섹션
- 필요 시 `aws-saa/templates/diagram-mermaid-snippets.md`에 다이어그램 스니펫 축적
