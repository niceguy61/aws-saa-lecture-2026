# Aurora: 읽기 확장과 DB 성능 패턴

## 소개 (이게 뭔가요?)

- Aurora는 RDS의 고성능/고가용성 관계형 DB 옵션으로, 시험에서는 “읽기 확장/리플리카/엔드포인트” 같은 신호로 자주 등장한다.

## 고객 사례 (스토리, 600~1000자)

서비스가 커지면서 “관계형이 필요한 기능”이 많아진다. 조인/트랜잭션/복잡한 리포트 쿼리 때문에 MySQL 계열 DB를 쓰고 있는데, 트래픽이 늘자 읽기 지연이 올라간다. 팀은 무작정 인스턴스를 키우거나, DB를 다른 종류로 바꾸려 한다. 그런데 요구 문장을 보면 힌트는 더 단순하다. “읽기가 많다”, “리포트/조회가 병목이다”, “읽기 확장이 필요하다” 같은 신호다.

이럴 때 Aurora/RDS의 대표 패턴은 “읽기 확장”이다. Read replica를 두거나(Aurora는 read endpoint 같은 개념으로 묶어서 노출), 읽기 트래픽을 분산한다. 반대로 쓰기 병목/락 경합/쿼리 자체가 비효율이면, 단순히 리플리카만 늘려서는 해결이 안 되고 인덱스/쿼리 튜닝, 커넥션 풀링 같은 조치가 필요하다. 시험에서도 이런 힌트를 문장으로 준다(“connection exhaustion”, “slow query”, “index missing” 같은 신호).

또 실무에선 “리플리카를 늘리면 끝”이 아니라, 애플리케이션이 읽기 트래픽을 어디로 보내는지도 중요하다. 시험에서도 “read endpoint” 같은 표현으로 ‘읽기 분산’이 의도됐음을 힌트로 주는 경우가 있다. 이 신호를 잡으면, 단순 스펙 업보다 ‘구조적 확장’ 답이 더 자연스럽다.

정리하면, Aurora는 “그냥 빠른 DB”가 아니라 “관계형을 유지하면서 읽기 확장/운영 패턴으로 성능을 푸는 선택지”다. 지금 시나리오의 병목은 읽기인가요, 쓰기/쿼리인가요?

## Impact 범위 (어디에 영향을 주나?)

- Performance: 읽기 확장/쿼리 튜닝이 지연을 좌우한다.
- Reliability: 관리형 HA/리플리카 패턴이 설계 선택지로 연결된다.
- Cost: 리플리카/상위 인스턴스는 비용이 크게 늘 수 있다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-3-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-3.3%20Database%20solutions-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Aurora](https://img.shields.io/badge/Service-Aurora-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: RDS](https://img.shields.io/badge/Service-RDS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 3: Design High-Performing Architectures
- Objectives: 관계형 DB에서 읽기 확장/성능 튜닝 신호를 해석할 수 있는지

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “읽기 확장 vs 캐시 vs NoSQL 전환” 비교 문제에서 Aurora가 자주 후보로 올라간다.

## VAKOG Anchors

- V(Visual): “쓰기=1, 읽기=여러 개로 분산”을 그림으로 떠올린다.
- A(Auditory): “읽기 많음=리플리카/엔드포인트”를 말로 고정한다.
- O(Olfactory, smell test): 읽기 문제인데 쿼리/인덱스 힌트를 무시하는 답은 냄새가 난다.
- G(Gustatory, taste test): 문장 1개로 “읽기 확장” 신호를 잡는다.

## Core Concepts

- 읽기 확장: Read replica(또는 Aurora의 read endpoint 개념)
- 시험 힌트로 등장하는 운영 포인트(서비스 선택 문제에 같이 섞임)
  - 연결 수/커넥션 풀링
  - 인덱스/쿼리 튜닝

## Exam Traps (5-8)

- 읽기 확장 요구인데 “무조건 캐시만” 고르는 선택지(요구/일관성/패턴에 따라 다름)
- 쿼리/인덱스 힌트가 있는데 “리플리카만 늘리면 된다”로 끝내는 선택지

## Taste Test (1~3분)

- “읽기가 매우 많고, 관계형 기능(조인/트랜잭션)이 필요하다” → 어떤 패턴이 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- 관계형 DB에서 “읽기 확장” 신호가 보이면 **Aurora/RDS Read replica(리드 엔드포인트)**가 대표 후보가 된다.

## Back

- `./00-theory-index.md`
