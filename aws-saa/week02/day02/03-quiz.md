# Quiz (Mock Questions) - Day 02

## Q1

**Scenario:** HTTP path 기반 라우팅이 필요하다. 가장 적절한 로드밸런서는?

A. NLB  
B. ALB  
C. Gateway Load Balancer  
D. Route 53만 사용  

**Answer:** B  
**Explanation:** path/host 기반 라우팅은 ALB의 대표 기능이다.  
**Tags:** `domain:2` `services:ELB`

## Q2

**Scenario:** TCP 기반 초고성능 트래픽을 처리해야 한다. 후보가 되는 로드밸런서는?

A. ALB  
B. NLB  
C. CloudFront  
D. WAF  

**Answer:** B  
**Explanation:** L4 요구(프로토콜/성능)면 NLB가 후보가 된다.  
**Tags:** `domain:2` `services:ELB`

## Q3

**Scenario:** Auto Scaling이 제공하는 가치로 가장 적절한 것은?

A. 암호화 키 관리  
B. 수평 확장 + 헬스체크 기반 자가 치유  
C. DNS 질의 응답  
D. 취약점 스캔  

**Answer:** B  
**Explanation:** ASG는 확장과 복구를 함께 다룬다.  
**Tags:** `domain:2` `services:AutoScaling`

## Q4

**Scenario:** Multi-AZ 구성이 가용성에 좋은 이유는?

A. 더 큰 인스턴스 1대라서  
B. 장애 영역(AZ)을 분리해 단일 장애 영향을 줄여서  
C. 캐시가 자동으로 생겨서  
D. IAM 권한이 자동으로 부여돼서  

**Answer:** B  
**Explanation:** AZ 분산은 장애 격리의 기본이다.  
**Tags:** `domain:2` `services:HA`

## Q5

**Scenario:** 다음 중 ALB와 함께 안전한 인스턴스 접근 제어로 더 적절한 것은?

A. EC2 SG를 0.0.0.0/0에 오픈  
B. EC2 SG는 ALB SG에서만 80 허용  
C. NACL을 모든 포트 허용  
D. S3 버킷 퍼블릭 오픈  

**Answer:** B  
**Explanation:** 백엔드는 ALB에서만 접근하도록 제한하는 게 일반적으로 더 안전하다.  
**Tags:** `domain:2` `services:VPC,ELB`

## Q6

**Scenario:** 타겟 그룹 헬스체크가 실패하면 일반적으로 어떤 일이 일어나는가?

A. Route 53 레코드가 삭제된다  
B. unhealthy 타겟이 트래픽에서 제외된다(그리고 ASG가 교체할 수 있다)  
C. KMS 키가 회전된다  
D. SQS DLQ로 이동한다  

**Answer:** B  
**Explanation:** 헬스체크는 트래픽 제외/교체의 트리거로 동작한다.  
**Tags:** `domain:2` `services:ELB,AutoScaling`

