# S3 Versioning (실수 복구의 기본기)

## 소개 (이게 뭔가요?)

- S3 Versioning은 객체의 이전 버전을 보존해서 “삭제/덮어쓰기 실수”를 되돌릴 수 있게 한다.

## 고객 사례 (스토리, 600~1000자)

배치 작업이 오래된 파일을 정리하다가, 필요한 객체까지 같이 삭제했다. 팀은 “S3에 있으니 안전하다”고 생각했지만, 안전은 ‘내구성’이지 ‘실수 복구’가 아니다. 삭제는 너무 쉽고, 한 번 누르면 끝이다. 복구를 위해 백업 ZIP을 찾고, 복원 작업을 하느라 반나절이 날아간다. 요구사항 문장도 똑같다. “accidental deletion/overwrite를 막아야 한다”는 문장이 등장한다.

이때 S3 Versioning은 가장 직접적인 선택지다. delete는 실제 삭제가 아니라 delete marker가 붙는 모델이라, 이전 버전을 되돌릴 수 있다. 물론 더 강한 요구(규제/WORM/변경 불가)가 있으면 Object Lock 같은 옵션으로 넘어가야 하지만, ‘실수 복구’라는 축에서는 Versioning이 기본기다.

운영 관점에서 좋은 점은 “복구가 가능한 상태”를 기본값으로 만든다는 것이다. 사람이 실수할 수 있다는 전제를 깔고, 실수의 비용(복구 시간/데이터 손실)을 줄인다. 그래서 문제 문장에 ‘accidental’ 같은 단어가 보이면, 복제/DR 같은 큰 얘기보다 Versioning부터 떠올리는 게 맞다.

지금 문제는 ‘재해(리전 장애)’인가요, 아니면 ‘실수(삭제/덮어쓰기)’인가요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: 운영 실수 복구(롤백) 메커니즘
- Operations: 복구 절차를 단순화한다

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Backup%20%26%20DR-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: S3](https://img.shields.io/badge/Service-S3-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 2: Design Resilient Architectures
- Task focus: “실수 복구/삭제 복구” 요구에서 Versioning 선택

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “accidental deletion/overwrite”는 Versioning 신호다.

## VAKOG Anchors

- V(Visual): delete marker 모델을 시퀀스로 본다.
- A(Auditory): “실수 복구=Versioning”을 말로 고정한다.
- O(Olfactory, smell test): 실수 복구 요구인데 replication만 고르는 답은 냄새가 난다.
- G(Gustatory, taste test): 문장 하나 보고 Versioning을 고른다.

## Core Concepts

- What it gives you
  - 덮어쓰기/삭제가 발생해도 이전 버전을 되돌릴 수 있음
- 시험형 힌트
  - “accidental deletion/overwrite”가 문장에 있으면 versioning이 정답 후보

## Deep Dive

## Exam must-know (포인트 + Why + 대안)

- Key point: “실수로 삭제/덮어쓰기”를 복구해야 한다면 S3 Versioning이 가장 직접적인 해법이다.
- Why: delete는 실제 삭제가 아니라 delete marker가 붙는 모델이라, 이전 버전을 복구할 수 있다.
- Alternative: 더 강한 요구(감사/승인/장기 보관/immutability)가 있으면 Object Lock/보관 정책까지 같이 검토한다.

```mermaid
sequenceDiagram
  participant U as User
  participant S3 as S3 - versioning on
  U->>S3: PUT object v1
  U->>S3: PUT object v2 overwrite
  U->>S3: DELETE object
  Note over S3: delete marker
  U->>S3: Restore previous version
```

## Quick Comparison Table

| Need | Best choice |
|---|---|
| 실수 복구(삭제/덮어쓰기) | S3 Versioning |

## Exam Traps (5-8)

- “실수 복구”인데 versioning 언급이 없는 답안

## Taste Test (1~3분)

- “실수로 객체가 삭제됐다” → 무엇이 1순위?

## TL;DR (한 줄 정리)

- “실수로 삭제/덮어쓰기 복구”는 S3 Versioning이 기본 정답 후보다.

## Back

- `./00-theory-index.md`
