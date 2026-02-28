# RDS/Aurora: Multi-AZ vs Read Replica

## 소개 (이게 뭔가요?)

- DB 문제는 “가용성(자동 장애 조치)”과 “읽기 확장”을 분리해서 고른다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - Multi-AZ vs Read Replica](../../assets/scenario_image/w2d4s1.png)

DB가 느려지자 팀은 “읽기를 늘리자”고 했다. 그런데 장애가 한 번 나고 나서 운영팀은 “자동으로 넘어가야 한다”고 요구한다. 둘 다 중요하지만, 같은 기능으로 해결하려 하면 오답이 된다. Read replica는 읽기 성능을 늘리는 도구이지, 자동 장애 조치(HA)의 standby가 아니다. 반대로 Multi-AZ는 자동 failover가 목적이지, 읽기 확장 도구가 아니다.

시험도 이 혼동을 노린다. 문장에 “failover”, “자동 장애 조치”, “가용성”이 있으면 Multi-AZ가 신호다. “read-heavy”, “읽기 성능”, “읽기 트래픽”이 핵심이면 Read replica가 신호다. 결국 먼저 질문해야 한다. “지금 복구해야 하는 건 속도인가, 연속성인가?”

여기서 한 번 더: Read replica는 복제 지연(lag)이 생길 수 있고, 보통 자동 엔드포인트 전환을 ‘HA’처럼 제공하지 않는다. 그래서 “몇 분 다운도 안 된다” 같은 문장에서는 replica 추가만으로는 정답이 되기 어렵다. 반대로 “읽기만 느리다”에서 Multi-AZ만 붙이는 답도 과할 수 있다. 이 미묘한 차이를 요구사항 문장으로 구분하는 게 SAA 포인트다.

지금 요구는 “읽기 성능”인가요, 아니면 “장애 시 자동 전환”인가요?

## Impact 범위 (어디에 영향을 주나?)

- Reliability: Multi-AZ(자동 failover)
- Performance: Read replica(읽기 분산)

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-2-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-2.2%20Database%20resilience-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: RDS](https://img.shields.io/badge/Service-RDS-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

## Why This Matters (시험/실무에서 걸리는 지점)

- “Read replica로 HA”는 대표 함정이다.

## Core Concepts

![RDS Multi-AZ vs Read Replica](../../assets/core/rds-multi-az-vs-read-replica.svg)

| Goal | Best feature | Why | Common trap |
|---|---|---|---|
| HA/자동 장애 조치 | Multi-AZ | failover 중심 | Read replica로 HA 해결하려 함 |
| 읽기 확장 | Read replica | read scaling | Multi-AZ가 읽기 확장이라고 착각 |

```mermaid
flowchart LR
  App[App] --> DBP[Primary]
  DBP -->|sync/ha| DBS[Standby - Multi-AZ]
  DBP -->|async read| RR[Read Replica]
```

## Deep Dive

### “가용성”과 “성능”을 먼저 분리하기

DB 문제는 겉으로는 둘 다 “느리다/불안하다”로 보이지만, 시험에서는 문장이 어느 축을 말하는지 분리하는 게 핵심이다.

- **가용성(HA) 신호**: `자동 failover`, `몇 분 다운도 안 됨`, `AZ 장애에도 계속` 같은 표현
- **성능(읽기 확장) 신호**: `read-heavy`, `읽기 지연`, `리포트/조회가 병목`, `읽기 트래픽 분산` 같은 표현

### RDS/Aurora에서의 실제 차이(시험에 자주 나오는 디테일)

| 항목 | Multi-AZ | Read replica |
|---|---|---|
| 목적 | **자동 장애 조치(HA)** | **읽기 확장(read scaling)** |
| 복제 특성 | (보통) 동기/고가용성 구성 | (대개) 비동기 복제(지연 가능) |
| 애플리케이션 연결 | 장애 시 엔드포인트가 자동 전환 | 읽기 전용 엔드포인트/분산 설계 필요 |
| 대표 함정 | “Multi-AZ면 읽기가 빨라진다” | “RR을 HA standby로 쓴다” |

> Aurora는 “리더/리더 엔드포인트” 같은 구성 요소가 있어 표현이 조금 다르지만, 시험에서 요구를 분해하는 축(HA vs read scaling)은 동일하게 적용되는 경우가 많다.

### Best Practices (언제 이렇게/저렇게)

- “장애 시 자동 전환”이 핵심이면 **Multi-AZ**를 먼저 붙이고, 그 다음에 읽기 병목이 있으면 **Read replica**를 추가해 *목적별로 조합*한다.
- Read replica는 **읽기 전용**이라는 전제가 강하다. “쓰기 트래픽도 분산” 같은 문장이라면 함정일 가능성이 높다.
- “리전 DR/글로벌 읽기” 신호가 강하면 단순 RR/Multi-AZ만으로 끝내지 말고 **다중 리전 옵션(예: Aurora Global Database)** 같은 상위 설계를 떠올린다.

### 핵심 정리 (Deep Dive)

- “failover”는 **Multi-AZ**, “read-heavy”는 **Read replica**로 먼저 매핑한다.
- Read replica는 “느린 읽기”를 풀어주지만, **복제 지연** 때문에 “항상 최신” 요구에는 함정이 될 수 있다.

## Exam must-know (포인트 + Why + 대안)

- Key point: Read replica는 “읽기 확장”이고, HA의 standby로 착각하면 오답으로 빠진다.
- Why: 복제는 보통 비동기이며(지연 가능), 자동 failover/엔드포인트 전환은 Multi-AZ의 역할이다.
- Alternative: “글로벌 읽기/리전 DR” 요구가 강하면 Aurora Global Database 같은 다중 리전 옵션을 함께 검토한다.

## TL;DR (한 줄 정리)

- “failover”면 **Multi-AZ**, “read-heavy”면 **Read replica**다.

## Back

- `./README.md`
