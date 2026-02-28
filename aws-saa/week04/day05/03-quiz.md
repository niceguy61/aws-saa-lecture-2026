# 03-quiz - Week 04 Day 05 (Week Summary / Domain 4)

- 문항 수: 10 (Day05 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

이번 달 비용이 갑자기 2배가 됐다. “일단 뭔가를 끄자”는 제안이 나오지만, 그건 장애로 돌아올 가능성이 높다. 먼저 “어디서(어느 서비스/리전/계정/태그) 늘었는지”를 분해해 드라이버를 찾아야 한다.  
가장 적절한 도구는?
A. Budgets  
B. Cost Explorer  
C. GuardDuty  
D. Route 53  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 최적화는 드라이버 파악(분해/그룹핑)에서 시작한다.
- 소거법
  - A (근접 오답): 임계치 알림(센서)에는 좋지만 원인 분석 도구는 아니다.
  - D (명확히 틀림): DNS다.
  - C (명확히 틀림): 보안 탐지다.
- 한 줄 규칙: “원인 분석/그룹핑”이면 **Cost Explorer**.
- 태그: `pillar:cost-optimization` `services:CostExplorer` `week:04` `day:05`

</details>

---

## Q2.

팀은 비용 문제를 항상 월말에 뒤늦게 알았다. 운영 인력이 적어 “빠르게 감지해서 당일에 대응”하는 게 우선이다. 예산 80%/100% 같은 임계치에 도달하면 이메일/슬랙으로 경고를 받고 싶다.  
가장 적절한 도구는?
A. CloudFront  
B. Cost Explorer  
C. Budgets  
D. S3 Lifecycle  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 사전 감지/알림으로 대응 루틴을 만드는 게 운영 우수성이다. Budgets는 알림(센서) 도구다.
- 소거법
  - B (근접 오답): 분석 도구다.
  - A (명확히 틀림): CDN이다.
  - D (근접 오답): 장기 비용 자동화엔 좋지만 “지금 초과 감지” 도구가 아니다.
- 한 줄 규칙: “임계치/초과 알림”이면 **Budgets**.
- 태그: `pillar:operational-excellence` `services:Budgets` `week:04` `day:05`

</details>

---

## Q3. (복수정답: 2개)

팀은 두 가지를 모두 원한다.  
1) 비용이 급증하면 “당일에” 알림을 받고 싶다  
2) 알림이 오면 “어느 서비스/어느 팀(태그)에서 늘었는지” 원인을 분해하고 싶다  
가장 자연스러운 조합 2개를 고르시오.
A. Cost Explorer  
B. EFS  
C. Budgets  
D. IAM Identity Center  
E. Route 53  
<details>
<summary>정답/해설</summary>

- 정답: A, C
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: Budgets=알림, Cost Explorer=분석으로 역할이 분리된다.
- 소거법
  - E (명확히 틀림): DNS다.
  - D (근접 오답): 인증/권한 통합이지 비용 알림/분석 도구가 아니다.
  - B (명확히 틀림): 파일 스토리지다.
- 한 줄 규칙: “알림=Budgets, 분석=Cost Explorer”.
- 태그: `pillar:cost-optimization` `services:Budgets,CostExplorer` `week:04` `day:05`

</details>

---

## Q4.

팀이 4개로 늘면서 “팀별 비용(차지백/쇼백)” 요구가 생겼다. 계정은 하나라서 추측으로는 한계다.  
가장 먼저 해야 할 일로 가장 자연스러운 것은?
A. 모든 데이터를 Glacier Deep Archive로 옮긴다  
B. 모두 Spot으로 바꾼다  
C. NAT Gateway를 무조건 삭제한다  
D. 비용 할당 태그를 표준화/활성화하고 Cost Explorer에서 태그로 Group by 가능하게 만든다  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: “최적화” 이전에 “가시성”이 있어야 팀별로 근거 있는 논의가 된다.
- 소거법
  - B (근접 오답): 중단 허용 신호가 없으면 신뢰성을 깨기 쉽다.
  - A (근접 오답): 복구/접근 요구를 깨기 쉽다.
  - C (근접 오답): NAT가 드라이버일 수는 있지만 “무조건”은 위험하다.
- 한 줄 규칙: “팀별 비용”은 **태그(또는 계정 구조)**부터.
- 태그: `pillar:cost-optimization` `services:CostAllocationTags,CostExplorer` `week:04` `day:05`

</details>

---

## Q5.

서비스가 안정됐고 “1~3년 사용량이 예측 가능(steady state)”하다는 문장이 강하다. EC2 비용이 꾸준히 크다.  
가장 자연스러운 할인 모델 후보는?
A. Spot  
B. Savings Plans 또는 Reserved Instances  
C. On-Demand만 유지  
D. S3 Intelligent-Tiering  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: steady state는 장기 커밋(RI/SP)의 근거다.
- 소거법
  - A (근접 오답): 중단 허용 신호가 있어야 한다.
  - C (근접 오답): 절감 폭이 제한적일 수 있다.
  - D (명확히 틀림): S3 기능이다.
