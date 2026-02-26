# Quiz (Mock Questions) - Day 03

## Q1

**Scenario:** 장기 보관 데이터가 많고 자동으로 저렴한 스토리지로 전환하고 싶다. 정답 후보는?

A. Lifecycle policy  
B. WAF  
C. STS AssumeRole  
D. CloudTrail Event history  

**Answer:** A  
**Explanation:** lifecycle 전환/만료는 비용 최적화 기본 패턴이다.  
**Tags:** `domain:4` `services:S3`

## Q2

**Scenario:** 액세스 패턴이 예측하기 어렵고 자동 최적화가 필요하다. 정답 후보는?

A. Intelligent-Tiering  
B. Standard 고정  
C. Glacier Deep Archive 고정  
D. EBS io2  

**Answer:** A  
**Explanation:** “예측 어려움 + 자동”은 Intelligent-Tiering 힌트다.  
**Tags:** `domain:4` `services:S3`

## Q3

**Scenario:** “모든 데이터를 Glacier로 옮기자”는 제안이 오답이 될 수 있는 이유는?

A. Glacier는 암호화를 지원하지 않는다  
B. 복구 시간/복구 비용 트레이드오프를 무시할 수 있다  
C. Glacier는 DNS 서비스다  
D. Glacier는 캐시 서비스다  

**Answer:** B  
**Explanation:** Glacier 계열은 retrieval 특성이 트레이드오프다.  
**Tags:** `domain:4` `services:S3`

## Q4

**Scenario:** prefix 기반 lifecycle을 쓰는 이유로 가장 적절한 것은?

A. 모든 데이터에 동일 정책을 강제하기 위해  
B. 데이터 성격별로 다른 보관/전환 정책을 적용하기 위해  
C. IAM 권한을 대체하기 위해  
D. Route 53 장애 조치를 위해  

**Answer:** B  
**Explanation:** 데이터 특성 분리는 비용/요구사항 트레이드오프를 반영한다.  
**Tags:** `domain:4` `services:S3`

