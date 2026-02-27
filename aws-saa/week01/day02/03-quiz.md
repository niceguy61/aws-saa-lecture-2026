# 03-quiz - Week 01 Day 02 (KMS / Secrets / S3 SSE-KMS)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

팀이 `.env` 파일로 시크릿을 관리하다가 사고를 겪었다. 개발/스테이징/운영 환경이 늘면서 시크릿이 파일 복사로 퍼졌고, 누가 언제 바꿨는지 추적도 어렵다. 여기에 보안팀이 “DB 비밀번호는 주기적으로 교체(rotate)해야 한다”고 요구한다. 운영 담당이 1명이라 수동 교체는 부담이고, 교체가 실패하면 롤백까지 고려해야 한다.  
이 요구를 가장 자연스럽게 만족시키는 선택은?

A. 시크릿을 S3에 업로드하고, 필요할 때 다운로드한다  
B. Secrets Manager를 사용해 시크릿을 저장하고(필요 시) rotation을 구성한다  
C. Parameter Store(일반 String)로만 저장하고 수동으로 교체한다  
D. 시크릿을 코드에 하드코딩해 배포한다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: “rotation/자동 교체”는 단순 저장 문제가 아니라 수명 관리(교체/검증/회수/감사) 문제다. 문장에 rotation이 있으면 Secrets Manager가 강한 정답 후보가 된다.
- 소거법
  - A (명확히 틀림): 저장 위치만 바뀌고, 교체/감사/회수 요구를 만족하기 어렵다.
  - C (근접 오답): 저장은 가능하지만, “회전/운영 기능” 요구가 붙으면 부족해지기 쉽다.
  - D (명확히 틀림): 유출 경로를 스스로 만든다.
- 한 줄 규칙: 문장에 **rotation**이 보이면 Secrets Manager부터 본다.
- 태그: `pillar:security` `services:SecretsManager,ParameterStore` `week:01` `day:02`

</details>

---

## Q2.

이번엔 요구사항이 다르다. 저장해야 하는 값은 민감해서 암호화는 필요하지만, “정기 회전/자동 교체” 요구는 없다. 운영 기능보다 “단순 저장 + 접근 통제”가 우선이고, 불필요하게 과한 선택은 피하고 싶다.  
비용/단순성을 함께 고려했을 때 가장 자연스러운 선택은?

A. Secrets Manager만 사용한다(항상 정답)  
B. Parameter Store의 SecureString + KMS로 암호화해 저장한다  
C. Git 저장소에 암호화해서 커밋한다  
D. EC2 인스턴스에 텍스트 파일로 저장한다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용 최적화는 “요구 기능만” 선택하는 게 핵심이다. 회전/운영 기능이 필요 없고 단순 저장이면 Parameter Store(SecureString)가 충분한 경우가 많다.
- 소거법
  - A (근접 오답): 기능은 맞지만 “항상”은 아니다. 요구 기능 대비 과할 수 있다.
  - C (명확히 틀림): 저장소 노출/키 관리/감사 관점에서 위험하다.
  - D (명확히 틀림): 파일 배포/회수/감사가 취약하다.
- 한 줄 규칙: “회전”이 없으면 **Parameter Store(SecureString)**도 강한 후보가 된다.
- 태그: `pillar:cost-optimization` `services:ParameterStore,KMS` `week:01` `day:02`

</details>

---

## Q3.

보안팀이 “모든 데이터는 KMS로 암호화하세요”라고 해서 팀은 S3 SSE-KMS도 켰고, Secrets Manager도 KMS로 암호화했다. 그런데 배포 후부터 운영에서 `AccessDenied`가 터진다. 개발자는 “S3 권한은 줬는데요?”라고 하고, IAM 정책에 `kms:Decrypt`을 추가해도 여전히 안 된다.  
이 상황에서 가장 먼저 의심해야 할 핵심 포인트는?

