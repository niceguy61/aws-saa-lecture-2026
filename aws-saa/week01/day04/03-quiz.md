# Quiz (Mock Questions) - Day 04

## Q1

**Scenario:** Security Group과 NACL의 차이를 묻는다. 올바른 설명은?

A. 둘 다 무상태(stateless)다  
B. Security Group은 상태 저장(stateful)이고 NACL은 무상태(stateless)다  
C. NACL은 인스턴스에 직접 붙는다  
D. Security Group은 Deny 규칙을 지원한다  

**Answer:** B  
**Explanation:** 시험형 핵심 구분이다. SG는 stateful(allow), NACL은 stateless(allow/deny).  
**Tags:** `domain:1` `services:VPC`

## Q2

**Scenario:** 프라이빗 서브넷의 워크로드가 S3에 자주 접근한다. 보안과 비용을 개선하려면 가장 적절한 선택지는?

A. NAT Gateway만 사용  
B. S3 Gateway endpoint 사용  
C. S3를 퍼블릭으로 오픈  
D. Security Group에서 S3로 인바운드 허용  

**Answer:** B  
**Explanation:** S3 Gateway endpoint는 사설 경로로 연결해 NAT 의존을 줄이는 대표 정답 후보다.  
**Tags:** `domain:1` `services:VPC,S3`

## Q3

**Scenario:** 다음 중 Gateway endpoint가 대표적으로 지원하는 서비스는?

A. S3  
B. CloudWatch Logs  
C. Secrets Manager  
D. STS  

**Answer:** A  
**Explanation:** 시험에서는 S3/DynamoDB가 Gateway endpoint의 대표 예시로 등장한다.  
**Tags:** `domain:1` `services:VPC`

## Q4

**Scenario:** Interface endpoint(PrivateLink)의 일반적인 형태(개념)로 가장 적절한 것은?

A. 라우팅 테이블에만 경로가 추가된다  
B. VPC 안에 ENI 기반 엔드포인트가 생성된다  
C. S3 버킷이 자동으로 생성된다  
D. Route 53만 변경된다  

**Answer:** B  
**Explanation:** Interface endpoint는 ENI 형태로 VPC 내 엔드포인트가 생긴다는 개념이 빈출이다.  
**Tags:** `domain:1` `services:VPC,PrivateLink`

## Q5

**Scenario:** “S3 접근을 보안 그룹으로 제한하자”는 제안에 대한 올바른 반응은?

A. 맞다. S3는 인스턴스이므로 SG로 제어한다  
B. 틀리다. S3는 SG 대상이 아니며 bucket policy/endpoint policy 등을 고려한다  
C. 맞다. NACL만 설정하면 된다  
D. 틀리다. Route 53로 해결한다  

**Answer:** B  
**Explanation:** S3는 SG 대상이 아니고 정책/엔드포인트 관점으로 풀어야 한다.  
**Tags:** `domain:1` `services:S3,VPC,IAM`

## Q6

**Scenario:** NACL에서 흔히 발생하는 실수는?

A. 리턴 트래픽을 자동으로 허용한다고 가정  
B. Deny 규칙이 없다고 가정  
C. 서브넷에 적용된다는 사실을 가정  
D. 상태 저장이라고 가정하지 않음  

**Answer:** A  
**Explanation:** NACL은 무상태라 양방향(리턴 트래픽) 규칙이 필요하다.  
**Tags:** `domain:1` `services:VPC`

## Q7

**Scenario:** “사설 경로로 AWS 서비스 접근” 요구가 있을 때 endpoint가 자주 정답이 되는 이유는?

A. 캐시 기능 제공  
B. 인터넷 경유를 피하고 NAT 의존/비용을 줄일 수 있다  
C. 자동으로 IAM 권한을 부여한다  
D. 데이터를 Glacier로 전환한다  

**Answer:** B  
**Explanation:** 보안(사설) + 비용(NAT) 힌트는 endpoint 정답 확률을 올린다.  
**Tags:** `domain:1` `services:VPC`

## Q8

**Scenario:** Endpoint policy의 역할(개념)로 가장 적절한 것은?

A. 엔드포인트를 통해 허용되는 요청을 추가로 제한  
B. S3 버킷 이름을 바꿈  
C. CloudTrail 로그를 저장  
D. VPC CIDR을 변경  

**Answer:** A  
**Explanation:** endpoint policy는 “엔드포인트 경유 요청의 추가 제약”으로 출제된다.  
**Tags:** `domain:1` `services:VPC`

