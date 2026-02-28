# 02-quiz - Week 01 Day 05 (Week Summary / Domain 1)

- 문항 수: 10 (Day05 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

운영자들이 “급해서요”라는 말로 장기 액세스 키를 공유하기 시작했고, 감사팀은 “누가 했는지”도 애매해지는 상황을 위험 신호로 본다. 교차 계정 운영까지 고려하면 키 공유는 더 위험해진다.  
요구사항(키 공유 금지, 필요 시 임시 권한, 감사 가능)에 가장 적절한 기본 설계는?
A. S3를 퍼블릭으로 열어 인증 없이 접근한다  
B. Role을 만들고 STS `AssumeRole`로 임시 자격 증명을 사용한다  
C. 팀 공용 IAM 사용자 키를 공유한다  
D. 루트 사용자만 쓰도록 강제한다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: 장기 키 공유를 제거하고(노출/회수), 임시 자격 증명으로 수명/범위를 제한한다.
- 소거법
  - C (명확히 틀림): 키 공유는 회수/감사/노출에 취약하다.
  - D (근접 오답): 강해 보이지만 통제/감사/권한 분리 관점에서 오답이다.
  - A (명확히 틀림): 인증 제거는 요구사항과 정반대다.
- 한 줄 규칙: “키 공유” 신호가 보이면 **STS AssumeRole**.
- 태그: `pillar:security` `services:STS,IAM` `week:01` `day:05`

</details>

---

## Q2. (복수정답: 2개)

외부 파트너 SaaS가 고객 계정 Role을 AssumeRole 해서 제한된 리소스만 접근해야 한다. 고객은 “키 공유 금지”와 confused deputy 위험 완화를 요구한다.  
요구사항을 직접적으로 만족시키는 조치 2개를 고르시오.
A. 파트너에게 IAM 사용자 액세스 키를 발급해 전달한다  
B. 루트 사용자만 사용하도록 강제한다  
C. Role trust policy에 `ExternalId` 조건을 추가한다  
D. S3 버킷을 퍼블릭으로 열어 인증을 제거한다  
E. Role 권한을 최소 권한으로 제한하고, 필요 시 session policy로 더 좁힌다  
<details>
<summary>정답/해설</summary>

- 정답: C, E
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: 제3자 교차 계정은 “입구(trust)”를 ExternalId로 잠그고, “출구(permission)”를 최소 권한으로 줄이는 게 핵심이다.
- 소거법
  - A (명확히 틀림): 장기 키 공유는 회수/감사/노출에 취약하다.
  - D (명확히 틀림): 인증 제거는 요구사항과 정반대다.
  - B (명확히 틀림): 루트는 통제/감사/분리 관점에서 오답이다.
- 한 줄 규칙: 제3자 접근은 **ExternalId + 최소 권한**으로 잠근다.
- 태그: `pillar:security` `services:STS,IAM` `week:01` `day:05`

</details>

---

## Q3.

보안팀이 “실수로 공개 S3를 만들거나 특정 서비스 사용” 같은 위험을 조직 단위로 막고 싶어 한다. 팀이 계정 안에서 IAM Allow를 아무리 늘려도 “어떤 규칙은 절대 못 넘게” 만드는 상한선이 필요하다.  
조직 단위 가드레일(Organizations SCP)을 올바르게 이해한 설명은?
A. SCP는 특정 S3 버킷에만 적용된다  
B. SCP는 권한을 부여하므로, SCP Allow만 있으면 IAM 없이도 된다  
C. SCP는 OU/계정 단위 상한선이며, SCP에서 막히면 IAM Allow로 뚫을 수 없다  
D. SCP는 네트워크 인바운드만 제어한다  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 표준 가드레일을 “구조적으로” 유지해 팀이 바뀌어도 운영 일관성을 만든다. SCP는 부여가 아니라 제한이다.
- 소거법
  - B (근접 오답): 시험 단골 함정. SCP는 권한 부여가 아니다.
  - A (명확히 틀림): 조직 단위다.
  - D (명확히 틀림): 권한/API 상한선이지 네트워크가 아니다.
- 한 줄 규칙: **SCP=상한선, IAM=부여**.
- 태그: `pillar:operational-excellence` `services:Organizations,SCP,IAM` `week:01` `day:05`

</details>

---

## Q4.

S3 SSE-KMS와 Secrets Manager를 적용한 뒤 `AccessDenied`가 터진다. IAM 정책에 `kms:Decrypt`을 추가해도 해결이 안 된다. 고객 사례는 “암호화는 설정이 아니라 정책 문제로 귀결된다”는 포인트를 강조한다.  
가장 먼저 확인할 핵심 포인트는?
A. KMS key policy가 호출 주체를 허용하는지(관문) 확인한다  
B. Route 53 라우팅을 Weighted로 바꾼다  
C. S3 버킷을 퍼블릭으로 연다  
D. CloudFront 캐시를 지운다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: KMS는 key policy가 실제 gate 역할을 하는 경우가 흔하다. IAM Allow가 있어도 key policy가 막으면 실패한다.
- 소거법
  - D (명확히 틀림): 캐시는 권한을 해결하지 못한다.
  - B (명확히 틀림): DNS/라우팅은 KMS 권한과 무관하다.
  - C (명확히 틀림): 인증 제거는 요구사항과 정반대다.
- 한 줄 규칙: “KMS AccessDenied”면 **key policy**부터 본다.
- 태그: `pillar:security` `services:KMS` `week:01` `day:05`

</details>

---

## Q5.

DB 자격 증명을 저장해야 한다. 보안팀은 “정기 교체(rotate)”를 요구하고, 운영 인력은 1명이라 교체/검증/롤백을 자동화하고 싶다.  
가장 적절한 선택은?
A. CloudTrail  
B. S3  
C. Parameter Store(일반 String)  
D. Secrets Manager  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: rotation 요구는 “시크릿 운영 기능”이 필요하다는 강한 신호다. Secrets Manager가 자연스럽다.
- 소거법
  - B (명확히 틀림): 저장소일 뿐, 시크릿 운영/회전 기능이 아니다.
  - A (명확히 틀림): 감사/행위 로그다.
  - C (근접 오답): 단순 저장엔 좋지만 rotation 요구가 있으면 부족해지기 쉽다.
- 한 줄 규칙: “rotation”이면 **Secrets Manager**.
- 태그: `pillar:security` `services:SecretsManager` `week:01` `day:05`

</details>

---

## Q6. (복수정답: 2개)

`s3:GetObject`는 이미 허용돼 있는데, SSE-KMS로 암호화된 객체만 `AccessDenied`가 난다. 로그를 보면 S3가 KMS로 복호화를 ‘대신 호출’하는 순간에 막힌다.  
이 유형을 가장 빠르게 진단하기 위해 “가장 먼저” 확인할 2가지를 고르시오.
A. 객체가 어떤 KMS 키로 암호화됐는지 확인한다  
B. NACL을 모두 Allow로 바꾼다  
C. S3 버킷을 퍼블릭으로 연다  
D. Route 53 레코드를 바꾼다  
E. 호출 주체가 `kms:Decrypt` 및 key policy 관문을 통과하는지 확인한다  
<details>
<summary>정답/해설</summary>

- 정답: A, E
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: SSE-KMS는 S3 권한만으로 끝나지 않는다. “객체의 키”와 “KMS 관문(권한/키 정책)”을 순서대로 봐야 진단이 빨라진다.
- 소거법
  - B (근접 오답): 네트워크를 열어도 KMS 권한 관문은 해결되지 않는다.
  - D (명확히 틀림): DNS는 권한 거부와 무관하다.
  - C (명확히 틀림): 인증 제거는 요구사항과 정반대다.
- 한 줄 규칙: “SSE-KMS AccessDenied”면 **KMS(키/정책)**까지 같이 본다.
- 태그: `pillar:operational-excellence` `services:S3,KMS` `week:01` `day:05`

</details>

---

## Q7.

보안 그룹이 갑자기 0.0.0.0/0으로 열렸다. 운영팀은 “누가, 언제, 어떤 역할로” 변경했는지 근거가 필요하다.  
이 질문에 가장 직접적으로 답하는 서비스는?
A. GuardDuty  
B. AWS Config  
C. CloudTrail  
D. ElastiCache  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: “누가 무엇을 했나”는 행위(API 호출)의 근거가 필요하고, CloudTrail이 그 축이다.
- 소거법
  - B (근접 오답): 상태/구성 이력에 강하지만 “누가 호출했나” 질문은 CloudTrail이 직결된다.
  - A (명확히 틀림): 탐지(findings) 계층이다.
  - D (명확히 틀림): 캐시 서비스다.
- 한 줄 규칙: “누가 했나”는 **CloudTrail**.
- 태그: `pillar:operational-excellence` `services:CloudTrail` `week:01` `day:05`

</details>

---

## Q8. (복수정답: 2개)

감사팀이 두 가지를 동시에 요구한다.  
1) “누가 설정을 바꿨나?”(행위/주체)  
2) “현재 구성이 규칙을 위반하고 있나?”(준수/상태)  
이 두 축을 가장 자연스럽게 만족하는 서비스 조합 2개를 고르시오.
A. Route 53  
B. AWS Config  
C. WAF  
D. CloudFront  
E. CloudTrail  
<details>
<summary>정답/해설</summary>

