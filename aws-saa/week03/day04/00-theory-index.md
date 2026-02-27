# Day 04 - Theory Index (DB 성능 + 캐시: DynamoDB/Aurora/ElastiCache)

> 이 문서는 Day 이론 “인덱스”다. 상세 이론은 Day 폴더 바로 아래 `01-*.md` 서비스별 문서로 분리한다.

## 소개 (이게 뭔가요?)

- Day 04는 DB 성능 문제를 “서비스 선택”으로 바로 점프하지 않고, **캐시 → 액세스 패턴/인덱스 → 읽기 확장** 순서로 진단하는 흐름을 만든다.
- DynamoDB(키/인덱스/Query vs Scan), Aurora(읽기 확장/리드 엔드포인트), ElastiCache(반복 읽기 핫패스) 3개가 핵심이다.

## 고객 사례 (스토리)

서비스가 커지자 DB가 병목이 된다. 증상은 단순하다. “읽기 API가 느리다.” 그런데 팀이 DB를 더 크게 올리거나 리플리카를 늘려도 체감이 크게 좋아지지 않는다. 조회 패턴은 계속 반복되고(같은 상품/프로필/설정 값을 여러 번 읽는다), 트래픽 스파이크 때마다 DB 연결 수가 폭증한다. 운영팀은 “일단 캐시를 붙이면 되지 않나?”라고 하지만, 개발팀은 “최신 값이 바로 반영돼야 한다”는 요구가 있어 캐시가 불안하다.

이때 시험/실무 둘 다 같은 순서로 생각하면 깔끔해진다. 1) 반복 읽기라면 캐시(ElastiCache 또는 DynamoDB 전용 캐시인 DAX)로 DB 호출 자체를 줄일 수 있는가? 2) DynamoDB라면 Query가 가능한 구조인지(키 설계), Scan으로 전체를 읽고 있진 않은지, 새로운 액세스 패턴이 필요하면 GSI로 풀 수 있는가? 3) Aurora/RDS라면 읽기 확장(Read replica/리드 엔드포인트), 쿼리/인덱스/커넥션 풀링 힌트가 있는가?

시험은 이 셋을 섞어서 “캐시=무조건 정답”처럼 보이게 만들기도 하고, DynamoDB에서 Scan을 슬쩍 끼워 넣어 비용 함정을 만들기도 한다. 그래서 “어디가 병목인가”를 먼저 고정하는 게 중요하다.

즉, DB 성능 문제는 “서비스 하나 고르기”가 아니라 “핫패스의 레이어를 바꾸는 것”이다. 지금 문장에선 캐시/인덱스/읽기 확장 중 무엇이 가장 강한 신호인가요?

## Impact 범위 (어디에 영향을 주나?)

- Performance: 핫패스(반복 읽기) 최적화가 체감 성능을 좌우한다.
- Cost: Scan/불필요한 DB 확장/캐시 남발은 비용을 키운다.
- Operations: 캐시 무효화/일관성 정책이 운영 리스크가 된다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-3-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-3.3%20Database%20solutions-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: DynamoDB](https://img.shields.io/badge/Service-DynamoDB-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Aurora](https://img.shields.io/badge/Service-Aurora-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: ElastiCache](https://img.shields.io/badge/Service-ElastiCache-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 3: Design High-Performing Architectures
- Task focus:
  - 3.3 Determine high-performing database solutions

</details>

## Core Concepts

- DB 성능 문제는 보통 3단계로 푼다(시험형 프레임)
  1) 캐시로 반복 조회를 줄일 수 있는가(ElastiCache/DAX)
  2) 액세스 패턴이 맞는가(Query vs Scan, 키 설계, 인덱스)
  3) 읽기 확장/리플리카 같은 구조 변경이 필요한가

![캐싱 레이어](../../assets/core/caching-layers.svg)

## Service Theories (서비스별로 읽기)

- [DynamoDB: 키/Query/GSI가 성능을 결정한다](01-dynamodb.md)
- [ElastiCache: 반복 읽기 핫패스를 캐시로 뺀다](02-elasticache.md)
- [Aurora: 읽기 확장과 DB 성능 패턴](03-aurora.md)

## Exam Traps

- DynamoDB 문제를 무조건 DAX로 해결하는 선택지(키 설계/Query/GSI가 근본일 수 있다).
- Query가 가능한데 Scan을 고르는 선택지.
- 캐시를 “모든 문제의 답”으로 고르는 선택지(일관성 요구가 강하면 신중).

## TL;DR (한 줄 정리)

- DB 성능은 **캐시 → 액세스 패턴/인덱스 → 읽기 확장** 순서로 좁히고, 서비스는 그 신호에 맞춰 고른다.
