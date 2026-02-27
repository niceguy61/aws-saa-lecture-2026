# Day 03 - CloudTrail/Config + detection services (audit/detect)

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

## Exam-Style Design Questions

- “감사(audit)”와 “준수(compliance)” 요구를 동시에 충족하려면 어떤 조합이 자연스러운가?
- “누가 보안 그룹을 열었는지”와 “현재 보안 그룹이 어떤 규칙인지”는 같은 질문인가?
- 탐지 서비스(GuardDuty 등)는 “로그 소스”가 무엇인지(CloudTrail/VPC Flow Logs/DNS 등)와 어떻게 연결되는가?
