# 03-quiz - Week 03 Day 03 (EBS Performance / EFS Shared Files)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

내부 분석 시스템이 “항상 답답하다”는 불만이 나온다. CPU는 여유인데 쿼리/배치가 시작되면 응답이 뚝뚝 끊긴다. CloudWatch에서 `VolumeQueueLength`가 올라가고 I/O 관련 지표가 포화된 느낌이다. 인스턴스를 키워도 큰 변화가 없다.  
이 상황에서 가장 자연스러운 1차 접근은?

A. EC2 인스턴스 타입만 계속 키운다(컴퓨트가 항상 병목이다)  
B. EBS 성능 축(IOPS/처리량) 병목을 의심하고 볼륨 타입/튜닝(gp3/io2)을 검토한다  
C. Route 53 라우팅 정책을 Latency로 바꾼다  
D. IAM Allow를 더 준다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: CPU가 낮고 큐/IO wait 신호가 보이면 스토리지 I/O 병목일 가능성이 높다. 병목 축을 맞춰야 비용/성능이 함께 개선된다.
- 소거법
  - A (근접 오답): 흔한 오판. 컴퓨트 스케일업만으로 I/O 병목이 풀리지 않을 수 있다.
  - C (명확히 틀림): DNS는 EBS 큐 길이와 무관하다.
  - D (명확히 틀림): 권한 문제는 I/O 지표로 나타나지 않는다.
- 한 줄 규칙: “느린데 CPU는 낮다”면 **스토리지/네트워크 병목**을 먼저 의심한다.
- 태그: `pillar:performance-efficiency` `services:EBS,CloudWatch` `week:03` `day:03`

</details>

---

## Q2.

요구사항이 이렇게 들어왔다. “디스크 용량은 충분하다. 그런데 I/O가 병목이라 성능(IOPS/처리량)만 올리고 싶다.”  
이 문장 신호에 가장 자연스러운 EBS 타입/접근은?

A. gp3를 사용하고 IOPS/처리량을 조절해 튜닝한다  
B. st1(sc1) 같은 HDD로 바꿔 비용을 낮춘다  
C. standard(magnetic)로 바꿔 레거시를 유지한다  
D. EFS로 바꿔 단일 인스턴스 디스크를 대체한다  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: gp3는 용량과 성능(IOPS/처리량)을 분리해 “필요한 만큼만” 맞추기 좋다. 요구 기능을 만족하면서 과한 비용을 피할 수 있다.
- 소거법
  - B (근접 오답): 비용은 내려갈 수 있지만 랜덤 I/O 병목이면 성능이 더 나빠질 수 있다.
  - C (명확히 틀림): 구형/트랩에 가깝다.
  - D (명확히 틀림): 공유 파일 요구가 없는데 레이어를 바꾸는 건 부자연스럽다.
- 한 줄 규칙: “용량은 OK, 성능만”이면 **gp3 튜닝**이 1순위 후보.
- 태그: `pillar:cost-optimization` `services:EBS` `week:03` `day:03`

</details>

---

## Q3.

요구사항이 이렇게 들어왔다. “높은 IOPS가 필요하고, 지연이 일정해야 한다(일관된 성능). 비용이 좀 더 들어도 된다.”  
이 문장 신호에 가장 자연스러운 EBS 타입은?

A. io2(프로비저닝 IOPS)  
B. sc1(콜드 HDD)  
C. gp2(레거시)  
D. S3 Standard  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: “높은/일관된 IOPS” 신호는 프로비저닝 IOPS(io2)로 매핑된다.
- 소거법
  - B (명확히 틀림): 성능 요구와 반대다.
  - C (근접 오답): 가능할 수는 있지만 “일관된 고IOPS” 신호엔 io2가 더 자연스럽다.
  - D (명확히 틀림): 객체 스토리지다.
- 한 줄 규칙: “일관된 고IOPS”면 **io2**.
- 태그: `pillar:performance-efficiency` `services:EBS` `week:03` `day:03`

</details>

---

## Q4.

웹 서버를 Auto Scaling으로 늘리기 시작하자 업로드 파일(이미지/첨부)이 각 인스턴스의 로컬 디스크에 흩어졌다. 어떤 사용자는 파일이 보이고 어떤 사용자는 안 보인다. 팀은 NFS를 직접 구성하거나 rsync로 동기화하려 하지만, 인스턴스가 늘어날수록 운영이 지옥이 된다.  
요구사항(여러 인스턴스가 같은 파일을 읽고/쓴다, 공유 POSIX 파일시스템)에 가장 자연스러운 선택은?

A. EBS를 여러 인스턴스에 동시에 붙인다  
B. EFS를 마운트해 공유 파일시스템으로 사용한다  
C. 각 인스턴스에 파일을 따로 유지하고 “문제 없다고 가정”한다  
D. Route 53 Latency 라우팅으로 파일을 공유한다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 수동 동기화/단일 파일 서버 같은 운영 함정을 제거하는 방향이 정답이다. “공유 파일” 신호는 EFS로 바로 매핑된다.
- 소거법
  - A (근접 오답): EBS는 기본적으로 인스턴스에 붙는 블록 스토리지라 “공유 모델”과 결이 다르다(함정).
  - C (명확히 틀림): 요구사항(공유/일관성)과 정면 충돌한다.
  - D (명확히 틀림): DNS는 파일 일관성을 제공하지 않는다.
- 한 줄 규칙: “여러 인스턴스가 같은 파일”이면 **EFS**.
- 태그: `pillar:operational-excellence` `services:EFS` `week:03` `day:03`

</details>

---

## Q5. (복수정답: 2개)

다음 중 사실에 맞는 설명 2개를 고르시오.

A. EBS는 인스턴스에 붙는 블록 스토리지로 “단일 인스턴스 I/O 튜닝” 축에 가깝다  
B. EFS는 여러 인스턴스가 동시에 마운트해 공유하는 파일시스템(NFS) 축에 가깝다  
C. EFS는 “용량은 그대로, IOPS만 조절” 같은 요구에 가장 직접적이다  
D. gp3는 공유 파일시스템이라 여러 인스턴스가 동시에 마운트한다  
E. NACL을 열면 EBS IOPS가 자동으로 증가한다  

<details>
<summary>정답/해설</summary>

- 정답: A, B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 스토리지 문제는 “요구 레이어(블록 vs 공유 파일)”를 먼저 맞춰야 소거가 빠르다.
- 소거법
  - C (근접 오답): 그 신호는 EBS(gp3/io2) 축이다.
  - D (명확히 틀림): gp3는 EBS 볼륨 타입이다.
  - E (명확히 틀림): 네트워크 규칙과 IOPS는 별개다.
- 한 줄 규칙: “공유 파일=EFS, I/O 튜닝=EBS”로 분리한다.
- 태그: `pillar:operational-excellence` `services:EBS,EFS` `week:03` `day:03`

</details>

---

## TL;DR (오늘의 규칙)

- “IOPS/큐/지연” 신호면 **EBS 타입(gp3/io2) 튜닝**, “공유 파일” 신호면 **EFS**.
