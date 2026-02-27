# Quiz (Mock Questions) - Day 02

## Q1

**Scenario:** 중단 허용 배치 워크로드다. 비용을 크게 줄이고 싶다. 정답 후보는?

A. Spot  
B. Reserved Instances  
C. S3 Glacier  
D. Route 53 Failover  

**Answer:** A  
**Explanation:** 중단 허용은 Spot의 대표 신호다.  
**Tags:** `domain:4` `services:EC2,Spot`

## Q2

**Scenario:** 1~3년 동안 사용량이 예측 가능한 steady-state 워크로드다. 비용 최적화 정답 후보는?

A. Savings Plans 또는 Reserved Instances  
B. On-Demand만 유지  
C. SQS DLQ  
D. CloudTrail  

**Answer:** A  
**Explanation:** 예측 가능/steady state는 RI/SP 힌트다.  
**Tags:** `domain:4` `services:EC2`

## Q3

**Scenario:** right sizing에 대한 올바른 설명은?

A. 항상 가장 큰 인스턴스를 선택  
B. 측정(지표/부하) 기반으로 요구사항에 맞는 적정 사양을 선택  
C. 보안을 낮춘다  
D. NAT Gateway를 늘린다  

**Answer:** B  
**Explanation:** 시험은 측정 기반 의사결정을 선호한다.  
**Tags:** `domain:4` `services:EC2`

## Q4

**Scenario:** 비피크 시간에 트래픽이 거의 없다. 비용을 줄이려면 어떤 패턴이 적절한가?

A. Scheduled scaling으로 야간 0  
B. 인스턴스를 단일 AZ로 변경  
C. 버킷 퍼블릭 오픈  
D. WAF 룰 추가  

**Answer:** A  
**Explanation:** 시간 기반 scaling은 비피크 비용 절감에 직접적이다.  
**Tags:** `domain:4` `services:AutoScaling`

