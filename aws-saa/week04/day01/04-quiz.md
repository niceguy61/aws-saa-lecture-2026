# 04-quiz - Week 04 Day 01 (Cost Explorer / Budgets / Cost Allocation Tags)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

이번 달 비용이 갑자기 2배가 됐다. 팀은 “요즘 배포가 많았으니 EC2겠지”라고 짐작하지만 근거가 없다. 여기서 가장 흔한 실수는 “일단 뭔가를 끄는 것”이다(운 좋으면 줄지만, 다음 주 장애로 돌아온다).  
먼저 해야 할 “원인 분석(어디서 늘었는지 분해)”에 가장 적절한 도구는?
A. Cost Explorer (서비스/리전/계정/태그로 Group by)  
B. CloudTrail (누가 무엇을 했나)  
C. Route 53 (DNS)  
D. AWS Budgets (임계치 알림)  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 최적화는 “감”이 아니라 “드라이버 파악”에서 시작한다. 비용을 축으로 분해/분석하는 도구가 Cost Explorer다.
- 소거법
  - D (근접 오답): 초과 감지엔 좋지만 “어디서 늘었는지 분석”의 1순위는 아니다.
  - C (명확히 틀림): DNS는 비용 분석 도구가 아니다.
  - B (근접 오답): 변경 원인 추적엔 도움되지만, 비용을 축으로 분해하는 도구는 아니다.
- 한 줄 규칙: “원인/추세/그룹핑 분석”이면 **Cost Explorer**.
- 태그: `pillar:cost-optimization` `services:CostExplorer` `week:04` `day:01`

</details>

---

## Q2.

팀은 비용 문제를 항상 “월말에 청구서로” 뒤늦게 알았다. 운영 인력이 1명이라, 사후 분석보다 “초과를 빨리 알아채는 센서”가 필요하다. 예산의 80%/100% 같은 임계치에 도달하면 이메일/슬랙으로 알림을 받고 싶다.  
가장 적절한 선택은?
A. AWS Budgets  
B. AWS Config  
C. CloudFront  
D. Cost Explorer  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 “사전 감지 → 빠른 대응” 루틴이 중요하다. Budgets는 분석 도구가 아니라 초과 알림(센서) 역할이다.
- 소거법
  - D (근접 오답): 분석엔 좋지만 임계치 알림 도구는 아니다.
  - B (명확히 틀림): 준수/상태 평가 도구다.
  - C (명확히 틀림): 캐시/전송 계층이다.
- 한 줄 규칙: “임계치/초과 알림”이면 **Budgets**.
- 태그: `pillar:operational-excellence` `services:Budgets` `week:04` `day:01`

</details>

---

## Q3.

팀이 4개로 늘자 비용 회의가 지옥이 됐다. “이번 달 비용은 누가 쓴 거죠?”를 아무도 답하지 못한다. 계정은 하나고 리소스 이름도 제각각이다. 팀별/프로젝트별 비용(차지백/쇼백)을 ‘근거 있게’ 나누려면 무엇이 첫 단추인가?
A. DynamoDB Scan을 늘린다  
B. 비용 할당 태그를 표준화하고 활성화해 Cost Explorer에서 태그로 Group by 가능하게 만든다  
C. CloudFront invalidation을 남발한다  
D. 모든 리소스를 퍼블릭으로 열어 운영을 단순화한다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용을 팀/프로젝트로 나누려면 “가시성의 기준”이 필요하다. 태그 표준화/활성화가 있어야 분석/최적화가 흔들리지 않는다.
- 소거법
  - D (명확히 틀림): 보안/비용 모두 악화될 수 있다.
  - C (명확히 틀림): 캐시 운영 포인트지 차지백 해법이 아니다.
  - A (명확히 틀림): DB 조회 방식과 비용 차지백은 무관하다.
- 한 줄 규칙: “팀별 비용”은 **태그(또는 계정 구조)**부터.
- 태그: `pillar:cost-optimization` `services:CostAllocationTags,CostExplorer` `week:04` `day:01`

</details>

---

## Q4.

비용이 올랐을 때 가장 “안전한” 첫 액션은 무엇인가? (장애를 유발할 수 있는 무작정 종료는 피해야 한다.)
A. 모든 리소스의 권한을 AdministratorAccess로 바꾼다  
B. Cost Explorer로 서비스/리전/태그 기준으로 비용 드라이버를 분해한 뒤 우선순위를 잡는다  
C. 가장 큰 리소스를 무조건 종료한다  
D. NAT Gateway를 무조건 삭제한다(서비스 영향은 고려하지 않는다)  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 근거 기반 변경으로 장애 리스크를 줄인다. 비용 최적화도 “분해 → 대안 비교 → 변경” 순서가 안전하다.
- 소거법
  - C (명확히 틀림): 비용은 줄 수 있어도 장애로 돌아오기 쉽다.
  - D (근접 오답): NAT가 드라이버일 수는 있지만 “무조건/영향 무시”는 위험하다.
  - A (명확히 틀림): 비용 문제 해결과 무관하고 보안까지 악화된다.
- 한 줄 규칙: 최적화도 **분석 후 변경**이 기본이다.
- 태그: `pillar:operational-excellence` `services:CostExplorer` `week:04` `day:01`

</details>

---

## Q5. (복수정답: 2개)

팀은 두 가지를 모두 원한다.  
1) 비용이 급증하면 “당일에” 알림을 받고 싶다(센서)  
2) 알림이 오면 “어느 서비스/어느 팀(태그)에서 늘었는지” 원인을 분해하고 싶다(분석)  
가장 자연스러운 조합 2개를 고르시오.
A. AWS Budgets  
B. Route 53  
C. GuardDuty  
D. Cost Explorer  
E. CloudFront  
<details>
<summary>정답/해설</summary>

- 정답: A, D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: Budgets는 초과 감지(알림), Cost Explorer는 원인 분해(분석) 역할 분담이다.
- 소거법
  - E (명확히 틀림): 캐시/전송 계층이다.
  - B (명확히 틀림): DNS다.
  - C (근접 오답): 보안 탐지엔 유용하지만 비용 센서/분석 도구는 아니다.
- 한 줄 규칙: “알림=Budgets, 분석=Cost Explorer”.
- 태그: `pillar:cost-optimization` `services:Budgets,CostExplorer` `week:04` `day:01`

</details>

---

