# 03-quiz - Week 01 Day 04 (SG vs NACL / VPC Endpoints / PrivateLink)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

백엔드를 프라이빗 서브넷에 올린 뒤 연결이 끊겼다. 개발자는 Security Group 인바운드를 열고 다시 테스트했지만 여전히 타임아웃이다. “NACL도 열어야 한다”는 말이 나오지만, 무엇을 어디까지 열어야 하는지 감이 없다. 보안팀은 “그냥 다 열어두기”는 안 된다고 한다.  
이 상황에서 가장 가능성이 큰 원인/진단 방향은?
A. NACL은 무상태라 인바운드만 열면 리턴 트래픽은 자동으로 허용된다  
B. NACL은 무상태라 리턴 트래픽(에페메랄 포트 등)을 포함해 아웃바운드 규칙도 함께 고려해야 한다  
C. Route 53 레코드를 바꾸면 네트워크 연결 문제가 해결된다  
D. Security Group은 Deny 규칙을 넣을 수 있으니 Deny를 제거하면 된다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 신뢰성은 “예상 가능한 네트워크 동작”을 만들고 장애를 빠르게 줄이는 게 중요하다. NACL은 **무상태(stateless)**라 리턴 트래픽까지 명시적으로 허용하지 않으면 타임아웃이 날 수 있다.
- 소거법
  - A (근접 오답): SG의 특징(stateful)을 NACL에 착각한 선택지다.
  - D (명확히 틀림): SG는 allow-only(deny 규칙 없음)다.
  - C (명확히 틀림): DNS는 보안 그룹/NACL 차단을 해결하지 못한다.
- 한 줄 규칙: “인바운드는 열었는데 타임아웃”이면 **NACL 리턴 트래픽(무상태)**를 의심한다.
- 태그: `pillar:reliability` `services:SecurityGroup,NACL` `week:01` `day:04`

</details>

---

## Q2.

장애 회고에서 논쟁이 났다. “인바운드만 열었는데 왜 리턴 트래픽이 막히지?”라는 질문에 누군가는 “보안 그룹은 원래 그렇게 동작한다”고 하고, 또 다른 사람은 “아니, NACL은 다르다”고 말한다.  
팀이 같은 실수를 반복하지 않도록, 두 컴포넌트의 동작 차이를 한 문장으로 정확히 정리해 문서에 넣으려 한다. 어떤 설명이 맞나?
A. SG는 allow+deny를 모두 지원하고, NACL은 allow만 지원한다  
B. SG는 서브넷 단위, NACL은 인스턴스(ENI) 단위다  
C. SG는 “누가 API를 호출했는지”를 기록한다  
D. SG는 stateful, NACL은 stateless다  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: 네트워크 경계에서 최소 노출을 만들려면 “무엇이 어디에 붙고, 어떤 방식으로 평가되는지”를 정확히 구분해야 한다. 시험도 이 혼동을 노린다.
- 소거법
  - B (명확히 틀림): 범위가 반대다(SG=ENI/인스턴스, NACL=서브넷).
  - A (근접 오답): 반대다(SG=allow-only, NACL=allow+deny).
  - C (명확히 틀림): 행위 기록은 CloudTrail 축이다.
- 한 줄 규칙: **SG=인스턴스/상태 저장, NACL=서브넷/무상태**.
- 태그: `pillar:security` `services:SecurityGroup,NACL` `week:01` `day:04`

</details>

---

## Q3.

