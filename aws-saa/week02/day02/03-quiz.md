# 03-quiz - Week 02 Day 02 (ALB vs NLB / Auto Scaling)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

요구사항에 이런 문장이 있다.  
“`/api`는 API 타깃 그룹으로, `/static`은 정적 컨텐츠 타깃 그룹으로 보내고 싶다. 또한 WAF 연동도 고려해야 한다.”  
이 문장을 가장 자연스럽게 만족시키는 로드 밸런서 선택은?
A. NLB  
B. Route 53 Simple routing만 사용한다  
C. Gateway Load Balancer  
D. ALB  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 요구사항이 L7(HTTP host/path, 규칙 기반 라우팅)이다. ALB는 요청 내용을 해석해 라우팅 규칙을 적용할 수 있다.
- 소거법
  - A (근접 오답): NLB는 L4(TCP/UDP) 축이 강하고 L7 라우팅 규칙이 핵심 요구일 때는 부자연스럽다.
  - C (명확히 틀림): GWLB는 보안 어플라이언스 삽입(개념) 축이다.
  - B (명확히 틀림): DNS만으로 L7 라우팅 규칙을 구현할 수 없다.
- 한 줄 규칙: “host/path/WAF” 신호가 보이면 **ALB**.
- 태그: `pillar:performance-efficiency` `services:ALB,ELB` `week:02` `day:02`

</details>

---

## Q2.

요구사항에 이런 문장이 있다.  
“TCP 기반 연결이 핵심이고, 초고성능이 필요하다. 또한 일부 고객은 고정 IP를 요구한다.”  
이 문장을 가장 자연스럽게 만족시키는 선택은?
A. NLB  
B. CloudFront  
C. ALB  
D. S3 Static website hosting  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: TCP/UDP, 고성능, (케이스에 따라) 정적 IP 같은 신호는 L4 축이 강하고 NLB가 자연스럽다.
- 소거법
  - C (근접 오답): HTTP 규칙이 핵심이 아니고, L4 신호가 더 강하다.
  - B (명확히 틀림): 엣지 캐시/전송 최적화 서비스다.
  - D (명확히 틀림): 로드밸런싱 요구를 만족하지 못한다.
- 한 줄 규칙: “TCP/정적 IP/초고성능”이면 **NLB**.
- 태그: `pillar:performance-efficiency` `services:NLB,ELB` `week:02` `day:02`

</details>

---

## Q3.

트래픽이 몰릴 때마다 운영자가 수동으로 인스턴스를 늘렸다가 이벤트가 끝나면 줄이고 있었다. 더 큰 문제는 인스턴스 한 대가 죽으면 일부 사용자만 계속 오류를 겪는다는 것이다. “운영자가 새벽에 깨서 재기동”하는 패턴을 없애고, 실패한 인스턴스를 자동으로 제외/교체(자가 치유)하고 싶다.  
가장 자연스러운 설계는?
A. Route 53 Weighted로 트래픽을 분배하면 인스턴스가 자동으로 교체된다  
B. 단일 EC2에만 큰 인스턴스 타입으로 스케일업한다  
C. S3 버킷 버저닝을 켠다  
D. Auto Scaling Group(ASG) + (필요 시) ELB health check로 실패 인스턴스를 자동 교체한다  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 신뢰성은 장애가 나도 자동으로 복구되는 메커니즘(자가 치유)이 핵심이다. ASG는 헬스체크 실패를 기준으로 제외/교체 흐름을 만들 수 있다.
- 소거법
  - B (근접 오답): 성능은 좋아질 수 있어도 “죽었을 때 자동 교체”를 해결하지 못한다.
  - A (명확히 틀림): DNS 라우팅은 인스턴스 교체 엔진이 아니다.
  - C (명확히 틀림): 스토리지 기능이다.
- 한 줄 규칙: “자동 복구/교체” 신호가 보이면 **ASG + health check**.
- 태그: `pillar:reliability` `services:AutoScaling,ELB` `week:02` `day:02`

</details>

---

## Q4.

서비스는 평상시에는 트래픽이 낮지만, 특정 시간대/이벤트에만 트래픽이 급증한다. 요구사항은 “평상시엔 비용을 아끼고, 피크에는 자동으로 늘어나야 한다”다. 또한 인스턴스 구성은 표준화(이미지/보안그룹/유저데이터)돼야 한다.  
이 요구를 가장 자연스럽게 만족시키는 방향은?
A. Launch template로 표준 구성을 만들고, ASG에 min/desired/max 및 스케일 정책을 설정한다  
B. NACL을 모두 Allow로 바꾼다  
C. 모든 트래픽을 하나의 인스턴스로 모아 캐시만 늘린다  
D. 매번 운영자가 콘솔에서 수동으로 늘리고 줄인다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용 최적화는 “필요할 때만 자원 사용”이 핵심이다. ASG는 필요한 순간에만 확장하고, 평상시엔 줄이는 자동화를 제공한다.
- 소거법
  - D (근접 오답): 동작은 하지만 운영 인력 의존/실수/지연으로 비용과 리스크가 커진다.
  - C (명확히 틀림): 단일 인스턴스 병목/단일 장애점이 된다.
  - B (명확히 틀림): 스케일/비용 요구를 해결하지 못한다.
- 한 줄 규칙: “피크만 자동 확장”이면 **ASG(표준 구성 + 스케일 정책)**.
- 태그: `pillar:cost-optimization` `services:AutoScaling` `week:02` `day:02`

</details>

---

## Q5. (복수정답: 2개)

고객 사례에서 요구는 동시에 두 가지다.  
1) “HTTP 요청을 경로(path) 기반으로 서로 다른 타깃 그룹으로 라우팅”  
2) “인스턴스가 죽으면 자동으로 제외/교체(자가 치유)”  
이 요구를 가장 자연스럽게 만족시키는 구성 2개를 고르시오.
A. Route 53 Simple routing  
B. S3 Glacier  
C. ALB  
D. IAM Permissions boundary  
E. Auto Scaling Group(ASG)  
<details>
<summary>정답/해설</summary>

- 정답: C, E
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: L7 라우팅은 ALB, 자가 치유는 ASG(헬스체크 기반 교체)로 풀린다. 둘을 분리해서 조합하는 게 정답 패턴이다.
- 소거법
  - A (근접 오답): DNS는 라우팅 “대상 선택”은 가능하지만 L7 경로 규칙/자가 치유를 제공하지 않는다.
  - B (명확히 틀림): 저장 클래스다.
  - D (명확히 틀림): IAM 권한 상한선이다.
- 한 줄 규칙: “HTTP 규칙=ALB, 자동 교체=ASG”로 조합한다.
- 태그: `pillar:reliability` `services:ALB,AutoScaling` `week:02` `day:02`

</details>

---

