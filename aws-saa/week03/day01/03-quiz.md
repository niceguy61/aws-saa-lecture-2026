# Quiz (Mock Questions) - Day 01

## Q1

**Scenario:** 지속적으로 높은 CPU 사용률이 요구되는 배치 워크로드다. 성능이 예측 가능해야 한다. 가장 적절한 EC2 선택 방향은?

A. T 계열(t3/t4g)  
B. Compute optimized(C 계열)  
C. S3 Intelligent-Tiering  
D. Route 53 Failover  

**Answer:** B  
**Explanation:** 지속 고CPU/예측 가능성 요구는 burstable이 함정이며 C 계열이 후보가 된다.  
**Tags:** `domain:3` `services:EC2`

## Q2

**Scenario:** T 계열 인스턴스에서 “갑자기 성능이 떨어진다”는 증상이 있다. 가장 관련 있는 개념은?

A. CPU credits 소진  
B. S3 versioning  
C. WAF rate limit  
D. CloudTrail trail  

**Answer:** A  
**Explanation:** burstable은 크레딧 기반이라 지속 부하에서 성능이 떨어질 수 있다.  
**Tags:** `domain:3` `services:EC2`

## Q3

**Scenario:** 성능 문제를 진단할 때 CloudWatch에서 가장 먼저 확인할 지표로 적절한 것은?

A. CPUUtilization(그리고 필요 시 관련 보조 지표)  
B. IAM 사용자 수  
C. Route 53 레코드 수  
D. S3 스토리지 클래스  

**Answer:** A  
**Explanation:** 병목 1차 분류는 CPU/IO/Network 지표 확인이 출발점이다.  
**Tags:** `domain:3` `services:CloudWatch`

## Q4

**Scenario:** 인메모리 캐시/메모리 기반 워크로드에 더 적절한 패밀리 선택 방향은?

A. Memory optimized(R/X 계열)  
B. Compute optimized(C 계열)  
C. Burstable(T 계열)  
D. Storage classes  

**Answer:** A  
**Explanation:** 메모리 신호가 강하면 R/X 계열이 후보가 된다.  
**Tags:** `domain:3` `services:EC2`

## Q5

**Scenario:** 다음 중 “성능 문제 = 무조건 스케일업”이 함정인 이유로 가장 적절한 것은?

A. 병목이 DB/스토리지/네트워크일 수 있다  
B. 스케일업은 항상 무료다  
C. 스케일업은 보안 위반이다  
D. 스케일업은 Route 53 문제다  

**Answer:** A  
**Explanation:** 성능은 병목 지점을 먼저 찾아야 한다.  
**Tags:** `domain:3` `services:Architecture`

