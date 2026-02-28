# 03-quiz - Week 04 Day 04 (VPC Endpoints vs NAT / CloudFront Cost)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

애플리케이션 서버는 프라이빗 서브넷에 있고, 매일 S3에서 설정 파일과 릴리즈 아티팩트를 “자주/대량”으로 가져온다. NAT Gateway를 통해 나가면 기능은 되지만, 트래픽이 쌓이면서 NAT 비용이 꾸준히 올라간다. 보안팀은 인터넷 경유도 줄이고 싶다.  
요구사항(프라이빗 + S3 자주 호출 + 비용)을 가장 자연스럽게 만족하는 선택은?
A. Route 53 Failover를 설정해 비용을 줄인다  
B. S3 Gateway VPC Endpoint를 만들고 라우팅 테이블에 연결해 NAT 경유를 피한다  
C. NAT Gateway를 더 큰 사이즈로 바꾸면 비용이 줄어든다  
D. S3 버킷을 퍼블릭으로 열어 NAT 없이 접근한다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: NAT는 편하지만 비용 드라이버가 될 수 있다. S3는 Gateway endpoint로 사설 경로를 만들 수 있어 NAT/인터넷 경유 비용과 보안 노출을 함께 줄인다.
- 소거법
  - C (명확히 틀림): NAT 비용은 “사이즈 업”으로 자동 절감되지 않는다.
  - D (명확히 틀림): 보안 요구와 정반대다.
  - A (명확히 틀림): DNS는 NAT 비용 드라이버를 제거하지 못한다.
- 한 줄 규칙: “프라이빗 → S3 자주 호출 + NAT 비용”이면 **S3 Gateway Endpoint**.
- 태그: `pillar:cost-optimization` `services:VPCEndpoints,NATGateway,S3` `week:04` `day:04`

</details>

---

## Q2.

보안팀과 재무팀이 같이 리뷰한다. “프라이빗 서브넷이면 NAT로 밖에 나가면 되지”라는 의견이 나왔지만, 실제로는 NAT가 비용 드라이버가 될 수 있고 ‘인터넷 경유’ 자체를 줄이라는 요구도 있다.  
이 상황을 비용/보안 관점에서 가장 올바르게 정리한 설명은?
A. 프라이빗이면 무조건 NAT Gateway가 정답이다(엔드포인트는 필요 없다)  
B. NAT는 “일단 되게” 하지만 비용 드라이버가 될 수 있고, 대상 서비스가 지원하면 VPC Endpoints로 사설 경로를 만들 수 있다  
C. VPC Endpoints는 CloudFront의 다른 이름이다  
D. VPC Endpoints는 인터넷을 경유하는 방식이다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영/비용은 “기본값을 무엇으로 가져갈지”에서 갈린다. 프라이빗 요구는 NAT 강제가 아니라 인터넷 경유를 줄이라는 뜻이고, endpoints가 가능한 대상(S3/DDB 등)은 비용/보안 모두 유리하다.
- 소거법
  - A (근접 오답): 동작은 되지만 시험/실무에서 비용 함정으로 자주 나온다.
  - D (명확히 틀림): endpoints는 사설 경로를 만드는 개념이다.
  - C (명확히 틀림): 목적/계층이 다르다.
- 한 줄 규칙: NAT는 기본값이 될 수 있지만, “비용/보안 신호”가 붙으면 endpoints가 후보로 올라온다.
- 태그: `pillar:operational-excellence` `services:VPCEndpoints,NATGateway` `week:04` `day:04`

</details>

---

## Q3.