- 정답: B, E
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: 행위 추적은 CloudTrail, 준수/상태 평가는 Config가 축이다.
- 소거법
  - D (명확히 틀림): 캐싱/전송 계층이다.
  - A (근접 오답): DNS/라우팅은 준수 평가와 무관하다.
  - C (명확히 틀림): 웹 공격 방어(L7)다.
- 한 줄 규칙: “행위=CloudTrail, 준수/상태=Config”.
- 태그: `pillar:security` `services:CloudTrail,Config` `week:01` `day:05`

</details>

---

## Q9.

보안팀이 “의심스러운 API 호출/비정상 DNS 조회 같은 위협 징후를 자동으로 찾아서 알림을 보내라”고 요구한다. 기록만 남기는 로그 저장소가 아니라, 이상 패턴을 분석해 findings를 만들어야 한다.  
가장 자연스러운 서비스는?
A. AWS Config  
B. GuardDuty  
C. S3 Glacier  
D. CloudTrail Trail  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: GuardDuty는 여러 신호 소스 기반으로 이상 징후를 탐지해 findings를 만든다.
- 소거법
  - D (근접 오답): Trail은 장기 보관/감사엔 좋지만 탐지 엔진이 아니다.
  - C (명확히 틀림): 저장 클래스다.
  - A (명확히 틀림): 준수/상태 평가 축이다.
