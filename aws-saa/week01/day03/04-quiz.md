# 04-quiz - Week 01 Day 03 (CloudTrail / Config / Detection Services)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

새벽에 알림이 떴다. “보안 그룹 인바운드가 0.0.0.0/0으로 열렸습니다.” 운영팀은 즉시 “누가, 언제, 어떤 방식으로(콘솔/IaC/CLI) 열었지?”를 알아야 한다. 애플리케이션 로그에는 아무것도 없고, 인프라 변경은 앱 로그 밖에서 일어난다.  
이 질문(누가 무엇을 했나)에 가장 직접적으로 답을 주는 서비스는?
A. CloudTrail  
B. GuardDuty  
C. Inspector  
D. AWS Config  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 장애/사고에서 “근거를 빠르게 찾아 복구”하는 과정이 중요하다. CloudTrail은 API 호출(행위)의 영수증이라 “누가 무엇을 했나”에 직접 답한다.
- 소거법
  - D (근접 오답): Config는 “상태/구성” 이력에 강하지만, “누가 호출했나” 질문에는 CloudTrail이 더 직결된다.
  - B (명확히 틀림): GuardDuty는 탐지(findings) 계층이지, 변경 행위의 원장 로그가 아니다.
  - C (명확히 틀림): Inspector는 취약점/구성 평가 축이다.
- 한 줄 규칙: “누가 바꿨나/누가 삭제했나”는 **CloudTrail**.
- 태그: `pillar:operational-excellence` `services:CloudTrail` `week:01` `day:03`

</details>

---

## Q2.

감사팀이 요구한다. “퍼블릭 S3가 생기면 바로 잡혀야 합니다. 그리고 지난 3개월 동안 어떤 리소스가 규칙을 위반했는지 보고서가 필요해요.”  
이 요구의 핵심은 ‘행위 로그’보다 ‘리소스가 현재/과거에 어떤 구성 상태였는지’와 ‘규칙 위반 여부(준수)’다. 이 경우 가장 적절한 서비스는?
A. AWS Config를 사용해 구성 이력과 규칙 기반 준수 평가를 수행한다  
B. WAF를 사용해 HTTP 공격을 차단한다  
C. CloudTrail Event history만 사용한다  
D. Route 53 라우팅 정책을 Failover로 바꾼다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: 준수/규정 위반은 “현재 상태가 기준을 어겼는가”로 판단하는 흐름이 필요하다. Config는 구성 이력 + 규칙 평가로 그 질문에 맞는다.
- 소거법
  - C (근접 오답): 행위 추적에는 유용하지만, 준수/상태 평가 요구를 바로 만족시키기 어렵다.
  - B (명확히 틀림): 웹 공격 방어(L7)로 준수 보고서를 만들 수 없다.
  - D (명확히 틀림): 라우팅은 준수 평가와 무관하다.
- 한 줄 규칙: “준수/규칙 위반/보고서” 신호가 보이면 **Config**.
- 태그: `pillar:security` `services:Config` `week:01` `day:03`

</details>

---

## Q3.

로그는 쌓이는데, 문제는 “누가 봐서” 이상을 판단하느냐다. 보안팀은 “의심스러운 API 호출/비정상 DNS 조회/이상 트래픽 같은 위협 징후를 자동으로 찾아서 알림을 보내라”고 요구한다.  
CloudTrail이 기록을 남긴다고 해서 자동으로 위협을 찾아주지는 않는다. 이 요구에 가장 직접적으로 대응하는 서비스는?
A. CloudTrail Trail  
B. AWS Config  
C. S3 Glacier Deep Archive  
D. GuardDuty  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: GuardDuty는 여러 신호 소스(CloudTrail/VPC/DNS 등) 기반으로 이상 패턴을 분석해 findings를 만든다. “탐지/알림” 요구의 핵심이다.
- 소거법
  - A (근접 오답): Trail은 장기 보관/감사엔 좋지만, “탐지 엔진”은 아니다.
  - B (명확히 틀림): Config는 준수/상태 평가 축이다.
  - C (명확히 틀림): 저장 클래스는 탐지와 무관하다.
- 한 줄 규칙: “탐지/위협/알림” 신호가 나오면 **GuardDuty**가 후보로 올라간다.
- 태그: `pillar:security` `services:GuardDuty` `week:01` `day:03`

</details>

---

## Q4.

여러 계정/여러 서비스에서 보안 결과가 쏟아지기 시작했다. 팀은 “각 서비스 콘솔을 돌아다니며 확인”하는 방식으로는 운영이 안 된다고 느낀다. 보안팀은 “findings를 한 곳에서 모아 표준화하고, 우선순위를 잡아 운영하라”고 한다.  
이 요구에 가장 자연스러운 서비스는?
A. IAM Identity Center  
B. EFS  
C. CloudFront  
D. Security Hub  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 관측/운영 포인트를 “한 곳에서 관리 가능하게” 만드는 게 중요하다. Security Hub는 여러 보안 결과를 집계/표준화해 허브 역할을 한다.
- 소거법
  - C (명확히 틀림): 엣지 캐싱/전송 최적화 서비스다.
  - A (근접 오답): 출입구(SSO) 통합이지, findings 집계 허브는 아니다.
  - B (명확히 틀림): 파일 스토리지다.
- 한 줄 규칙: “보안 결과를 한 곳에서 집계/표준화”는 **Security Hub**.
- 태그: `pillar:operational-excellence` `services:SecurityHub` `week:01` `day:03`

</details>

---

## Q5. (복수정답: 2개)

감사/보안 질문이 동시에 들어왔다.  
1) “누가 보안 그룹을 열었는가?”(행위/주체)  
2) “현재 우리 계정은 ‘퍼블릭 S3 금지’ 규칙을 위반하고 있는가?”(상태/준수)  
이 두 질문에 가장 자연스럽게 답하기 위한 서비스 조합 2개를 고르시오.
A. AWS Config  
B. Shield Advanced  
C. CloudFront  
D. Route 53  
E. CloudTrail  
<details>
<summary>정답/해설</summary>

- 정답: A, E
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: “행위(누가 무엇을 했나)”는 CloudTrail, “상태/준수(규칙 위반)”는 Config가 축이다. 고객 사례의 핵심 구분 그대로다.
- 소거법
  - C (명확히 틀림): 캐싱/전송 계층이다.
  - D (근접 오답): 라우팅/DNS로 보안 구성 준수 판단을 할 수 없다.
  - B (명확히 틀림): DDoS 완화 서비스다(행위/준수 질문과 축이 다름).
- 한 줄 규칙: “누가 했나=CloudTrail, 준수/상태=Config”를 세트로 기억한다.
- 태그: `pillar:security` `services:CloudTrail,Config` `week:01` `day:03`

</details>

---