A. KMS는 key policy가 관문(gate)일 수 있으므로 key policy에서 호출 주체가 허용되는지 확인한다  
B. Route 53 라우팅 정책을 Latency로 바꾼다  
C. CloudFront 캐시 정책을 조정한다  
D. EBS 볼륨 타입을 gp3로 바꾼다  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: KMS는 “키를 누가 쓸 수 있나”를 key policy로 강하게 통제하는 설계가 흔하다. IAM Allow가 있어도 **key policy가 막으면 실패**할 수 있다.
- 소거법
  - B (명확히 틀림): DNS는 암호화/권한과 무관하다.
  - C (명확히 틀림): 캐시는 권한 거부를 해결하지 못한다.
  - D (명확히 틀림): 스토리지는 권한/키 정책과 무관하다.
- 한 줄 규칙: “KMS AccessDenied”면 **IAM만 보지 말고 key policy**를 본다.
- 태그: `pillar:security` `services:KMS` `week:01` `day:02`

</details>

---

## Q4. (복수정답: 2개)

팀이 S3에 SSE-KMS를 켰다. 버킷 정책과 IAM 정책에서 `s3:GetObject`는 이미 허용되어 있고, 일반 객체는 잘 읽힌다. 그런데 SSE-KMS로 암호화된 객체만 특정 경로에서 `AccessDenied`가 난다. 로그를 보면 S3가 KMS로 복호화를 시도하는 순간에 막힌다(대행 호출).  
이 유형을 가장 빠르게 진단하기 위해 “가장 먼저” 확인할 2가지를 고르시오.

A. S3 버킷을 퍼블릭으로 열어 재현을 쉽게 만든다  
B. 해당 객체가 어떤 KMS 키로 암호화됐는지 확인한다  
C. CloudFront로 앞단 캐시를 붙여 우회한다  
D. 호출 주체(역할/서비스)가 `kms:Decrypt` 및 key policy 관문을 통과하는지 확인한다  
E. Route 53에 Weighted 라우팅을 추가한다  

<details>
<summary>정답/해설</summary>

- 정답: B, D
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 “빨리 진단하고 재발을 줄이는 체크 순서”가 핵심이다. SSE-KMS는 S3 권한만으로 끝나지 않고, **객체의 KMS 키**와 **KMS 권한/키 정책(관문)**을 같이 봐야 한다.
- 소거법
  - A (명확히 틀림): 편해 보이지만 보안 요구를 깨고 문제를 더 키운다.
  - C (근접 오답): 캐시는 증상을 가릴 수 있어도 권한/정책 원인을 해결하지 못한다.
  - E (명확히 틀림): DNS는 권한 거부와 무관하다.
- 한 줄 규칙: “SSE-KMS AccessDenied”면 **S3 다음은 KMS(키/정책)**다.
- 태그: `pillar:operational-excellence` `services:S3,KMS` `week:01` `day:02`

</details>

---

## Q5.

고객 사례에서 팀은 “암호화만 켜면 끝”이라고 생각했다. 그런데 실제로는 권한(정책)에서 막히고, “누가/언제/어떤 주체로 접근했는지” 같은 감사 요구까지 연결되면서 문제가 커졌다.  
시험/실무에서 “데이터 보호 통제”를 더 완성도 있게 설계하려면 어떤 방향이 가장 자연스러운가?

A. 암호화만 켠다(SSE-KMS만 켜면 끝)  
B. 암호화 + 접근 제어(최소 권한) + 감사(누가 접근했는지 추적)까지 묶어 설계한다  
C. 비용만 줄이면 보안은 자동으로 좋아진다  
D. 시크릿을 이메일로 공유해 운영을 단순화한다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: 보안은 단일 설정이 아니라 “통제 조합”으로 풀리는 경우가 많다(암호화/권한/감사). 고객 사례도 결국 정책/감사로 귀결된다.
- 소거법
  - A (근접 오답): 암호화는 필요하지만, 권한/감사가 빠지면 사고 대응이 약하다.
  - C (명확히 틀림): 비용과 보안은 별개 축이다.
  - D (명확히 틀림): 유출 경로를 스스로 만든다.
- 한 줄 규칙: “데이터 보호”는 보통 **암호화 + 권한 + 감사**로 답이 완성된다.
- 태그: `pillar:security` `services:KMS,IAM,CloudTrail` `week:01` `day:02`

</details>

---

## TL;DR (오늘의 규칙)

- “rotation”이면 **Secrets Manager**, “SSE-KMS AccessDenied”면 **KMS key policy/Decrypt**까지 같이 본다.
