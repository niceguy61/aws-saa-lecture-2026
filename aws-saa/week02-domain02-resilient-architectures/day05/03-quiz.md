# Case Quiz (Domain 2) - Day 05

## Q1

**Scenario:** 주문 처리 시스템에서 트래픽 스파이크가 발생한다. 시스템은 요청을 잃지 않아야 하고, 처리 컴포넌트를 느슨하게 결합하고 싶다.

A. SNS만 사용한다  
B. SQS를 사용해 버퍼링하고 워커가 폴링해서 처리한다  
C. 모든 요청을 단일 EC2에 동기 처리한다  
D. Route 53만 설정한다  

**Answer:** B  
**Explanation:** 내구 큐 + 비동기 워커는 스파이크 흡수/느슨한 결합의 전형이다.  
**Tags:** `domain:2` `services:SQS`

## Q2

**Scenario:** 한 이벤트를 여러 다운스트림 시스템에 전달해야 한다(팬아웃). 가장 표준적인 조합은?

A. SNS + 여러 SQS 구독  
B. 단일 SQS만 사용  
C. 단일 Lambda만 사용  
D. 단일 RDS만 사용  

**Answer:** A  
**Explanation:** SNS는 팬아웃, SQS는 각 소비자별 내구/재시도를 제공한다.  
**Tags:** `domain:2` `services:SNS,SQS`

## Q3

**Scenario:** 워커가 메시지를 반복 실패한다. 실패 메시지를 분리해 원인 분석/재처리를 하고 싶다.

A. CloudFront invalidation  
B. DLQ 구성  
C. Security group 수정  
D. KMS key rotation  

**Answer:** B  
**Explanation:** DLQ는 실패 격리와 재처리 경로를 제공한다.  
**Tags:** `domain:2` `services:SQS`

## Q4

**Scenario:** HTTP 기반 웹 서비스에서 경로 기반 라우팅이 필요하다.

A. NLB  
B. ALB  
C. Route 53 Weighted routing만 사용  
D. CloudTrail  

**Answer:** B  
**Explanation:** ALB는 L7(host/path) 라우팅을 지원한다.  
**Tags:** `domain:2` `services:ELB`

## Q5

**Scenario:** RDS에서 “가용성(자동 failover)”을 목표로 한다. 가장 적절한 선택은?

A. Read replica  
B. Multi-AZ  
C. 단일 AZ + 스냅샷  
D. DynamoDB Streams  

**Answer:** B  
**Explanation:** Multi-AZ는 자동 failover로 HA를 제공한다. Read replica는 주로 읽기 확장이다.  
**Tags:** `domain:2` `services:RDS,Aurora`

## Q6

**Scenario:** Route 53에서 헬스체크 기반 장애 조치가 필요하다.

A. Failover routing policy  
B. Geolocation routing policy  
C. Simple routing policy  
D. Multi-value answer는 불가능하다  

**Answer:** A  
**Explanation:** Failover 라우팅은 헬스체크 기반 primary/secondary 구성을 지원한다.  
**Tags:** `domain:2` `services:Route53`

## Q7

**Scenario:** RTO가 아주 짧아야 하지만 비용은 제한적이다. 다음 중 일반적으로 Backup/Restore보다 RTO를 줄이는 선택은?

A. Pilot light  
B. 로그 압축만 수행  
C. 단일 AZ 유지  
D. CloudFront만 사용  

**Answer:** A  
**Explanation:** Pilot light는 핵심 구성만 상시 유지해 복구 시간을 줄인다.  
**Tags:** `domain:2` `services:DR`

## Q8

**Scenario:** S3 데이터 내구성과 복구를 위해 버전 관리와 복제를 설계한다. 가장 적절한 조합은?

A. Versioning + Replication  
B. 버킷 퍼블릭 오픈  
C. SQS 사용  
D. KMS만 설정  

**Answer:** A  
**Explanation:** versioning은 실수/삭제 복구, replication은 다른 위치로 내구성을 확장한다.  
**Tags:** `domain:2` `services:S3`

## Q9

**Scenario:** EventBridge가 적합한 경우는?

A. 큐 기반 버퍼링이 핵심일 때  
B. 규칙 기반 라우팅/다양한 AWS 서비스 통합 이벤트 처리일 때  
C. 정적 콘텐츠 캐시가 필요할 때  
D. TLS 인증서 발급이 필요할 때  

**Answer:** B  
**Explanation:** EventBridge는 이벤트 라우팅/통합에 강하다. 버퍼링은 SQS가 더 직접적이다.  
**Tags:** `domain:2` `services:EventBridge`

## Q10

**Scenario:** 느슨한 결합 아키텍처에서 “중복 메시지 처리”에 대한 올바른 태도는?

A. 중복은 절대 발생하지 않는다  
B. 중복은 발생할 수 있으니 idempotent 처리로 방어한다  
C. 중복은 VPC로 해결한다  
D. 중복은 KMS로 해결한다  

**Answer:** B  
**Explanation:** 적어도 한 번(at-least-once) 전달 모델에서 중복은 정상이며 처리측 방어가 필요하다.  
**Tags:** `domain:2` `services:SQS,SNS`

## Q11

**Scenario:** 다음 중 “가용성”을 직접 높이는 구성으로 가장 적절한 것은?

A. 단일 AZ 배포  
B. Multi-AZ 배포  
C. 더 큰 인스턴스 1대  
D. 코드 압축  

**Answer:** B  
**Explanation:** AZ 분산은 장애 영역을 줄여 가용성을 올린다.  
**Tags:** `domain:2` `services:HA`

## Q12

**Scenario:** DR 설계에서 RPO의 의미는?

A. 복구 시간 목표  
B. 복구 시점 목표(데이터 손실 허용량)  
C. 응답 시간 목표  
D. 비용 목표  

**Answer:** B  
**Explanation:** RPO는 장애 시 허용 가능한 데이터 손실 시점이다.  
**Tags:** `domain:2` `services:DR`

