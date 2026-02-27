# DB 복원력: RDS/Aurora/DynamoDB

## 소개 (이게 뭔가요?)

- DB는 시험에서 “가용성(장애 조치)”과 “성능(읽기 확장)”을 섞어서 묻는다.
- Multi-AZ는 failover, Read replica는 read scaling. 목적을 먼저 고르면 헷갈림이 줄어든다.

## 고객 사례 (스토리)

서비스가 성장하면서 DB가 병목이 됐다. 피크 시간마다 읽기 요청이 폭증하고, 가끔은 DB가 재시작되면서 몇 분씩 먹통이 된다. 개발자는 “읽기 성능을 늘리고 싶다”라고 말하지만, 운영팀은 “장애가 나도 자동으로 살아나야 한다”를 더 크게 외친다. 둘을 한 기능으로 해결하려고 하면 바로 함정에 빠진다.

특히 SLA가 있는 서비스라면 “몇 분 다운”도 치명적이다. 이때는 성능보다 먼저, 장애 시 자동 전환이 가능한지부터 확인해야 한다.

RDS/Aurora에서 Multi-AZ는 ‘장애 조치’가 목적이다. primary에 문제가 생기면 자동으로 standby로 전환되는 흐름이 핵심이다(시험 문장에 failover가 있으면 신호). 반대로 Read replica는 ‘읽기 확장’이다. 읽기 트래픽을 분산하고 성능을 올리지만, 복제는 보통 비동기라 “즉시 자동 전환”을 기대하면 오답이 된다. 그리고 데이터 모델 자체가 다르면 DynamoDB가 답이 되는 문제도 있다. 키-값 기반, 저지연, 관리형 내구가 필요하고, “실수로 업데이트/삭제했다” 같은 요구가 있으면 PITR(시점 복구)이 자연스럽다. 결국 DB는 “무엇을 회복해야 하나(가용성 vs 성능 vs 실수 복구)”를 먼저 분리하는 게 정답이다.

지금 상황에서 더 급한 건, 읽기 속도일까요, 아니면 장애 시 자동 전환일까요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: DB 장애 시 자동 복구/전환(HA) 설계
- Performance: read-heavy 워크로드에서 읽기 확장 선택이 핵심
- Operations: 장애 대응을 수동에서 자동으로 바꾸는 표준 기능들

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Database%20resilience-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: RDS](https://img.shields.io/badge/Service-RDS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Aurora](https://img.shields.io/badge/Service-Aurora-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: DynamoDB](https://img.shields.io/badge/Service-DynamoDB-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 2: Design Resilient Architectures
- Task focus:
  - 2.2 Highly available and/or fault-tolerant architectures

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “failover”면 Multi-AZ, “read-heavy”면 Read replica, “실수 복구/롤백”이면 PITR처럼 문장 신호로 고르는 문제가 많다.

## Core Concepts

- DB 문제는 보통 “가용성”과 “확장”을 분리해서 묻는다
  - HA/자동 장애 조치: Multi-AZ
  - 읽기 확장: Read replica
  - “둘 다 필요”면 둘을 같이 쓴다
- 시험의 핵심은 목적 매칭
  - “failover”가 문장에 있으면 Multi-AZ
  - “read-heavy”가 문장에 있으면 Read replica

![RDS Multi-AZ vs Read Replica](../../assets/core/rds-multi-az-vs-read-replica.svg)

## Service Chapters (서비스별로 읽기)

- [RDS/Aurora: Multi-AZ vs Read Replica (시험 단골)](theory/10-rds-aurora-multi-az-vs-rr.md)
- [DynamoDB Resilience (개념) + PITR](theory/20-dynamodb-resilience.md)

> DB 문제는 “HA vs 읽기 확장 vs 실수 복구”를 분리해서 읽는 순간 정답이 선명해진다.

## Exam Traps

- “Multi-AZ = 읽기 확장” 착각
- 관계형/NoSQL 요구를 구분하지 못하고 아무 DB나 고르는 실수

## TL;DR (한 줄 정리)

- “failover/HA”면 **Multi-AZ**, “read-heavy”면 **Read replica**, “실수 롤백”이면 **DynamoDB PITR**처럼 목적을 먼저 분리한다.
