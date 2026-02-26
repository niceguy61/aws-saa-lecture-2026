# Quiz (Mock Questions) - Day 03

## Q1

**Scenario:** “실수로 S3 객체를 삭제/덮어썼을 때 복구”가 핵심 요구다. 가장 적절한 기능은?

A. S3 Versioning  
B. CloudFront Invalidation  
C. IAM Permission boundary  
D. Route 53 Latency routing  

**Answer:** A  
**Explanation:** accidental deletion/overwrite는 versioning 힌트다.  
**Tags:** `domain:2` `services:S3`

## Q2

**Scenario:** S3 Replication을 구성할 때 일반적으로 필수 전제는?

A. 양쪽 버킷 모두 versioning 활성화  
B. 양쪽 버킷 모두 퍼블릭 오픈  
C. CloudTrail 비활성화  
D. KMS 키 삭제  

**Answer:** A  
**Explanation:** replication은 versioning과 강하게 연결된다.  
**Tags:** `domain:2` `services:S3`

## Q3

**Scenario:** “리전 장애 대비”가 요구사항에 있다. 데이터 복제 관점에서 후보가 되는 것은?

A. 단일 버킷만 사용  
B. CRR/SRR 등 복제 전략 고려  
C. 보안 그룹 변경  
D. WAF 룰 추가  

**Answer:** B  
**Explanation:** DR/리전 장애 요구가 있으면 복제가 후보가 된다(요구에 따라 CRR 등).  
**Tags:** `domain:2` `services:S3,DR`

## Q4

**Scenario:** EBS snapshot의 용도로 가장 적절한 것은?

A. DNS 라우팅  
B. 볼륨 백업/복구  
C. DDoS 방어  
D. 시크릿 rotation  

**Answer:** B  
**Explanation:** 스냅샷은 백업/복구 단위로 출제된다.  
**Tags:** `domain:2` `services:EBS`

## Q5

**Scenario:** 다음 중 versioning이 켜진 버킷에서 DELETE 후 나타날 수 있는 개념은?

A. delete marker  
B. IAM role  
C. NACL  
D. Target group  

**Answer:** A  
**Explanation:** versioning에서는 삭제 마커가 중요한 시험/실무 개념이다.  
**Tags:** `domain:2` `services:S3`