다운로드 기능이 인기라서 트래픽이 급증했고, 오리진(S3/ALB)은 버티지만 전송량/요청 수가 올라가면서 비용이 함께 올라간다. “같은 파일을 전 세계에서 반복해서 받는” 정적/캐시 가능한 콘텐츠가 대부분이다.  
전송/오리진 비용을 줄이는 레버로 가장 자연스러운 선택은?
A. CloudFront를 붙여 캐시 hit로 오리진 호출/전송을 줄인다  
B. S3 버킷을 퍼블릭으로 열어 인증을 제거한다  
C. 모든 사용자를 단일 리전으로 강제한다  
D. Global Accelerator를 붙여 정적 파일을 캐시한다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 캐시 가능한 정적 다운로드는 엣지 캐시로 오리진 호출/전송을 줄이면 비용과 성능이 같이 좋아질 수 있다.
- 소거법
  - D (근접 오답): GA는 캐시가 아니라 경로 최적화/고정 IP 축이다.
  - C (근접 오답): 비용은 줄 수 있어도 사용자 경험/요구사항을 깨기 쉽다.
  - B (명확히 틀림): 보안 요구와 충돌할 수 있다.
- 한 줄 규칙: “글로벌 + 정적 + 전송 비용”이면 **CloudFront**.
- 태그: `pillar:cost-optimization` `services:CloudFront` `week:04` `day:04`

</details>

---

## Q4.

CloudFront를 붙였는데 기대만큼 비용/성능 효과가 없다. 설정을 보니 쿼리 스트링/쿠키/헤더를 무조건 캐시 키에 포함해 변종이 너무 많다. 캐시 hit가 잘 안 나고 오리진 호출이 그대로다.  
가장 자연스러운 개선 방향은?
A. NAT Gateway를 추가로 만든다  
B. 개인화에 꼭 필요한 요소만 캐시 키에 포함하고, 공통 정적 리소스 위주로 캐시 범위를 설계한다  
C. invalidation을 모든 배포마다 전 객체에 대해 남발한다  
D. 캐시 키는 무조건 크게 잡아야 hit가 올라간다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 캐시 효과는 hit율에 달려 있고, 불필요한 변종은 hit율을 깨서 오리진 비용을 남긴다. 키 설계로 “히트율”을 회복해야 한다.
- 소거법
  - D (명확히 틀림): 키가 커질수록 변종이 늘어 hit율이 떨어질 수 있다.
  - C (근접 오답): 즉시 반영은 되지만 비용/운영 부담이 커지고 근본 원인(키 폭발)을 해결하지 못한다.
  - A (명확히 틀림): NAT는 CloudFront 캐시 hit율과 무관하다.
- 한 줄 규칙: CloudFront 비용/성능은 **TTL/키/무효화** 설계에서 갈린다.
- 태그: `pillar:cost-optimization` `services:CloudFront` `week:04` `day:04`

</details>

---

## Q5. (복수정답: 2개)

팀이 이번 분기에 두 가지 비용 드라이버를 동시에 줄이려 한다.  
1) 프라이빗 서브넷 워커가 S3를 자주 호출해 NAT 비용이 크다  
2) 글로벌 다운로드가 많아 오리진 전송/요청 비용이 크다  
가장 자연스러운 선택 2개를 고르시오.
A. CloudFront  
B. CloudTrail Trail  
C. IAM Permissions boundary  
D. Route 53 Simple routing  
E. S3 Gateway VPC Endpoint  
<details>
<summary>정답/해설</summary>

- 정답: A, E
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: NAT 비용 드라이버는 S3 Gateway endpoint로 경유를 줄이고, 글로벌 다운로드 비용은 CloudFront 캐시 hit로 오리진 전송/요청을 줄인다.
- 소거법
  - D (근접 오답): 라우팅은 가능하지만 NAT/전송 비용 드라이버를 직접 제거하진 못한다.
  - C (명확히 틀림): 보안 상한선이다.
  - B (근접 오답): 감사엔 유용하지만 비용 드라이버 제거 도구는 아니다.
- 한 줄 규칙: 비용은 “드라이버별 레버”를 고르면 답이 선명해진다.
- 태그: `pillar:cost-optimization` `services:VPCEndpoints,CloudFront,S3,NATGateway` `week:04` `day:04`

</details>

---

