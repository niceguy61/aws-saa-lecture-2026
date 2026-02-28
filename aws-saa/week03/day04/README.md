# Day 04 - DB performance + caching (DB 성능 + 캐시: DynamoDB/Aurora/ElastiCache)

![고객 사례 삽화 - DB 성능 진단 순서](../../assets/scenario_image/w3d4s0.png)

## Outcomes

- DB 성능 문제를 “쿼리/인덱스/캐시/모델링” 관점으로 분해한다.
- DynamoDB에서 “파티션 키 설계/핫 파티션”이 성능에 미치는 영향을 설명한다.
- ElastiCache/DAX의 역할을 “읽기 캐시”로 위치시킨다(개념).
- DynamoDB GSI로 “다른 액세스 패턴”을 추가하는 사고 흐름을 설명한다.

## Services In Scope

- DynamoDB (partition key, GSI 개념)
- ElastiCache, DAX (개념)
- Aurora/RDS performance patterns (개념)

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [DynamoDB: 키/Query/GSI가 성능을 결정한다](01-dynamodb.md)
- [ElastiCache: 반복 읽기 핫패스를 캐시로 뺀다](02-elasticache.md)
- [Aurora: 읽기 확장과 DB 성능 패턴](03-aurora.md)

## Core Concepts

- DB 성능 문제는 보통 3단계로 푼다(시험형 프레임)
  1) 캐시로 반복 조회를 줄일 수 있는가(ElastiCache/DAX)
  2) 액세스 패턴이 맞는가(Query vs Scan, 키 설계, 인덱스)
  3) 읽기 확장/리플리카 같은 구조 변경이 필요한가

![캐싱 레이어](../../assets/core/caching-layers.svg)

## Exam Traps (확장)

- DynamoDB 문제를 무조건 DAX로 해결하는 선택지(키 설계/Query/GSI가 근본일 수 있다).
- Query가 가능한데 Scan을 고르는 선택지.
- 캐시를 “모든 문제의 답”으로 고르는 선택지(일관성 요구가 강하면 신중).
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- DynamoDB 지연 문제에서 “무조건 DAX”가 오답이 되는 신호는?
- “다른 조건으로 조회” 요구가 있을 때 GSI가 정답인 신호는?
- 캐시가 정답이 되는 상황과 오답이 되는 상황을 구분할 수 있는가?

## TL;DR (한 줄 정리)

- DB 성능은 **캐시 → 액세스 패턴/인덱스 → 읽기 확장** 순서로 좁히고, 서비스는 그 신호에 맞춰 고른다.
