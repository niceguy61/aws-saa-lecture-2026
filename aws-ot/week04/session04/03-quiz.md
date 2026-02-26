# Quiz - Session 04

## Q1

**Scenario:** 30분 이상 걸리는 배치 작업을 실행해야 한다. 가장 적절한 방향은?

A. Lambda 단독으로 실행  
B. Step Functions와 ECS Fargate 또는 Batch로 구성  
C. Route 53 failover  
D. Secrets Manager rotation  

**Answer:** B  
**Explanation:** Lambda는 15 minute 제한이 있어 긴 실행은 다른 컴퓨트로 간다.  

## Q2

**Scenario:** 이벤트 기반 짧은 작업을 빠르게 배포하고 싶다. 운영 부담을 줄이는 선택지는?

A. Lambda  
B. 단일 EC2  
C. 물리 서버  
D. NACL  

**Answer:** A  
**Explanation:** 이벤트 기반 단기 실행은 Lambda가 후보가 된다.  

