# Quiz (Mock Questions) - Day 04

## Q1

**Scenario:** DynamoDB 성능 이슈가 있는데 트래픽이 특정 파티션 키에 집중된다. 가장 근본적인 접근은?

A. 무조건 DAX 추가  
B. 파티션 키 설계를 개선해 핫 파티션을 완화  
C. CloudFront invalidation  
D. Route 53 weighted  

**Answer:** B  
**Explanation:** 핫 파티션은 키 설계 문제인 경우가 많다. 캐시는 보조 수단일 수 있다.  
**Tags:** `domain:3` `services:DynamoDB`

## Q2

**Scenario:** “다른 조건(status)으로 조회” 요구가 생겼다. DynamoDB에서 정답 후보가 되는 기능은?

A. GSI  
B. NACL  
C. KMS grant  
D. S3 lifecycle  

**Answer:** A  
**Explanation:** 다른 액세스 패턴 추가는 GSI가 대표 선택지다.  
**Tags:** `domain:3` `services:DynamoDB`

## Q3

**Scenario:** Query와 Scan의 차이로 가장 적절한 것은?

A. Query는 전체를 읽고 Scan은 키 기반이다  
B. Query는 키 기반, Scan은 전체 탐색이다  
C. 둘은 동일하다  
D. 둘 다 캐시 기능이다  

**Answer:** B  
**Explanation:** Scan은 비용/성능 함정으로 자주 출제된다.  
**Tags:** `domain:3` `services:DynamoDB`

## Q4

**Scenario:** 반복 읽기 트래픽이 많아 DB 부하와 지연이 커진다. 정답 후보가 되는 아키텍처 패턴은?

A. 캐시 계층 추가(ElastiCache/DAX 등)  
B. CloudTrail 활성화  
C. Route 53 failover  
D. SCP 적용  

**Answer:** A  
**Explanation:** 반복 읽기에 캐시는 대표 성능 패턴이다(일관성 트레이드오프 고려).  
**Tags:** `domain:3` `services:ElastiCache,DAX`

## Q5

**Scenario:** “무조건 캐시”가 오답이 되는 신호로 가장 적절한 것은?

A. 읽기 반복이 매우 많다  
B. 데이터가 개인화/일관성 요구가 매우 강하고 캐시 무효화가 어렵다  
C. 정적 콘텐츠다  
D. 지연시간을 줄이고 싶다  

**Answer:** B  
**Explanation:** 캐시는 트레이드오프(일관성/무효화)가 있어 요구사항에 따라 오답이 될 수 있다.  
**Tags:** `domain:3` `services:Architecture`

