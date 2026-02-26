# Quiz (Mock Questions) - Day 01

## Questions

### Q1

**Scenario:** 보안팀이 “개발자가 장기 액세스 키를 공유하지 않도록” 교차 계정 운영 방식을 요구한다. 가장 적절한 설계는?

A. 운영 계정에서 개발 계정의 IAM 사용자 액세스 키를 발급받아 공유한다  
B. 개발 계정에 역할을 만들고 운영 계정의 주체가 STS AssumeRole로 접근한다  
C. 개발 계정에서 루트 사용자로 로그인해 필요한 작업을 수행한다  
D. 모든 계정을 하나로 합쳐 계정 간 이동을 없앤다  

**Answer:** B  
**Explanation:** 교차 계정 액세스는 역할 + trust policy + STS 임시 자격 증명이 표준이다. 키 공유/루트 사용은 보안 모범사례에 위배된다.  
**Tags:** `domain:1` `services:IAM,STS`

### Q2

**Scenario:** 동일 계정 내에서 EC2 인스턴스가 S3에 접근해야 한다. 가장 권장되는 방식은?

A. 코드에 액세스 키를 하드코딩한다  
B. IAM 사용자에 액세스 키를 만들고 인스턴스에 저장한다  
C. IAM 역할을 인스턴스 프로파일로 연결하고 필요한 권한만 부여한다  
D. S3 버킷을 퍼블릭으로 열어 접근한다  

**Answer:** C  
**Explanation:** 워크로드 권한은 IAM Role로 위임하고 장기 키를 피한다.  
**Tags:** `domain:1` `services:IAM,EC2`

### Q3

**Scenario:** Organizations에서 SCP로 특정 서비스 사용을 차단했다. 개발자가 “IAM에서 Allow를 줬는데도” 접근이 안 된다고 한다. 가장 먼저 설명해야 할 사실은?

A. SCP는 권한을 부여하므로 Allow를 더 주면 된다  
B. SCP는 계정/OU의 최대 허용 범위를 제한하며, SCP에서 막히면 IAM Allow가 있어도 Deny다  
C. SCP는 리전별로만 적용된다  
D. SCP는 루트 사용자에게는 절대 적용되지 않는다  

**Answer:** B  
**Explanation:** SCP는 상한선이다. 상위에서 막으면 하위 Allow로 해제할 수 없다.  
**Tags:** `domain:1` `services:Organizations`

### Q4

**Scenario:** S3 접근 제어에서 “특정 버킷을 다른 계정에 공유”해야 한다. 더 자연스러운 선택은?

A. 공유 대상 계정에 동일한 IAM 사용자 이름을 만든다  
B. 버킷 정책(resource-based policy)로 외부 계정 principal을 허용한다  
C. 보안 그룹에서 인바운드 443만 허용한다  
D. Route 53 레코드를 공유한다  

**Answer:** B  
**Explanation:** 교차 계정 리소스 공유는 resource-based policy가 기본 패턴이다.  
**Tags:** `domain:1` `services:S3,IAM`

### Q5

**Scenario:** “Explicit Deny”가 포함된 정책이 하나라도 존재하면 결과는?

A. 다른 Allow가 더 많으면 Allow  
B. 리소스 정책이 있으면 Allow  
C. 무조건 Deny  
D. SCP가 없으면 Allow  

**Answer:** C  
**Explanation:** 정책 평가에서 Explicit Deny가 최우선이다.  
**Tags:** `domain:1` `services:IAM`

### Q6

**Scenario:** 외부 SaaS 업체가 고객 계정의 역할을 AssumeRole 하도록 구성한다. 고객은 “confused deputy” 위험을 줄이고 싶다. 어떤 메커니즘이 핵심인가?

A. ExternalId 조건 사용  
B. S3 퍼블릭 접근 허용  
C. 액세스 키를 이메일로 전달  
D. 루트 사용자로만 접근 허용  

**Answer:** A  
**Explanation:** ExternalId는 제3자 교차 계정 AssumeRole에서 confused deputy 완화에 사용된다.  
**Tags:** `domain:1` `services:STS`

### Q7

**Scenario:** 다음 중 “권한을 부여하지 않고 상한선만 제한”하는 것은?

A. IAM inline policy  
B. S3 bucket policy  
C. Permissions boundary  
D. AWS access key  

**Answer:** C  
**Explanation:** Permissions boundary는 identity에 대해 최대 권한 상한선을 강제한다.  
**Tags:** `domain:1` `services:IAM`

### Q8

**Scenario:** 역할(Role)의 trust policy가 정의하는 것은?

A. AssumeRole 이후 수행 가능한 액션 목록  
B. 누가/어떤 주체가 그 역할을 Assume 할 수 있는지  
C. 버킷에 접근 가능한 IP 대역  
D. CloudTrail 로그 저장 위치  

**Answer:** B  
**Explanation:** trust policy는 “Assume 가능한 주체”를, permission policy는 “Assume 후 권한”을 정의한다.  
**Tags:** `domain:1` `services:IAM,STS`

### Q9 (Multiple response)

**Scenario:** IAM 모범사례로 옳은 것을 모두 고르시오.

A. 루트 사용자 MFA 활성화  
B. 장기 액세스 키를 여러 팀이 공유  
C. 최소 권한 원칙 적용  
D. 워크로드 권한은 IAM role로 위임  

**Answer:** A, C, D  
**Explanation:** MFA/least privilege/role 기반 위임은 모범사례다. 키 공유는 안티패턴이다.  
**Tags:** `domain:1` `services:IAM`

### Q10

**Scenario:** AssumeRole 시점에 session policy를 넣는 목적은?

A. 역할 권한을 영구적으로 확장한다  
B. 임시 세션의 권한을 추가로 제한한다  
C. S3 버킷 이름을 암호화한다  
D. VPC 라우팅을 변경한다  

**Answer:** B  
**Explanation:** session policy는 AssumeRole로 발급된 세션 권한을 “더 좁게” 만들 수 있다.  
**Tags:** `domain:1` `services:STS`

### Q11

**Scenario:** “그룹(Group)”에 대해 옳은 설명은?

A. 그룹은 리소스 정책을 가질 수 있다  
B. 그룹은 사용자 권한 관리를 단순화하는 단위이며, 리소스에 직접 붙지 않는다  
C. 그룹은 STS로 임시 자격 증명을 발급한다  
D. 그룹은 SCP를 대체한다  

**Answer:** B  
**Explanation:** 그룹은 사용자에게 정책을 묶어 적용하기 위한 관리 단위다.  
**Tags:** `domain:1` `services:IAM`

### Q12

**Scenario:** 다음 중 “권한 부여 모델을 유연하게 설계”하기 위한 조합으로 가장 적절한 것은?

A. 사용자마다 inline policy로 모든 권한 부여  
B. 역할 기반(RBAC)으로 역할에 정책을 부여하고 필요 시 AssumeRole로 전환  
C. 루트 사용자 공유  
D. 모든 버킷을 퍼블릭으로 전환  

**Answer:** B  
**Explanation:** RBAC + AssumeRole은 분리/감사/회수 관점에서 유리하며 시험에 자주 등장한다.  
**Tags:** `domain:1` `services:IAM,STS`

