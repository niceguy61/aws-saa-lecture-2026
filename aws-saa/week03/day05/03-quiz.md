# Case Quiz (Domain 3) - Day 05

## Q1

**Scenario:** 전 세계 사용자에게 정적 콘텐츠를 낮은 지연시간으로 제공해야 한다.

A. 단일 리전 EC2  
B. CloudFront  
C. CloudTrail  
D. KMS  

**Answer:** B  
**Explanation:** CloudFront는 엣지 캐시로 전 세계 지연을 줄이는 대표 선택지다.  
**Tags:** `domain:3` `services:CloudFront`

## Q2

**Scenario:** CloudFront에서 원본 객체가 변경됐는데도 사용자가 이전 버전을 본다. 빠르게 갱신하려면?

A. IAM 사용자 생성  
B. Invalidation 생성  
C. SQS DLQ 설정  
D. SCP 적용  

**Answer:** B  
**Explanation:** 캐시 무효화(invalidation)는 즉시성 있는 갱신 선택지다.  
**Tags:** `domain:3` `services:CloudFront`

## Q3

**Scenario:** DynamoDB에서 특정 파티션 키에 트래픽이 집중되어 지연이 발생한다. 가장 근본적인 접근은?

A. 무조건 DAX 추가  
B. 파티션 키 설계를 개선해 핫 파티션을 완화  
C. S3로 마이그레이션  
D. WAF 추가  

**Answer:** B  
**Explanation:** 핫 파티션은 키 설계 문제인 경우가 많다. DAX는 캐시지만 근본이 아닐 수 있다.  
**Tags:** `domain:3` `services:DynamoDB`

## Q4

**Scenario:** 반복 조회가 많은 애플리케이션에서 DB 읽기 지연을 줄이려 한다.

A. ElastiCache 같은 캐시 계층 추가를 고려한다  
B. CloudTrail을 활성화한다  
C. NAT Gateway를 추가한다  
D. ACM 인증서를 발급한다  

**Answer:** A  
**Explanation:** 캐시는 반복 읽기 워크로드에서 성능 개선의 표준 패턴이다.  
**Tags:** `domain:3` `services:ElastiCache`

## Q5

**Scenario:** EBS 스토리지 성능을 높이고 싶다. 일반적으로 고려하는 축은?

A. IOPS/Throughput  
B. Route 53 라우팅  
C. WAF 규칙  
D. CloudTrail 이벤트  

**Answer:** A  
**Explanation:** EBS는 볼륨 타입별 IOPS/throughput 특성이 핵심이다.  
**Tags:** `domain:3` `services:EBS`

## Q6

**Scenario:** Lambda가 종종 throttling 된다. 가장 관련 있는 개념은?

A. 동시성(concurrency) 제한  
B. S3 lifecycle  
C. SCP  
D. DLQ  

**Answer:** A  
**Explanation:** Lambda throttling은 동시성 제한과 직접 연결된다.  
**Tags:** `domain:3` `services:Lambda`

## Q7

**Scenario:** Global Accelerator가 CloudFront보다 더 어울리는 경우(개념)는?

A. 캐시 가능한 정적 콘텐츠  
B. TCP/UDP 기반의 글로벌 가속(고정 Anycast IP 필요)  
C. S3 객체 암호화  
D. IAM 역할 전환  

**Answer:** B  
**Explanation:** GA는 L4 수준 가속/Anycast IP가 핵심이다.  
**Tags:** `domain:3` `services:GlobalAccelerator,CloudFront`

## Q8

**Scenario:** Aurora와 RDS 비교에서 성능 선택지를 묻는다. 일반적으로 옳은 방향은?

A. 둘은 항상 동일하다  
B. 요구(읽기 확장/복제/클러스터) 패턴에 따라 Aurora가 더 유리할 수 있다  
C. Aurora는 캐시 서비스다  
D. RDS는 NoSQL이다  

**Answer:** B  
**Explanation:** 시험은 “요구사항 기반 선택”을 묻는다.  
**Tags:** `domain:3` `services:Aurora,RDS`

## Q9

**Scenario:** CloudFront 캐시 키에 쿼리 스트링/헤더를 포함시키면 어떤 영향이 있을 수 있는가?

A. 캐시 히트율이 낮아질 수 있다  
B. 항상 성능이 좋아진다  
C. DLQ로 메시지가 이동한다  
D. KMS 권한이 필요해진다  

**Answer:** A  
**Explanation:** 캐시 키가 세분화되면 객체 변종이 늘어 히트율이 떨어질 수 있다.  
**Tags:** `domain:3` `services:CloudFront`

## Q10

**Scenario:** EFS 사용 시 성능 모드/처리량 모드를 고려해야 하는 이유는?

A. IAM 그룹 권한 때문  
B. 파일 시스템 성능 특성이 워크로드에 영향  
C. Route 53 때문  
D. CloudTrail 때문  

**Answer:** B  
**Explanation:** EFS는 워크로드 특성에 따라 성능/처리량 선택이 중요하다.  
**Tags:** `domain:3` `services:EFS`

## Q11

**Scenario:** 성능 문제에서 “캐시를 먼저 고려”하는 이유로 가장 적절한 것은?

A. 캐시는 데이터 전송 비용만 올린다  
B. 캐시는 호출 수를 줄여 전체 병목을 완화할 수 있다  
C. 캐시는 보안 기능이다  
D. 캐시는 DR 기능이다  

**Answer:** B  
**Explanation:** 병목의 큰 부분이 반복 읽기라면 캐시가 가장 큰 효과를 낸다.  
**Tags:** `domain:3` `services:CloudFront,ElastiCache`

## Q12

**Scenario:** 다음 중 “네트워크 아키텍처 성능” 선택지로 가장 관련이 높은 것은?

A. CloudFront/GA  
B. KMS  
C. IAM Identity Center  
D. Secrets Manager  

**Answer:** A  
**Explanation:** 엣지/가속은 네트워크 성능 선택지로 자주 출제된다.  
**Tags:** `domain:3` `services:CloudFront,GlobalAccelerator`

