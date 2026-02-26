# Quiz (Mock Questions) - Day 02

## Q1

**Scenario:** SSE-KMS로 암호화된 S3 객체를 읽으려는데, `s3:GetObject`는 Allow인데도 AccessDenied가 난다. 가장 먼저 의심할 것은?

A. Route 53 라우팅 정책  
B. `kms:Decrypt` 권한 또는 KMS key policy  
C. CloudFront TTL  
D. SQS DLQ  

**Answer:** B  
**Explanation:** SSE-KMS 객체 접근은 KMS decrypt 경로가 걸릴 수 있어 KMS 권한/키 정책이 빈출 포인트다.  
**Tags:** `domain:1` `services:S3,KMS`

## Q2

**Scenario:** 애플리케이션 DB 비밀번호를 저장해야 하고, 주기적 rotation 요구가 있다. 가장 적절한 서비스는?

A. S3  
B. Secrets Manager  
C. CloudTrail  
D. Parameter Store(일반)  

**Answer:** B  
**Explanation:** rotation 요구가 있으면 Secrets Manager가 시험에서 강력한 힌트다.  
**Tags:** `domain:1` `services:SecretsManager`

## Q3

**Scenario:** KMS에서 키 사용을 제어할 때 특히 중요한 정책 유형은?

A. Security group  
B. Key policy  
C. Route table  
D. NACL  

**Answer:** B  
**Explanation:** KMS는 key policy가 핵심 gate로 출제된다.  
**Tags:** `domain:1` `services:KMS`

## Q4

**Scenario:** “IAM에서 Allow를 줬는데도 KMS 작업이 실패”한다. 가능한 원인으로 가장 타당한 것은?

A. S3 버킷 이름 중복  
B. key policy에서 해당 principal을 허용하지 않음  
C. CloudFront invalidation 미생성  
D. ALB 헬스체크 실패  

**Answer:** B  
**Explanation:** key policy가 막으면 IAM Allow가 있어도 실패할 수 있다.  
**Tags:** `domain:1` `services:KMS,IAM`

## Q5

**Scenario:** Parameter Store SecureString과 Secrets Manager의 차이를 묻는다. 다음 중 일반적으로 옳은 설명은?

A. Secrets Manager는 rotation 요구에 더 적합하다  
B. Parameter Store는 DDoS 방어 서비스다  
C. SecureString은 KMS를 사용할 수 없다  
D. Secrets Manager는 IAM과 통합되지 않는다  

**Answer:** A  
**Explanation:** Secrets Manager는 시크릿 운영 기능(예: rotation) 요구에 더 자연스럽다.  
**Tags:** `domain:1` `services:SecretsManager,SSM,KMS`

## Q6

**Scenario:** 최소 권한으로 KMS decrypt를 부여하려 한다. 가장 좋은 접근은?

A. `kms:*`를 `Resource:*`로 Allow  
B. 필요한 액션(`kms:Decrypt`)만, 특정 키 ARN으로 제한  
C. 루트 사용자만 사용  
D. 모든 계정에 동일 키를 공유  

**Answer:** B  
**Explanation:** 시험은 액션/리소스 범위를 최소화하는 답을 선호한다.  
**Tags:** `domain:1` `services:KMS,IAM`

## Q7

**Scenario:** 데이터 보호 통제로 가장 완성도 높은 답안은?

A. 암호화만 적용  
B. 접근 제어만 적용  
C. 암호화 + 접근 제어 + 감사까지 같이 설계  
D. 비용 최적화만 적용  

**Answer:** C  
**Explanation:** SAA는 통제 조합(암호화/권한/감사)을 함께 묻는 경우가 많다.  
**Tags:** `domain:1` `services:KMS,IAM,CloudTrail`

## Q8

**Scenario:** 다음 중 “SSE-KMS”의 의미로 가장 적절한 것은?

A. 클라이언트 측 암호화  
B. 서버 측에서 KMS 키로 암호화  
C. 네트워크 암호화만 수행  
D. 데이터가 암호화되지 않는다  

**Answer:** B  
**Explanation:** SSE-KMS는 서버 측 암호화에서 KMS를 키 관리에 사용한다는 의미다.  
**Tags:** `domain:1` `services:S3,KMS`

## Q9

**Scenario:** KMS에서 “허용/차단”을 설계할 때 key policy가 중요한 이유로 가장 적절한 것은?

A. key policy는 VPC 라우팅을 정의한다  
B. key policy는 키 자체에 대한 접근 제어(리소스 정책 성격)를 가진다  
C. key policy는 S3 스토리지 클래스를 결정한다  
D. key policy는 CloudFront 캐시 키를 정의한다  

**Answer:** B  
**Explanation:** KMS의 핵심 함정은 key policy/IAM policy 관계다.  
**Tags:** `domain:1` `services:KMS`

## Q10

**Scenario:** Secrets Manager 시크릿을 KMS로 보호하는 경우(일반적으로) 무엇을 함께 고려해야 하는가?

A. KMS decrypt 권한 설계  
B. Route 53 레코드 삭제  
C. NLB로 전환  
D. EBS 볼륨 타입 변경  

**Answer:** A  
**Explanation:** 시크릿 보호는 결국 키 사용 권한(누가 decrypt 가능한지) 설계로 이어진다.  
**Tags:** `domain:1` `services:SecretsManager,KMS,IAM`

