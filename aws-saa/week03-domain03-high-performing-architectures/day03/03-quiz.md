# Quiz (Mock Questions) - Day 03

## Q1

**Scenario:** 스토리지 IOPS가 병목이라는 신호가 있다. 다음 중 가장 관련 있는 선택 축은?

A. EBS IOPS/throughput  
B. Route 53 Weighted  
C. WAF rule  
D. STS ExternalId  

**Answer:** A  
**Explanation:** 스토리지 성능은 IOPS/throughput 축으로 출제된다.  
**Tags:** `domain:3` `services:EBS`

## Q2

**Scenario:** 여러 EC2 인스턴스가 동일 파일을 동시에 접근해야 한다. 가장 적절한 스토리지는?

A. EBS  
B. EFS  
C. Instance store  
D. S3 Glacier  

**Answer:** B  
**Explanation:** 공유 파일 시스템 요구는 EFS가 정답 후보가 된다.  
**Tags:** `domain:3` `services:EFS`

## Q3

**Scenario:** gp3의 대표 장점으로 가장 적절한 것은?

A. 용량을 늘려야만 성능이 오른다  
B. 용량과 성능(IOPS/throughput)을 분리해 조정할 수 있다  
C. 항상 무료다  
D. DNS 라우팅이 자동이다  

**Answer:** B  
**Explanation:** gp3는 용량과 성능을 분리해 튜닝할 수 있다는 점이 자주 포인트로 나온다.  
**Tags:** `domain:3` `services:EBS`

## Q4

**Scenario:** EBS VolumeQueueLength가 지속적으로 높다. 가장 합리적인 1차 해석은?

A. 스토리지 I/O 병목 가능성  
B. DDoS 공격  
C. KMS 키 만료  
D. Route 53 장애  

**Answer:** A  
**Explanation:** 큐 길이는 디스크 I/O 대기 신호로 볼 수 있다.  
**Tags:** `domain:3` `services:EBS,CloudWatch`

## Q5

**Scenario:** “공유” 요구가 없고 단일 인스턴스에서 빠른 블록 스토리지가 필요하다. 더 자연스러운 선택은?

A. EBS  
B. EFS(무조건)  
C. Route 53  
D. Secrets Manager  

**Answer:** A  
**Explanation:** 공유 파일 시스템이 필요 없으면 블록 스토리지(EBS)가 보통 더 직접적이다.  
**Tags:** `domain:3` `services:EBS,EFS`

