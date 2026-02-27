# 03-quiz - Week 03 Day 04 (DynamoDB / ElastiCache / Aurora)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

주문 서비스가 성장하면서 “상태별 주문 목록(예: status=SHIPPED)” 같은 조회 요구가 늘었다. 팀은 DynamoDB에서 파티션 키 설계를 단순하게 해두고, 필요한 조건이 생길 때마다 Scan으로 전체를 뒤져 처리했다. 작은 데이터에선 티가 안 났지만 데이터가 커지자 지연과 비용이 폭증하고 throttling도 발생한다.  
이 요구(새 조회 조건을 빠르게/저지연으로 처리)에 가장 자연스러운 해결 방향은?

A. Scan을 더 자주 돌린다(인덱스는 필요 없다)  
B. 새로운 액세스 패턴을 위해 GSI(Global Secondary Index)를 추가한다  
C. CloudFront를 붙여 DynamoDB를 캐시한다(무조건 정답)  
D. Route 53 라우팅 정책을 Latency로 바꾼다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: DynamoDB 성능은 “키/Query 경로”가 핵심이다. 키로 안 나오는 새로운 조회 조건은 GSI로 액세스 패턴을 추가하는 게 정답 패턴이다.
- 소거법
  - A (명확히 틀림): Scan은 데이터가 커질수록 지연/비용이 폭증하는 대표 함정이다.
  - C (근접 오답): 캐시는 반복 읽기엔 유용하지만, 키 설계/조회 경로 문제를 근본 해결하지 못한다.
  - D (명확히 틀림): DNS는 DB 조회 경로를 바꾸지 않는다.
- 한 줄 규칙: “새 조회 조건”이면 Scan이 아니라 **GSI(새 액세스 패턴)**.
- 태그: `pillar:performance-efficiency` `services:DynamoDB` `week:03` `day:04`

</details>

---

## Q2.

문장에 이런 힌트가 있다. “특정 고객만 느리다”, “특정 키에서만 throttling이 난다.” 전체가 느린 게 아니라 특정 파티션 키에 트래픽이 몰리는 듯하다.  
이 신호의 핵심 원인으로 가장 자연스러운 것은?

A. 핫 파티션(키 분산이 깨져 특정 키로 집중)  
B. CloudTrail 로그가 부족  
C. S3 Versioning 미설정  
D. NACL이 stateful이라서 리턴 트래픽이 막힘  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 특정 키/특정 사용자만 느린 패턴은 “분산이 깨진” 신호다. 핫 파티션은 지연/스로틀링으로 이어져 안정적인 처리량(신뢰성)을 무너뜨린다.
- 소거법
  - B (명확히 틀림): 감사 로그와 성능은 축이 다르다.
  - C (명확히 틀림): 객체 실수 복구 기능이다.
  - D (명확히 틀림): NACL은 stateless다(그리고 DynamoDB 핫 파티션과 무관).
- 한 줄 규칙: “특정 키만 느림”이면 **핫 파티션/키 분산**부터 의심한다.
- 태그: `pillar:reliability` `services:DynamoDB` `week:03` `day:04`

</details>

---

## Q3.

홈 화면 추천 목록처럼 “대부분의 사용자가 비슷한 데이터를 반복해서 읽는” API가 폭발한다. DB는 CPU도 괜찮고 스토리지도 버티는데, 읽기 요청이 너무 많아 연결 수가 늘고 지연이 튄다. “몇 분 정도 지연은 허용된다”는 문장이 있다.  
이 요구(반복 읽기 핫패스에서 지연/부하 감소)에 가장 자연스러운 선택은?

