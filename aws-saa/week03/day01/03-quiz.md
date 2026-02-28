# 03-quiz - Week 03 Day 01 (EC2 Sizing / CloudWatch Bottleneck)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

배치 API가 매일 특정 시간대에만 처리 시간이 급격히 늘어난다. 팀은 “순간 트래픽이니까 T 계열이면 싸고 좋다”라고 생각해 t3를 늘렸는데, 며칠 뒤부터는 같은 시간대에 더 심하게 느려지고 응답이 끊기는 구간까지 생긴다. “지속적으로 CPU를 쓰는 구간”이 반복되고 “일관된 성능”이 중요하다는 신호가 명확하다.  
이 요구에 더 자연스러운 EC2 패밀리 방향은?
A. X(초고메모리) 계열로 바꾼다(무조건 빠르다)  
B. C(컴퓨트 최적화) 계열 같은 지속 고CPU에 맞는 패밀리를 고려한다  
C. S3 Versioning을 켠다  
D. T(버스트) 계열을 더 늘린다(항상 가장 싸다)  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: “지속 고CPU/일관 성능” 신호가 강하면 T의 크레딧 모델이 함정이 될 수 있다. CPU가 병목이라면 C 계열이 자연스럽다.
- 소거법
  - D (근접 오답): 스케일로 버틸 수 있어 보여도, 크레딧 소진 유형이면 근본 원인을 못 고친다.
  - A (명확히 틀림): 메모리 신호 없이 초고메모리를 고르는 건 과하다.
  - C (명확히 틀림): 스토리지 실수 복구 기능이다.
- 한 줄 규칙: “지속 고CPU/일관 성능”이면 **T가 아니라 C/M**부터 본다.
- 태그: `pillar:performance-efficiency` `services:EC2` `week:03` `day:01`

</details>

---

## Q2.

워크로드가 평소에는 CPU 사용률이 매우 낮고, 하루에 몇 번 짧게 CPU가 튀는 “간헐 스파이크” 형태다. 비용을 아끼는 게 중요하고, 지속적으로 CPU를 태우는 구간은 없다.  
이 문장 신호에 가장 자연스러운 선택은?
A. GPU(G/P) 계열  
B. C(컴퓨트 최적화) 계열  
C. X(초고메모리) 계열  
D. T(버스트) 계열  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용 최적화는 요구 형태에 맞는 “가성비 옵션”을 고르는 것이다. 간헐 스파이크면 T 계열의 burst 모델이 비용 효율적일 수 있다.
- 소거법
  - B (근접 오답): 성능은 좋지만 지속 고CPU 신호가 없으면 과할 수 있다.
  - C (명확히 틀림): 메모리 신호가 없다.
  - A (명확히 틀림): GPU/ML 신호가 없다.
- 한 줄 규칙: “가끔만 튄다”면 **T**, “계속 높다”면 **C/M**.
- 태그: `pillar:cost-optimization` `services:EC2` `week:03` `day:01`

</details>

---

## Q3.

성능 신고가 들어와 CPU 그래프부터 봤는데 CPUUtilization은 30% 수준이다. 그런데 CloudWatch에서 `VolumeQueueLength`가 올라가고 `VolumeWriteBytes`가 꾸준히 늘어난다. 즉 “CPU가 낮은데도 느린” 케이스다.  
가장 가능성이 큰 병목 축은?
A. DNS 병목(Route 53)  
B. 스토리지 I/O 병목(EBS 큐/처리량 이슈)  
C. IAM 권한 평가 병목(Explicit Deny)  
D. CPU 병목(스펙 업만 하면 해결)  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 성능 문제는 “병목 축 분리”가 핵심이다. CPU가 낮고 EBS 큐가 높으면 스토리지 I/O가 병목일 가능성이 크다.
- 소거법
  - D (근접 오답): CPU만 보고 결론 내리는 건 흔한 함정이다.
  - A (명확히 틀림): DNS는 볼륨 큐 길이와 무관하다.
  - C (명확히 틀림): 권한 문제는 지표(QueueLength)로 나타나지 않는다.
- 한 줄 규칙: CPU가 낮아도 느리면 **I/O/네트워크 지표로 교차 확인**한다.
- 태그: `pillar:performance-efficiency` `services:CloudWatch,EBS` `week:03` `day:01`

</details>

---

## Q4.

T 계열 인스턴스에서 CPUUtilization은 그럴듯하게 보이는데, 특정 시점부터 지연이 급격히 악화된다. CloudWatch를 보면 `CPUCreditBalance`가 바닥나고 그 순간부터 성능이 무너진다.  
장애 보고서에 원인을 한 문장으로 적어야 한다. 가장 정확한 설명은?
A. S3 Replication이 설정되지 않아 지연이 생긴다  
B. T 계열은 지속 부하에서 크레딧 소진으로 스로틀링되어 성능이 급락할 수 있다  
C. CloudTrail이 부족해서 지연이 생긴다  
D. T 계열은 언제나 일관된 성능을 보장한다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: T 계열의 핵심 함정은 “크레딧”이다. 지속 CPU 사용 시 크레딧이 소진되면 스로틀링으로 p95/p99 지연이 무너질 수 있다.
- 소거법
  - D (근접 오답): 반대다. 일관 성능 요구에 T는 함정이 될 수 있다.
  - C (명확히 틀림): 감사 로그는 성능과 축이 다르다.
  - A (명확히 틀림): 복제는 스토리지 DR 축이다.
- 한 줄 규칙: T 계열 + 지연이면 **크레딧 지표**를 본다.
- 태그: `pillar:performance-efficiency` `services:EC2,CloudWatch` `week:03` `day:01`

</details>

---

## Q5. (복수정답: 2개)

T 계열 인스턴스의 성능이 갑자기 나빠졌는데, CPUUtilization만 보면 애매하다. 고객 사례처럼 “크레딧 소진”이 원인인지 빠르게 확인하고 싶다.  
CloudWatch에서 가장 먼저 같이 확인할 지표 2개를 고르시오.
A. NetworkIn  
B. StatusCheckFailed  
C. VolumeQueueLength  
D. CPUCreditBalance  
E. CPUCreditUsage  
<details>
<summary>정답/해설</summary>

- 정답: D, E
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 “재현/진단 루틴”을 표준화하는 것이다. T 계열 성능 문제는 크레딧 관련 지표(잔고/사용량)가 가장 직접적인 힌트다.
- 소거법
  - A (근접 오답): 네트워크 병목일 수도 있지만, “T 크레딧” 확인이라는 목적에 더 직접적이지 않다.
  - C (근접 오답): I/O 병목 진단에 유용하지만, 크레딧 소진 여부를 바로 말해주진 않는다.
  - B (명확히 틀림): 인스턴스 상태 체크는 크레딧 소진과 다른 축이다.
- 한 줄 규칙: “T 계열 + 성능 저하”면 **CreditBalance/Usage**부터 본다.
- 태그: `pillar:operational-excellence` `services:CloudWatch,EC2` `week:03` `day:01`

</details>

---

