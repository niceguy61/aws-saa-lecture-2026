# Quiz (Mock Questions) - Day 04

## Q1

**Scenario:** 관계형 DB에서 “가용성(자동 장애 조치)”이 핵심 요구다. 가장 적절한 선택지는?

A. RDS Read replica  
B. RDS/Aurora Multi-AZ  
C. CloudFront  
D. SQS  

**Answer:** B  
**Explanation:** HA/자동 장애 조치는 Multi-AZ가 대표 정답 후보며 Read replica는 주로 읽기 확장이다.  
**Tags:** `domain:2` `services:RDS,Aurora`

## Q2

**Scenario:** “읽기 트래픽이 많아 성능을 확장”하고 싶다. 관계형 DB에서 후보가 되는 것은?

A. Multi-AZ만 사용  
B. Read replica  
C. KMS grants  
D. WAF  

**Answer:** B  
**Explanation:** 읽기 확장 요구는 read replica가 직접 매핑된다.  
**Tags:** `domain:2` `services:RDS,Aurora`

## Q3

**Scenario:** DynamoDB에서 “실수로 삭제한 데이터를 특정 시점으로 복구”해야 한다. 후보가 되는 기능은?

A. PITR  
B. Route 53 Failover  
C. ALB Target group  
D. IAM permissions boundary  

**Answer:** A  
**Explanation:** 시점 복구 요구는 PITR 힌트다.  
**Tags:** `domain:2` `services:DynamoDB`

## Q4

**Scenario:** Multi-AZ와 Read replica의 차이로 가장 적절한 설명은?

A. 둘 다 읽기 확장만 제공한다  
B. Multi-AZ는 HA/failover, Read replica는 읽기 확장 중심이다  
C. Read replica는 항상 동기 복제다  
D. Multi-AZ는 캐시 서비스다  

**Answer:** B  
**Explanation:** 시험 단골 구분이다.  
**Tags:** `domain:2` `services:RDS,Aurora`

## Q5

**Scenario:** NoSQL(DynamoDB)을 정답 후보로 고려할 신호는?

A. 조인과 복잡한 트랜잭션이 핵심  
B. 키-값/저지연/탄력 확장이 핵심  
C. TLS 인증서 발급 필요  
D. DNS 라우팅 필요  

**Answer:** B  
**Explanation:** 요구사항 기반 선택이 핵심이다.  
**Tags:** `domain:2` `services:DynamoDB`

