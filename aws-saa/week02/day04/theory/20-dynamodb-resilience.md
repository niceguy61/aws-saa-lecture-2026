# DynamoDB Resilience (개념) + PITR

- 관리형 서비스로 AZ 내구가 기본 전제(시험 문장에 자주 등장)
- 백업/복구 관점 옵션
  - On-demand backup(수동)
  - PITR(Point-in-time recovery): 시점 복구(요구사항에 “실수 복구/롤백”이 있으면 힌트)

## Exam must-know (포인트 + Why + 대안)

- Key point: “실수로 데이터가 잘못 업데이트/삭제” 힌트가 있으면 DynamoDB PITR이 정답 후보로 올라간다.
- Why: PITR은 특정 시점으로 복구할 수 있는 롤백 메커니즘이며 ‘운영 실수’ 유형에 직접 대응한다.
- Alternative: “규제/장기 보관/감사” 요구가 핵심이면 백업 보관 정책/아카이브(S3 등)까지 포함한 설계를 선택한다.

## TL;DR (한 줄 정리)

- “실수 복구/롤백” 신호가 있으면 DynamoDB는 **PITR**이 정답 후보로 올라간다.

## Back

- `../01-theory.md`
