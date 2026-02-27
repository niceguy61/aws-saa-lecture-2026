# Quiz (Mock Questions) - Day 03

## Q1

**Scenario:** 운영팀이 “누가 보안 그룹 인바운드 규칙을 변경했는지”를 확인해야 한다. 가장 적절한 서비스는?

A. CloudTrail  
B. Config  
C. WAF  
D. Shield  

**Answer:** A  
**Explanation:** “누가 무엇을 했나(API 호출)”는 CloudTrail이 정답이다.  
**Tags:** `domain:1` `services:CloudTrail`

## Q2

**Scenario:** “현재 S3 버킷이 퍼블릭으로 열려 있는지”와 같은 구성 상태/준수를 지속적으로 평가하려 한다. 적절한 서비스는?

A. CloudTrail  
B. Config  
C. STS  
D. ACM  

**Answer:** B  
**Explanation:** 구성 변화/준수 평가가 목적이면 Config가 자연스럽다.  
**Tags:** `domain:1` `services:Config`

## Q3

**Scenario:** CloudTrail과 Config의 차이를 묻는다. 가장 적절한 설명은?

A. 둘 다 DDoS 방어 서비스다  
B. CloudTrail은 API 활동, Config는 리소스 구성/준수 상태를 중심으로 본다  
C. Config는 암호화 키를 관리한다  
D. CloudTrail은 캐시를 제공한다  

**Answer:** B  
**Explanation:** 시험형 핵심 문장이다: 행위 vs 상태.  
**Tags:** `domain:1` `services:CloudTrail,Config`

## Q4

**Scenario:** 보안팀이 “이상 행위 탐지”를 원한다. 다음 중 개념적으로 가장 가까운 서비스는?

A. GuardDuty  
B. CloudFront  
C. EBS  
D. Route 53  

**Answer:** A  
**Explanation:** GuardDuty는 위협 탐지(findings)로 출제된다.  
**Tags:** `domain:1` `services:GuardDuty`

## Q5

**Scenario:** 여러 보안 결과를 집계/표준화해 한 곳에서 볼 수 있게 하고 싶다. 가장 적절한 서비스는?

A. Security Hub  
B. KMS  
C. STS  
D. SQS  

**Answer:** A  
**Explanation:** Security Hub는 findings 집계 허브로 출제된다.  
**Tags:** `domain:1` `services:SecurityHub`

## Q6

**Scenario:** CloudTrail에서 장기 보관/감사를 위해 일반적으로 하는 구성은?

A. CloudTrail 로그를 S3로 저장(Trail)  
B. CloudTrail을 SQS로 저장  
C. CloudTrail을 EBS로 저장  
D. CloudTrail을 Parameter Store에 저장  

**Answer:** A  
**Explanation:** Trail은 S3로 로그를 남겨 장기 보관/감사를 가능하게 한다.  
**Tags:** `domain:1` `services:CloudTrail,S3`

## Q7

**Scenario:** 다음 중 CloudTrail을 선택해야 하는 질문은?

A. “현재 보안 그룹 규칙이 정책 위반인가?”  
B. “누가 IAM 정책을 변경했나?”  
C. “S3 storage class는 무엇이 최적인가?”  
D. “Lambda 동시성 제한은?”  

**Answer:** B  
**Explanation:** “누가 변경했나”는 API 활동 추적(CloudTrail)이다.  
**Tags:** `domain:1` `services:CloudTrail`

## Q8

**Scenario:** Config를 선택해야 하는 질문은?

A. “누가 AssumeRole 했나?”  
B. “리소스 구성이 언제 어떤 값으로 바뀌었나?”  
C. “DDoS 공격을 막고 싶다”  
D. “SQS 메시지 재시도”  

**Answer:** B  
**Explanation:** 상태/구성 변경은 Config 관점이다.  
**Tags:** `domain:1` `services:Config`

## Q9

**Scenario:** “탐지 서비스가 곧 로그 저장소다”라는 문장에 대한 올바른 반응은?

A. 맞다. GuardDuty는 로그 저장소다  
B. 틀리다. 탐지는 로그/신호(예: CloudTrail 등)를 기반으로 findings를 만든다  
C. 맞다. Security Hub는 S3에 로그를 쓴다  
D. 틀리다. KMS가 로그를 만든다  

**Answer:** B  
**Explanation:** 탐지/집계는 소스 로그(CloudTrail 등)와 역할이 다르다.  
**Tags:** `domain:1` `services:GuardDuty,SecurityHub,CloudTrail`

## Q10

**Scenario:** CloudTrail Event history와 Trail의 관계로 가장 적절한 설명은?

A. Event history는 SQS로만 저장된다  
B. Event history는 최근 이벤트 확인, Trail은 S3로 장기 저장/감사를 가능하게 한다  
C. Trail은 캐시 서비스다  
D. 둘은 완전히 무관하다  

**Answer:** B  
**Explanation:** 시험에서 자주 나오는 구분이다.  
**Tags:** `domain:1` `services:CloudTrail,S3`