- 한 줄 규칙: “탐지/위협/알림”이면 **GuardDuty**.
- 태그: `pillar:security` `services:GuardDuty` `week:01` `day:05`

</details>

---

## Q10. (복수정답: 2개)

프라이빗 서브넷 워크로드가 **S3와 DynamoDB** 모두에 인터넷 없이 접근해야 한다. NAT 비용도 최소화해야 한다.  
가장 자연스러운 구성 2개를 고르시오.
A. Internet Gateway 추가  
B. S3 Gateway endpoint 추가  
C. S3 버킷을 퍼블릭으로 연다  
D. DynamoDB Gateway endpoint 추가  
E. Route 53 레코드 추가  
<details>
<summary>정답/해설</summary>

- 정답: B, D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: S3/DDB는 Gateway endpoint로 사설 경로를 만들 수 있어 NAT 비용을 줄이는 대표 정답 패턴이다.
- 소거법
  - A (근접 오답): 인터넷을 쓰는 방향으로 요구사항과 반대다.
  - E (명확히 틀림): DNS는 사설 경로를 만들지 않는다.
  - C (명확히 틀림): 인증 제거는 요구사항과 정반대다.
- 한 줄 규칙: “프라이빗 + NAT 비용”이면 **Gateway endpoint**.
- 태그: `pillar:cost-optimization` `services:VPCEndpoints,S3,DynamoDB` `week:01` `day:05`

</details>

---

