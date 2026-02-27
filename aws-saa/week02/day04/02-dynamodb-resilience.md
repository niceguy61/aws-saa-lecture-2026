# DynamoDB Resilience + PITR (실수 롤백)

## 소개 (이게 뭔가요?)

- DynamoDB는 관리형 NoSQL로 AZ 내구가 기본 전제라는 문장이 자주 나온다.
- “실수로 잘못 업데이트/삭제” 같은 롤백 요구는 PITR이 신호다.

## 고객 사례 (스토리, 600~1000자)

운영 중에 배치가 잘못 돌았다. 특정 파티션 키의 값이 전부 덮어써졌다. 장애는 아니지만 데이터가 망가졌다. 팀은 “몇 시간 전 상태로만 되돌릴 수 있으면 된다”고 한다. 이건 리전 DR이 아니라 ‘실수 복구’다. RDS라면 백업 복원이나 PITR을 떠올릴 수 있는데, DynamoDB에서도 비슷한 요구가 나온다.

이때 DynamoDB PITR(Point-in-time recovery)이 자연스럽다. 특정 시점으로 복구할 수 있는 롤백 메커니즘이라 “운영 실수” 유형에 직접 대응한다. 시험도 “실수로 업데이트/삭제” 같은 문장을 넣어 PITR을 고르게 만든다. 반대로 규제/장기 보관/감사가 핵심이면 백업 보관 정책이나 S3 아카이브 같은 더 큰 설계를 함께 요구할 수 있다. 결국 DynamoDB 문제도 “무슨 종류의 복구인가(실수 vs 재해)”를 먼저 분리하면 정답이 보인다.

그리고 실무적으로는 “복구를 얼마나 자주 해야 하느냐”도 중요하다. 한 번의 실수로 끝나는 사고도 있지만, 반복되는 운영 작업에서 같은 유형의 실수가 다시 발생할 수 있다. 그래서 PITR 같은 ‘기능 스위치’가 있는 서비스는, 요구사항이 맞는 순간 설계가 훨씬 단순해진다.

지금 요구는 “리전 DR”인가요, “실수 롤백”인가요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: 실수 롤백(시점 복구) 요구 대응
- Operations: 복구 절차/근거를 단순화

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Backup%20%26%20restore-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: DynamoDB](https://img.shields.io/badge/Service-DynamoDB-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

## Why This Matters (시험/실무에서 걸리는 지점)

- “실수 복구/롤백” 문장이 보이면 PITR이 바로 후보로 올라간다.

## VAKOG Anchors

- V(Visual): PITR=시점 복구를 한 문장으로 써본다.
- A(Auditory): “실수 롤백=PITR”을 말로 고정한다.
- O(Olfactory, smell test): 실수 복구 요구인데 DR/복제만 고르는 답은 냄새가 난다.
- G(Gustatory, taste test): 문장 하나 보고 PITR 여부를 고른다.

## Core Concepts

- 관리형 서비스로 AZ 내구가 기본 전제(시험 문장에 자주 등장)
- 백업/복구 관점 옵션
  - On-demand backup(수동)
  - PITR(Point-in-time recovery): 시점 복구(요구사항에 “실수 복구/롤백”이 있으면 힌트)

## Deep Dive

## Exam must-know (포인트 + Why + 대안)

- Key point: “실수로 데이터가 잘못 업데이트/삭제” 힌트가 있으면 DynamoDB PITR이 정답 후보로 올라간다.
- Why: PITR은 특정 시점으로 복구할 수 있는 롤백 메커니즘이며 ‘운영 실수’ 유형에 직접 대응한다.
- Alternative: “규제/장기 보관/감사” 요구가 핵심이면 백업 보관 정책/아카이브(S3 등)까지 포함한 설계를 선택한다.

## TL;DR (한 줄 정리)

- “실수 복구/롤백” 신호가 있으면 DynamoDB는 **PITR**이 정답 후보로 올라간다.

## Back

- `./00-theory-index.md`
