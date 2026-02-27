# Quiz (Mock Questions) - Day 01

## Q1

**Scenario:** 팀/프로젝트별로 비용을 분리해 보고 싶다. 가장 먼저 고려해야 할 것은?

A. CloudTrail 활성화  
B. 태그 표준화 및(필요 시) 비용 할당 태그 활성화  
C. 모든 인스턴스를 Spot으로 전환  
D. S3 퍼블릭 오픈  

**Answer:** B  
**Explanation:** 차지백/쇼백은 태그(또는 계정 분리)가 출발점이다.  
**Tags:** `domain:4` `services:CostManagement`

## Q2

**Scenario:** 비용을 분석/그룹핑하고 추세를 보고 싶다. 적절한 도구는?

A. Cost Explorer  
B. Budgets  
C. GuardDuty  
D. STS  

**Answer:** A  
**Explanation:** 분석/그룹핑은 Cost Explorer가 직접 매핑된다.  
**Tags:** `domain:4` `services:CostExplorer`

## Q3

**Scenario:** 비용이 임계치를 넘기기 전에 이메일 알림을 받고 싶다. 적절한 도구는?

A. Budgets  
B. Cost Explorer  
C. CloudFront  
D. KMS  

**Answer:** A  
**Explanation:** 임계치 알림/통제는 Budgets가 대표적이다.  
**Tags:** `domain:4` `services:Budgets`

## Q4

**Scenario:** 다음 중 비용 드라이버로 자주 함정이 되는 것은?

A. NAT Gateway 경유 트래픽/시간 비용  
B. IAM 그룹 수  
C. CloudTrail 이벤트 이름  
D. Route 53 레코드 이름  

**Answer:** A  
**Explanation:** NAT는 트래픽/시간에 따라 비용이 급증할 수 있어 시험 함정으로 자주 나온다.  
**Tags:** `domain:4` `services:VPC`

## Q5

**Scenario:** 비용 최적화에 대한 올바른 태도는?

A. 무조건 가장 싼 서비스를 고른다  
B. 요구사항을 유지하며 비용 드라이버를 줄이는 대안을 비교한다  
C. 보안을 낮춰서 비용을 줄인다  
D. 모든 데이터를 Glacier로 옮긴다  

**Answer:** B  
**Explanation:** SAA는 트레이드오프 기반 설계를 묻는다.  
**Tags:** `domain:4` `services:Architecture`