보안팀이 “프라이빗 서브넷 워크로드는 인터넷으로 나가면 안 된다”고 요구한다. 하지만 서비스는 S3에서 파일을 읽고 써야 한다. NAT Gateway를 달면 동작은 되지만, 매달 NAT 비용이 꾸준히 발생하고 “인터넷 경유” 자체가 찜찜하다.  
요구사항(사설 경로 + NAT 비용 최소화)에 가장 자연스러운 선택은?
A. S3 Gateway VPC Endpoint를 사용해 라우팅 테이블에 사설 경로를 만든다  
B. CloudFront를 붙이면 VPC에서 S3로 사설로 연결된다  
C. S3 버킷을 퍼블릭으로 열고, 프라이빗 서브넷은 그대로 둔다  
D. NAT Gateway를 계속 사용한다(사설 경로 요구는 무시)  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: NAT는 편하지만 지속 비용이 발생한다. S3는 Gateway endpoint로 사설 경로를 만들 수 있어 NAT 비용을 줄이면서도 요구사항(인터넷 없이)을 만족한다.
- 소거법
  - D (근접 오답): 동작은 하지만 “비용 최소화/사설 경로” 요구를 만족하지 못한다.
  - C (명확히 틀림): 인증/접근 제어 관점에서 요구사항과 반대다.
  - B (명확히 틀림): CloudFront는 엣지 캐시/전송 최적화이지 VPC 사설 경로 대체가 아니다.
- 한 줄 규칙: “프라이빗 서브넷에서 S3, NAT 비용 최소화”면 **S3 Gateway Endpoint**.
- 태그: `pillar:cost-optimization` `services:VPCEndpoints,S3` `week:01` `day:04`

</details>

---

## Q4. (복수정답: 2개)

프라이빗 서브넷의 워크로드가 **S3와 DynamoDB** 모두에 인터넷 없이 접근해야 한다. NAT 비용도 최소화해야 한다.  
가장 자연스러운 구성 2개를 고르시오.
A. CloudFront 배포 생성  
B. S3 Gateway endpoint 추가  
C. DynamoDB Gateway endpoint 추가  
D. Internet Gateway 추가  
E. Secrets Manager Interface endpoint 추가  
<details>
<summary>정답/해설</summary>

- 정답: B, C
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: S3/DynamoDB는 Gateway endpoint로 라우팅 테이블 기반 사설 경로를 만들 수 있어 NAT 비용을 줄이는 대표 패턴이다.
- 소거법
  - E (근접 오답): Interface endpoint(PrivateLink) 자체는 맞는 개념이지만, 문제의 “목적지”가 S3/DDB다.
  - A (명확히 틀림): 캐싱/전송 계층으로 사설 경로 요구를 직접 해결하지 못한다.
  - D (명확히 틀림): 인터넷 경유를 허용하는 방향으로 요구사항과 반대다.
- 한 줄 규칙: **S3/DDB = Gateway endpoint**를 먼저 떠올린다.
- 태그: `pillar:cost-optimization` `services:VPCEndpoints,S3,DynamoDB` `week:01` `day:04`

</details>

---

## Q5.

이번엔 S3가 아니라 **Secrets Manager** 같은 “대부분의 AWS 서비스”에 프라이빗하게 접근해야 한다. 인터넷/NAT 경유는 금지이고, VPC 안에 사설 엔드포인트(ENI)가 생기는 형태가 필요하다.  
가장 자연스러운 선택은?
A. Interface VPC Endpoint(PrivateLink)를 만든다  
B. S3 버킷 정책을 바꾼다  
C. NACL을 모두 Allow로 바꾼다  
D. S3 Gateway endpoint를 만든다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 보안 원칙 (Security)
- 왜 이게 원칙에 맞나: “사설 경로/인터넷 없이” 요구는 VPC Endpoints가 축이다. S3/DDB 외 대부분 서비스는 **Interface endpoint(PrivateLink)** 형태로 VPC 안 ENI 기반 엔드포인트를 만든다.
- 소거법
  - D (근접 오답): Gateway endpoint는 S3/DynamoDB에 해당한다. 대상 서비스가 다르다.
  - C (명확히 틀림): 네트워크를 더 열어도 “사설 AWS 서비스 접근”은 해결되지 않는다.
  - B (명확히 틀림): 버킷 정책은 S3 리소스 접근 제어이고, Secrets Manager 접근 경로 문제와 축이 다르다.
- 한 줄 규칙: “S3/DDB 외 사설 접근”이면 **Interface endpoint(PrivateLink)**.
- 태그: `pillar:security` `services:VPCEndpoints,PrivateLink` `week:01` `day:04`

</details>

---