- 한 줄 규칙: “예측 가능”이면 **RI/SP**.
- 태그: `pillar:cost-optimization` `services:EC2` `week:04` `day:05`

</details>

---

## Q6.

배치 작업이 밤에만 돌고 중단돼도 재시도 가능하다. “fault-tolerant/중단 허용” 신호가 있다.  
가장 자연스러운 선택은?
A. 무조건 On-Demand  
B. CloudFront  
C. Spot  
D. Reserved Instances  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 중단 허용 워크로드는 Spot이 큰 절감 레버가 된다.
- 소거법
  - D (근접 오답): steady state 신호가 더 강할 때 후보.
  - A (근접 오답): 유연하지만 절감 폭이 약하다.
  - B (명확히 틀림): CDN이다.
- 한 줄 규칙: “중단 허용 배치”면 **Spot**.
- 태그: `pillar:cost-optimization` `services:EC2` `week:04` `day:05`

</details>

---

## Q7. (복수정답: 2개)

업무 시스템이라 “업무시간 외에는 트래픽이 거의 없다”는 신호가 있다. 목표는 요구사항을 깨지 않으면서 큰 절감을 만드는 것이다.  
가장 자연스러운 조치 2개를 고르시오.
A. S3 버킷을 퍼블릭으로 연다  
B. 루트 사용자로만 운영 작업을 수행한다  
C. CloudWatch 지표로 실제 사용량을 측정해 right sizing(과한 스펙)을 조정한다  
D. Auto Scaling scheduled action으로 야간(비피크)에 desired를 0으로 줄인다  
E. 모든 인스턴스를 가장 큰 타입으로 고정한다  
<details>
<summary>정답/해설</summary>

- 정답: C, D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 큰 절감은 비피크 축소(야간 0)에서 자주 나온다. 동시에 측정 기반 right sizing으로 과한 스펙을 줄인다.
- 소거법
  - A (명확히 틀림): 보안/비용 모두 악화될 수 있다.
  - B (명확히 틀림): 운영/보안 원칙 위반이다.
  - E (명확히 틀림): 비용 낭비다.
- 한 줄 규칙: 절감 레버리지는 **비피크 축소 + 측정 기반 right sizing**.
- 태그: `pillar:cost-optimization` `services:AutoScaling,CloudWatch,EC2` `week:04` `day:05`

</details>

---

## Q8.

“가끔 접근하지만, 조회 시 즉시 복구가 필요”하다는 문장이 있다. “모두 Glacier로 옮기자”는 의견은 위험하다.  
가장 자연스러운 클래스 후보는?
A. S3 Glacier Deep Archive  
B. Route 53 Latency  
C. S3 Standard-IA  
D. EBS io2  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용을 줄이되 복구 요구를 깨면 오답이다. “가끔 접근 + 즉시”는 IA 신호다.
- 소거법
  - A (근접 오답): 느린 복구 허용 신호가 강할 때 후보.
  - D (명확히 틀림): 블록 스토리지다.
  - B (명확히 틀림): DNS다.
- 한 줄 규칙: 클래스는 “빈도+복구 요구”로 고른다.
- 태그: `pillar:cost-optimization` `services:S3` `week:04` `day:05`

</details>

---

## Q9.

프라이빗 서브넷 워커가 S3를 자주 호출한다. NAT Gateway 경유로 비용이 꾸준히 올라간다. 인터넷 경유도 줄이고 싶다.  
가장 자연스러운 선택은?
A. S3 Gateway VPC Endpoint  
B. Route 53 Failover  
C. GuardDuty  
D. CloudFront  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: NAT 비용 드라이버를 사설 경로(endpoint)로 줄이는 대표 패턴이다.
- 소거법
  - D (근접 오답): 다운로드/정적 콘텐츠 비용 절감 레버이지 NAT 경유 비용 제거는 아니다.
  - B (명확히 틀림): DNS다.
  - C (명확히 틀림): 보안 탐지다.
- 한 줄 규칙: “프라이빗 → S3 자주 호출 + NAT 비용”이면 **Gateway Endpoint**.
- 태그: `pillar:cost-optimization` `services:VPCEndpoints,S3,NATGateway` `week:04` `day:05`

</details>

---

## Q10.

글로벌 다운로드가 많아 오리진(S3/ALB) 전송량/요청 수 비용이 커졌다. 캐시 가능한 정적 콘텐츠가 대부분이다.  
가장 자연스러운 선택은?
A. EFS  
B. Global Accelerator  
C. DynamoDB PITR  
D. CloudFront  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 캐시 hit로 오리진 전송/요청을 줄이면 비용과 성능이 같이 좋아질 수 있다.
- 소거법
  - B (근접 오답): GA는 경로/고정 IP 축이다.
  - C (명확히 틀림): DB 복구 기능이다.
  - A (명확히 틀림): 파일 스토리지다.
- 한 줄 규칙: “글로벌 + 정적 + 전송/요청 비용”이면 **CloudFront**.
- 태그: `pillar:cost-optimization` `services:CloudFront` `week:04` `day:05`

</details>

---

