# Case Quiz (Domain 4) - Day 05

## Q1

**Scenario:** 1년 이상 꾸준히 사용하는 워크로드의 EC2 비용을 줄이려 한다. 가장 일반적인 선택지는?

A. On-Demand만 유지  
B. Savings Plans 또는 Reserved Instances 고려  
C. 모든 인스턴스를 Spot으로 전환  
D. S3 버킷 퍼블릭 오픈  

**Answer:** B  
**Explanation:** 예측 가능한 장기 사용은 SP/RI가 대표적인 비용 최적화 수단이다.  
**Tags:** `domain:4` `services:EC2`

## Q2

**Scenario:** 배치 처리 워크로드로 중단 허용이 가능하다. 비용을 크게 줄이려면?

A. Spot 인스턴스 고려  
B. 더 큰 On-Demand 1대  
C. NAT Gateway 추가  
D. WAF 추가  

**Answer:** A  
**Explanation:** 중단 허용 배치는 Spot이 시험에서 자주 정답으로 나온다.  
**Tags:** `domain:4` `services:EC2,Spot`

## Q3

**Scenario:** S3에 장기 보관 데이터가 많다. 자동으로 저렴한 스토리지로 전환하고 싶다.

A. CloudTrail 활성화  
B. Lifecycle policy 구성  
C. STS AssumeRole  
D. Security group 수정  

**Answer:** B  
**Explanation:** lifecycle 전환은 비용 최적화의 기본 패턴이다.  
**Tags:** `domain:4` `services:S3`

## Q4

**Scenario:** 접근 패턴이 예측하기 어렵고, “자동으로” 최적화를 하고 싶다.

A. Standard 고정  
B. Intelligent-Tiering 고려  
C. Glacier Deep Archive 고정  
D. EBS io2로 이동  

**Answer:** B  
**Explanation:** Intelligent-Tiering은 접근 패턴이 불명확할 때 자동 계층화를 제공한다.  
**Tags:** `domain:4` `services:S3`

## Q5

**Scenario:** 프라이빗 서브넷의 워크로드가 S3에 자주 접근한다. NAT 비용을 줄이려면?

A. NAT Gateway를 2개로 늘린다  
B. S3 Gateway Endpoint를 사용한다  
C. CloudTrail을 끈다  
D. ACM 인증서를 만든다  

**Answer:** B  
**Explanation:** S3 Gateway endpoint는 NAT 경유 없이 프라이빗 연결로 비용을 줄일 수 있다.  
**Tags:** `domain:4` `services:VPC,S3`

## Q6

**Scenario:** DynamoDB에서 트래픽이 일정하지 않고 예측이 어렵다. 운영 오버헤드를 줄이면서 비용을 관리하고 싶다.

A. Provisioned만 사용  
B. On-demand 고려  
C. 모든 트래픽을 RDS로 이동  
D. CloudFront만 사용  

**Answer:** B  
**Explanation:** 변동이 큰 경우 on-demand가 운영 부담을 줄이고 합리적일 수 있다(요구사항 기반).  
**Tags:** `domain:4` `services:DynamoDB`

## Q7

**Scenario:** 다음 중 “숨은 비용 드라이버”로 자주 출제되는 것은?

A. VPC NAT Gateway 데이터 처리/시간 기반 비용  
B. IAM 그룹 수  
C. CloudTrail 이벤트 이름  
D. Route 53 레코드 이름  

**Answer:** A  
**Explanation:** NAT는 트래픽이 늘면 비용이 급증할 수 있어 시험에서 자주 함정으로 나온다.  
**Tags:** `domain:4` `services:VPC`

## Q8

**Scenario:** “요구사항을 유지하면서 비용을 줄이는 설계”로 가장 적절한 것은?

A. 가용성을 낮춰 단일 AZ로 변경  
B. 비용 드라이버(전송/스토리지/컴퓨트)를 찾아 대안을 비교해 선택  
C. 루트 사용자 공유로 운영 단순화  
D. 모든 데이터를 Standard에 유지  

**Answer:** B  
**Explanation:** 시험은 트레이드오프를 기반으로 비용 최적화를 묻는다.  
**Tags:** `domain:4` `services:CostOptimization`

## Q9

**Scenario:** S3 Glacier 계열로 전환할 때 반드시 고려해야 하는 것은?

A. 복구 시간/요청/복구 비용  
B. IAM 그룹 이름  
C. WAF 규칙  
D. CloudTrail 데이터 이벤트  

**Answer:** A  
**Explanation:** Glacier는 retrieval 특성이 트레이드오프다.  
**Tags:** `domain:4` `services:S3`

## Q10

**Scenario:** right sizing의 핵심은?

A. 항상 가장 큰 인스턴스를 사용  
B. 요구사항에 맞는 최소 사양으로 조정하고 오토스케일을 활용  
C. 모든 리소스를 멈춤  
D. CloudFront 캐시 키를 늘림  

**Answer:** B  
**Explanation:** 요구사항 대비 적정 사양 + 자동 확장이 비용/성능 균형을 만든다.  
**Tags:** `domain:4` `services:EC2,AutoScaling`

## Q11

**Scenario:** 다음 중 비용 가시성 확보에 가장 직접적인 도구 조합은?

A. Cost Explorer/Budgets  
B. GuardDuty/Inspector  
C. CloudTrail/Config  
D. WAF/Shield  

**Answer:** A  
**Explanation:** 비용 최적화의 출발은 가시성이다(권한 필요).  
**Tags:** `domain:4` `services:CostExplorer,Budgets`

## Q12

**Scenario:** 저장 비용 최적화에서 prefix 기반 lifecycle을 쓰는 이유로 가장 적절한 것은?

A. 모든 데이터를 동일 정책으로 처리하기 위해  
B. 워크로드/데이터 중요도에 따라 다른 전환/만료 정책을 적용하기 위해  
C. IAM 권한을 대체하기 위해  
D. CloudTrail을 대체하기 위해  

**Answer:** B  
**Explanation:** 데이터 특성별 정책 분리가 비용/요구사항 트레이드오프를 잘 반영한다.  
**Tags:** `domain:4` `services:S3`

