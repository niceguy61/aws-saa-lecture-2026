# Day 03 - CloudTrail/Config + detection services (감사/준수/탐지)

![고객 사례 삽화 - CloudTrail 감사 추적](../../assets/scenario_image/w1d3s1.png)

## Outcomes

- CloudTrail과 Config의 차이를 “기록 대상/용도”로 구분한다.
- “누가 무엇을 했나(CloudTrail)” vs “리소스가 어떤 상태였나(Config)”를 시험형 문장으로 설명한다.
- GuardDuty/Security Hub/Inspector의 역할을 개념 수준에서 연결한다(탐지/집계/취약점).
- 예시 Trail 설정/로그를 보며, 실제 API 이벤트가 감사 로그로 남는 흐름을 따라간다.

## Services In Scope

- CloudTrail (Event history, Trail, S3 로그 저장)
- AWS Config (recording/compliance 개념, 예시 수준)
- GuardDuty / Security Hub / Inspector (탐지/집계/취약점 개념)

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [CloudTrail (누가/언제/무엇을 했나: 행위의 근거)](01-cloudtrail.md)
- [AWS Config (구성 상태 + 준수/규칙 위반)](02-config.md)
- [Detection services (GuardDuty / Security Hub / Inspector)](03-detection-services.md)

> “행위(CloudTrail) vs 상태(Config) vs 탐지/집계(GuardDuty/Security Hub)”를 분리해서 읽으면 소거가 빨라진다.

## Core Concepts

- Audit vs Compliance vs Detection
  - Audit: “누가/언제/무엇을 했는가”를 재구성(CloudTrail)
  - Compliance/Config state: “리소스가 어떤 구성인지/규칙 위반인지”(Config)
  - Detection: “이상 행위/위협”을 찾아 findings로 만들고 연결(GuardDuty/Security Hub 등)

![CloudTrail vs Config vs CloudWatch (audit and observability)](../../assets/core/observability-audit.svg)

## Quick Comparison Table

| Question | Best tool | Why |
|---|---|---|
| 누가 보안 그룹 인바운드를 열었나 | CloudTrail | API 호출 근거 |
| 현재 보안 그룹 규칙이 기준 위반인가 | Config | 구성/준수 |
| 의심스러운 활동을 탐지/알림하고 싶다 | GuardDuty/Security Hub | 탐지/집계 |

## Exam Traps (확장)

- CloudTrail과 Config를 “둘 다 로그니까 동일”로 보는 선택지: 기록 목적이 다르다.
- “탐지 서비스가 곧 로그 저장소”라는 오해: 탐지는 소스(CloudTrail 등) 위에서 동작한다.
- 데이터 이벤트/고급 기능을 무조건 켜는 답: 요구사항/비용 트레이드오프를 본다.
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “감사(audit)”와 “준수(compliance)” 요구를 동시에 충족하려면 어떤 조합이 자연스러운가?
- “누가 보안 그룹을 열었는지”와 “현재 보안 그룹이 어떤 규칙인지”는 같은 질문인가?
- 탐지 서비스(GuardDuty 등)는 “로그 소스”가 무엇인지(CloudTrail/VPC Flow Logs/DNS 등)와 어떻게 연결되는가?

## TL;DR (한 줄 정리)

- “누가 했나”는 **CloudTrail**, “구성이 어땠나/준수인가”는 **Config**, “이상 징후를 찾고 모아라”는 **GuardDuty + Security Hub(+ Inspector)**로 푼다.
