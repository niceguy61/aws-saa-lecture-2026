# 03-quiz - Week 03 Day 02 (CloudFront / Global Accelerator)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

대규모 캠페인 시작 후 페이지 로딩이 느리다는 문의가 폭증한다. 서버 CPU는 여유가 있는데도 해외 사용자일수록 이미지/JS가 늦게 내려오고, S3 오리진 요청 수가 급격히 늘면서 비용도 튄다. “서버를 더 늘리면 되지 않나?”라는 제안이 나오지만, 정적 콘텐츠는 서버 증설이 핵심이 아니다.  
이 요구(글로벌 지연 감소 + 오리진 부하/비용 감소)에 가장 자연스러운 선택은?
A. CloudFront를 붙여 엣지 캐시로 히트율을 올리고 오리진 호출을 줄인다  
B. S3 버킷을 퍼블릭으로 열어 접근을 단순화한다  
C. Global Accelerator를 붙여 정적 콘텐츠를 캐시한다  
D. Route 53 Weighted 라우팅만 설정한다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 정적 콘텐츠 지연/오리진 부하는 CDN 캐시로 해결하는 게 축이다. CloudFront는 엣지에서 캐시 히트 시 RTT와 오리진 호출(비용)을 같이 줄인다.
- 소거법
  - C (근접 오답): GA는 캐시가 아니라 경로 최적화/고정 IP 축이다.
  - D (근접 오답): DNS 분배는 가능하지만 캐시로 오리진 부하를 줄이진 못한다.
  - B (명확히 틀림): 보안 요구(퍼블릭 금지)와도 충돌할 수 있다.
- 한 줄 규칙: “글로벌 정적 콘텐츠/오리진 부하”면 **CloudFront**.
- 태그: `pillar:performance-efficiency` `services:CloudFront,S3` `week:03` `day:02`

</details>

---

## Q2.

CloudFront를 붙였는데 캐시 히트율이 생각보다 안 나온다. 설정을 보니 쿼리 스트링/쿠키/헤더를 무조건 캐시 키에 포함하도록 해두었다. 개인화 응답의 정확도는 올라가지만, 객체 변종이 폭발하면서 히트율이 떨어지고 오리진 부하가 다시 늘었다.  
이 문제를 완화하기 위한 “캐시 키 설계” 관점에서 가장 자연스러운 접근은?
A. invalidation을 모든 배포마다 전 객체에 대해 남발한다  
B. 캐시 키는 무조건 크게 잡아야 히트율이 올라간다  
C. CloudFront 대신 Global Accelerator로 바꿔서 캐시한다  
D. 개인화에 꼭 필요한 요소만 캐시 키에 포함하고, 공통 정적 리소스 위주로 캐시 범위를 설계한다  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 불필요한 변종은 히트율을 떨어뜨려 오리진 호출과 비용을 키운다. “정확도 vs 히트율”을 분리해 필요한 키만 포함하는 게 비용/성능에 유리하다.
- 소거법
  - B (명확히 틀림): 캐시 키가 커질수록 변종이 늘어 히트율이 떨어질 수 있다.
  - A (근접 오답): 즉시 반영은 되지만 비용/운영 부담이 커지고 근본 원인(키 폭발)을 해결하지 못한다.
  - C (명확히 틀림): GA는 캐시가 아니라 경로 최적화 서비스다.
- 한 줄 규칙: CloudFront는 **TTL(신선도) + 키(히트율) + 무효화(비용)**를 같이 설계한다.
- 태그: `pillar:cost-optimization` `services:CloudFront` `week:03` `day:02`

</details>

---

## Q3.

실시간 기능이 있는 서비스(TCP/UDP 기반)가 해외 사용자에게서 지연이 들쭉날쭉하다. ISP/인터넷 구간이 꼬이는 날에는 지연이 갑자기 늘어난다. 캐시할 성격의 트래픽이 아니라 CDN만으로는 체감이 좋아지지 않는다. 게다가 고객사가 “고정 IP 화이트리스트”를 요구한다.  
이 요구(경로 최적화 + 고정 IP)에 가장 자연스러운 선택은?
A. CloudFront  
B. AWS Config  
C. Global Accelerator  
D. S3 Replication  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: GA는 Anycast 고정 IP + AWS 백본 경로 최적화로 TCP/UDP 트래픽의 네트워크 경로 변동 영향을 줄이고, 고정 IP 요구도 만족한다.
- 소거법
  - A (근접 오답): CloudFront는 캐시 축이다. 캐시 불가 트래픽/고정 IP 요구엔 결이 다르다.
  - D (명확히 틀림): 데이터 복제/DR 축이다.
  - B (명확히 틀림): 준수/상태 평가 서비스다.
