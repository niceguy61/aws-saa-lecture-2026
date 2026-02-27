# Case Quiz (Domain 1) - Day 05

## Q1

**Scenario:** 외부 파트너 SaaS가 고객 계정 리소스에 교차 계정으로 접근해야 한다. 고객은 confused deputy 위험을 줄이고 싶다.

A. 파트너에게 액세스 키를 발급해 전달한다  
B. 파트너가 고객 계정 Role을 AssumeRole 하도록 하고 trust policy에 ExternalId 조건을 둔다  
C. S3 버킷을 퍼블릭으로 열어 데이터만 공유한다  
D. 루트 사용자 접근을 허용한다  

**Answer:** B  
**Explanation:** 제3자 AssumeRole은 ExternalId로 confused deputy 완화를 한다. 키 공유/루트/퍼블릭은 보안 안티패턴이다.  
**Tags:** `domain:1` `services:IAM,STS`

## Q2

**Scenario:** 개발자가 IAM에서 Allow를 추가했는데도 API 호출이 계속 AccessDenied다. 조직은 SCP를 사용 중이다. 가장 먼저 확인할 것은?

A. CloudFront 캐시 설정  
B. SCP에서 해당 액션이 상한선으로 차단됐는지  
C. S3 스토리지 클래스  
D. Route 53 라우팅 정책  

**Answer:** B  
**Explanation:** SCP는 계정/OU 상한선이다. 상위에서 막히면 하위 Allow로 해제할 수 없다.  
**Tags:** `domain:1` `services:Organizations`

## Q3

**Scenario:** 애플리케이션이 DB 자격 증명을 저장해야 한다. 자동 rotation 요구가 있다. 가장 적절한 서비스는?

A. S3  
B. Systems Manager Parameter Store(일반 파라미터)  
C. Secrets Manager  
D. CloudTrail  

**Answer:** C  
**Explanation:** rotation/통합 관점에서 Secrets Manager가 정답 후보 1순위다.  
**Tags:** `domain:1` `services:SecretsManager`

## Q4

**Scenario:** KMS로 암호화된 시크릿을 읽을 수 있도록 최소 권한을 구성했다. 다음 중 일반적으로 같이 필요해지는 권한 조합은?

A. `secretsmanager:GetSecretValue`만 있으면 충분하다  
B. `kms:Decrypt`만 있으면 충분하다  
C. `secretsmanager:GetSecretValue` + `kms:Decrypt`가 필요할 수 있다  
D. `ec2:DescribeInstances`가 필수다  

**Answer:** C  
**Explanation:** 시크릿은 KMS로 보호되므로 복호화 권한이 함께 필요해지는 경우가 흔하다.  
**Tags:** `domain:1` `services:KMS,SecretsManager`

## Q5

**Scenario:** “누가 AssumeRole 할 수 있는지”를 정의하는 것은?

A. Role permission policy  
B. Role trust policy  
C. S3 bucket policy  
D. Security group  

**Answer:** B  
**Explanation:** trust policy는 Assume 가능한 주체를 정의한다. permission policy는 Assume 후 권한이다.  
**Tags:** `domain:1` `services:IAM,STS`

## Q6

**Scenario:** AWS API 호출 내역(누가/언제/무엇을)을 감사 목적에 맞게 확인하려 한다. 적절한 서비스는?

A. CloudTrail  
B. Config  
C. GuardDuty  
D. WAF  

**Answer:** A  
**Explanation:** CloudTrail은 API 호출(관리 이벤트/데이터 이벤트)을 기록한다.  
**Tags:** `domain:1` `services:CloudTrail`

## Q7

**Scenario:** 리소스 구성 변경(예: 보안 그룹 규칙 변경 이력)과 준수 상태를 추적하려 한다. 적절한 서비스는?

A. CloudTrail만으로 충분하다  
B. Config를 사용한다  
C. Shield를 사용한다  
D. CloudFront를 사용한다  

**Answer:** B  
**Explanation:** Config는 리소스 구성 변경/준수 평가에 적합하다.  
**Tags:** `domain:1` `services:Config`

## Q8

**Scenario:** 웹 애플리케이션을 L7에서 보호(OWASP Top 10, SQLi 등)해야 한다. 적절한 서비스는?

A. Shield Advanced  
B. WAF  
C. NACL  
D. STS  

**Answer:** B  
**Explanation:** WAF는 L7 규칙 기반 보호다. Shield는 DDoS 완화(주로 L3/4) 쪽이 핵심이다.  
**Tags:** `domain:1` `services:WAF,Shield`

## Q9

**Scenario:** 최소 권한 원칙을 가장 잘 만족하는 접근은?

A. 모든 리소스에 대해 `Action:*`, `Resource:*`로 Allow  
B. 특정 리소스 ARN과 필요한 액션만 Allow  
C. 모든 사용자가 AdministratorAccess 사용  
D. 루트 사용자 공유  

**Answer:** B  
**Explanation:** 시험에서 “최소 권한”은 범위(리소스) + 액션 최소화로 표현된다.  
**Tags:** `domain:1` `services:IAM`

## Q10

**Scenario:** 임시 자격 증명(AssumeRole)이 장기 액세스 키보다 유리한 이유로 가장 적절한 것은?

A. 키가 영구히 유효하다  
B. 키가 짧은 수명을 가지며 회수/만료가 쉽다  
C. 키를 이메일로 공유하기 쉽다  
D. 루트 사용자 권한을 자동으로 얻는다  

**Answer:** B  
**Explanation:** 임시 크레덴셜은 수명/회수/감사 측면에서 유리하다.  
**Tags:** `domain:1` `services:STS`

## Q11

**Scenario:** 다음 중 “상한선(최대 권한)”에 해당하는 것을 모두 고르시오.

A. SCP  
B. Permissions boundary  
C. IAM Group  
D. S3 lifecycle  

**Answer:** A, B  
**Explanation:** SCP/boundary는 최대 권한을 제한한다. 그룹은 관리 단위다.  
**Tags:** `domain:1` `services:Organizations,IAM`

## Q12

**Scenario:** “데이터 보호 통제” 관점에서 가장 완성도 높은 답안 구성은?

A. 암호화만 설정한다  
B. 접근 제어만 설정한다  
C. 암호화 + 접근 제어 + 감사(누가 읽었는지)까지 함께 설계한다  
D. 비용 최적화만 한다  

**Answer:** C  
**Explanation:** 시험은 보통 통제를 묶어서 묻는다(암호화/권한/감사).  
**Tags:** `domain:1` `services:KMS,IAM,CloudTrail`