A. ElastiCache로 읽기 핫패스를 캐시한다  
B. DynamoDB Scan을 늘려서 해결한다  
C. 모든 데이터를 항상 최신으로 강제하고 캐시는 금지한다  
D. Route 53 Weighted로 트래픽을 나눈다  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 반복 읽기라면 DB 호출 수 자체를 줄이는 게 가장 빠르다. “약간의 지연 허용” 신호는 캐시 적합도를 올린다.
- 소거법
  - B (명확히 틀림): Scan은 느리고 비싸다(그리고 캐시 문제를 해결하지 못한다).
  - C (근접 오답): “항상 최신” 요구가 아니라면 과한 제약이다.
  - D (명확히 틀림): DNS는 DB 읽기 핫패스를 줄이지 못한다.
- 한 줄 규칙: “반복 읽기/핫 키 + 약간의 지연 허용”이면 **ElastiCache**.
- 태그: `pillar:performance-efficiency` `services:ElastiCache` `week:03` `day:04`

</details>

---

## Q4.

관계형 기능(조인/트랜잭션)이 필요해서 MySQL 계열 DB를 유지해야 한다. 그런데 트래픽이 늘자 “읽기 지연”이 병목이다. 문장 힌트는 “읽기가 많다”, “리포트/조회가 병목이다”, “읽기 확장이 필요하다”다.  
이 요구에 가장 자연스러운 해결 방향은?

A. Aurora/RDS Read replica(읽기 확장)로 읽기 트래픽을 분산한다  
B. 모든 읽기 문제는 ElastiCache로만 해결한다(항상 정답)  
C. Multi-AZ만 붙이면 읽기 성능이 자동으로 늘어난다  
D. DynamoDB로 무조건 전환한다(관계형 요구 무시)  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 관계형을 유지하면서 읽기 병목을 풀려면 read replica/읽기 엔드포인트로 읽기 확장을 하는 게 대표 패턴이다.
- 소거법
  - B (근접 오답): 캐시는 효과가 크지만, 최신성/무효화/데이터 특성에 따라 정답이 갈린다(“항상”은 함정).
  - C (근접 오답): Multi-AZ는 HA(failover) 목적이지 read scaling 도구가 아니다.
  - D (명확히 틀림): 요구사항(관계형 기능)을 무시하는 건 오답이다.
- 한 줄 규칙: “관계형 + 읽기 많음”이면 **Read replica/읽기 분산**이 기본 후보.
- 태그: `pillar:performance-efficiency` `services:Aurora,RDS` `week:03` `day:04`

</details>

---

## Q5. (복수정답: 2개)

다음 중 사실에 맞는 설명 2개를 고르시오.

A. DynamoDB에서 Query는 키 기반 빠른 경로이고, Scan은 전체 탐색이라 데이터가 커질수록 느리고 비싸진다  
B. ElastiCache는 반복 읽기 핫패스에서 DB 호출 수를 줄여 지연을 낮출 수 있다(단, 최신성/무효화 트레이드오프)  
C. GSI는 “캐시 무효화 정책”을 의미한다  
D. Read replica는 자동 failover(HA)용 standby이므로 Multi-AZ가 불필요하다  
E. NACL은 stateful이라 리턴 트래픽을 자동 허용한다  

<details>
<summary>정답/해설</summary>

- 정답: A, B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 소거는 “핵심 규칙”을 정확히 아는 것에서 시작한다(Query/Scan/GSI, 캐시의 트레이드오프).
- 소거법
  - C (명확히 틀림): GSI는 새로운 액세스 패턴(인덱스)이다.
  - D (근접 오답): read replica와 HA(failover)를 혼동한 함정이다.
  - E (명확히 틀림): NACL은 stateless다.
- 한 줄 규칙: DynamoDB는 **키/Query/GSI**, 캐시는 **반복 읽기 + 트레이드오프**로 판단한다.
- 태그: `pillar:operational-excellence` `services:DynamoDB,ElastiCache,Aurora` `week:03` `day:04`

</details>

---

## TL;DR (오늘의 규칙)

- DynamoDB는 **Query(키) vs Scan(전체)**를 먼저 가르고, 새 조건은 **GSI**로 푼다.  
- 반복 읽기 핫패스는 **ElastiCache**, 관계형 읽기 병목은 **Read replica**가 기본 후보.