- 한 줄 규칙: “고정 IP + TCP/UDP + 경로 최적화”면 **Global Accelerator**.
- 태그: `pillar:performance-efficiency` `services:GlobalAccelerator` `week:03` `day:02`

</details>

---

## Q4.

팀이 같은 주제로 두 번 연속 헷갈렸다.  
- 케이스 1: “정적 파일(이미지/JS)을 전 세계에 빠르게 내려주고, 오리진 요청/비용도 줄이자.”  
- 케이스 2: “캐시가 안 되는 TCP/UDP 트래픽인데, 네트워크 경로가 들쭉날쭉하고 고객사가 고정 IP 화이트리스트를 요구한다.”  
두 케이스를 같은 해법으로 뭉치지 않기 위해, 서비스 선택을 가장 정확히 정리한 문장은?
A. “정적 콘텐츠 캐시” 요구에는 Global Accelerator가 가장 자연스럽다  
B. “캐시”는 CloudFront, “경로/고정 IP/Anycast”는 Global Accelerator로 축이 다르다  
C. CloudFront와 Global Accelerator는 동일 서비스의 다른 이름이다  
D. “고정 IP 화이트리스트” 요구에는 CloudFront가 가장 자연스럽다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 요구사항 신호를 올바르게 분류(캐시 vs 경로)해야 운영/설계가 꼬이지 않는다. 시험도 이 혼동을 노린다.
- 소거법
  - A (명확히 틀림): GA는 캐시가 아니다.
  - D (근접 오답): CloudFront도 엣지 IP는 있지만, “고정 IP” 요구는 GA 쪽 신호가 더 강하다.
  - C (명확히 틀림): 목적/계층이 다르다.
- 한 줄 규칙: “캐시”와 “경로 최적화”는 같은 문제처럼 보여도 답이 다르다.
- 태그: `pillar:operational-excellence` `services:CloudFront,GlobalAccelerator` `week:03` `day:02`

</details>

---

## Q5. (복수정답: 2개)

고객 사례처럼, 팀이 CloudFront와 Global Accelerator를 자꾸 섞어 말한다. PM은 “정적 콘텐츠 지연/오리진 비용” 이슈와 “TCP/UDP 지연 변동 + 고정 IP” 요구를 한꺼번에 던졌고, 설계가 뒤죽박죽이 됐다.  
요구사항을 정확히 해석하고 팀에 설명하기 위해, 아래 보기 중 ‘옳은 설명’ 2개를 고르시오.
A. Global Accelerator는 캐시 키/TTL/무효화 설정이 핵심이다  
B. 둘 다 “S3 버전 관리” 기능이다  
C. Global Accelerator는 Anycast 고정 IP와 AWS 백본 경로로 TCP/UDP 경로를 최적화한다(캐시 서비스 아님)  
D. CloudFront는 고정 IP 화이트리스트 요구에만 쓰는 서비스다  
E. CloudFront는 정적/캐시 가능한 콘텐츠에서 엣지 캐시로 RTT와 오리진 부하를 줄일 수 있다  
<details>
<summary>정답/해설</summary>

- 정답: C, E
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 서비스의 “핵심 조절점”을 정확히 아는 게 소거의 핵심이다(CloudFront=TTL/키/무효화, GA=경로/고정 IP/헬스 전환).
- 소거법
  - A (명확히 틀림): TTL/키/무효화는 CloudFront 축이다.
  - D (근접 오답): CloudFront도 IP 요구가 힌트로 나올 수는 있지만, 본질은 캐시다.
  - B (명확히 틀림): S3 기능이다.
- 한 줄 규칙: “정적=CloudFront, 경로/고정 IP=GA”로 먼저 분리한다.
- 태그: `pillar:operational-excellence` `services:CloudFront,GlobalAccelerator` `week:03` `day:02`

</details>

---

