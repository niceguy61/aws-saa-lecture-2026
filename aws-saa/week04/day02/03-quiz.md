# 03-quiz - Week 04 Day 02 (EC2 Purchase Options / Right Sizing / Auto Scaling)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

서비스가 안정됐고 트래픽 변동이 크지 않다. “1~3년 사용량이 예측 가능(steady state)”하다는 문장이 강하다. 매달 EC2 비용이 꾸준히 크고, 큰 절감이 필요하다.  
이 신호에서 가장 자연스러운 구매/할인 모델 후보는?

A. Savings Plans 또는 Reserved Instances  
B. Spot  
C. On-Demand만 유지(할인은 금지)  
D. S3 Glacier Deep Archive  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: steady state는 “장기 커밋”의 근거다. RI/SP는 예측 가능할수록 비용 효율이 올라간다.
- 소거법
  - B (근접 오답): Spot은 “중단 허용” 신호가 있어야 정답이 된다.
  - C (근접 오답): 유연하지만 절감 폭이 작아 “큰 절감” 요구와 어긋난다.
  - D (명확히 틀림): 스토리지 클래스다.
- 한 줄 규칙: “예측 가능 1~3년”이면 **RI/SP**.
- 태그: `pillar:cost-optimization` `services:EC2` `week:04` `day:02`

</details>

---

## Q2.

배치 작업이 매일 밤 몇 시간만 돌고, 중간에 끊겨도 재시도하면 된다. “fault-tolerant”, “중단 허용” 같은 문장이 있다. 그런데 현재는 On-Demand로 돌리고 있다.  
가장 자연스러운 비용 최적화 선택은?

A. Spot  
B. Reserved Instances  
C. 모든 워크로드를 항상 On-Demand로만 돌린다  
D. Route 53 Failover를 설정한다  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: “중단 허용/재시도 가능”은 Spot의 핵심 신호다. 조건이 맞으면 절감 폭이 크다.
- 소거법
  - B (근접 오답): 예측 가능(steady state) 신호가 더 강할 때 후보가 된다.
  - C (명확히 틀림): 중단 허용 신호가 있는데 할인을 포기하면 비용 최적화가 약하다.
  - D (명확히 틀림): DNS는 구매 옵션과 무관하다.
- 한 줄 규칙: “중단 허용 배치”면 **Spot**.
- 태그: `pillar:cost-optimization` `services:EC2` `week:04` `day:02`

</details>

---

## Q3.

트래픽이 스파이크가 심하고 예측이 어렵다. “평상시엔 낮고 피크만 급증”한다. 장기 약정은 부담스럽고, 피크를 버티기 위해 24시간 비싼 스펙을 유지하고 싶지 않다.  
이 문장 신호에서 가장 자연스러운 기본 선택은?

A. On-Demand를 기본으로 두고 Auto Scaling으로 피크만 대응한다  
B. 무조건 Reserved Instances를 산다  
C. 무조건 Spot만 사용한다(중단 고려 없음)  
D. 모든 인스턴스를 가장 큰 타입으로 고정한다  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 예측이 어렵고 변동이 크면 유연성이 중요하다. On-Demand + ASG로 “피크만 비용을 지불”하는 패턴이 자연스럽다.
- 소거법
  - B (근접 오답): steady state 신호가 없으면 약정이 함정이 될 수 있다.
  - C (근접 오답): 중단 허용 신호 없이 Spot을 밀면 신뢰성 요구를 깨기 쉽다.
  - D (명확히 틀림): 24시간 비용 낭비가 커진다.
- 한 줄 규칙: “스파이크/예측 어려움”이면 **On-Demand + ASG**.
- 태그: `pillar:cost-optimization` `services:AutoScaling,EC2` `week:04` `day:02`

</details>

---

## Q4.

팀이 비용이 부담돼 인스턴스를 작은 타입으로 바꾸려 한다. 그런데 “한 번 내리면 장애가 나고, 다시 올리면 최적화 실패”가 반복된다. 어떤 리소스가 병목인지, 지금 스펙이 과한지 부족한지에 대한 측정이 없다.  
right sizing을 올바르게 시작하는 가장 자연스러운 방법은?

A. CloudWatch 지표(CPU/네트워크/I/O 등)로 실제 사용량을 측정한 뒤, 요구사항을 만족하는 최소 스펙을 찾는다  
B. CPU만 보고 무조건 한 단계 내린다  
C. 모든 리소스를 밤에 강제로 종료한다(영향 분석 없음)  
D. 보안 그룹을 0.0.0.0/0으로 열면 성능이 좋아진다  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 근거 기반 변경으로 장애를 줄인다. right sizing은 “스펙 줄이기”가 아니라 “측정 기반 최소화”다.
- 소거법
  - B (근접 오답): CPU만 보고 내리면 실제 병목이 메모리/I/O면 더 나빠질 수 있다.
  - C (근접 오답): 비피크가 명확할 때는 유효하지만, “영향 분석 없이”는 위험하다.
  - D (명확히 틀림): 보안/성능 축이 다르다.
- 한 줄 규칙: right sizing은 **측정부터**다.
- 태그: `pillar:operational-excellence` `services:CloudWatch` `week:04` `day:02`

</details>

---

## Q5. (복수정답: 2개)

업무 시스템이라 “업무시간 외에는 트래픽이 거의 없다”는 문장이 있다. 목표는 “요구사항을 깨지 않으면서” 큰 절감을 만드는 것이다.  
가장 자연스러운 조치 2개를 고르시오.

A. Auto Scaling scheduled action으로 야간(비피크)에 desired를 0으로 줄인다  
B. CloudWatch 지표로 실제 사용량을 측정해 right sizing(과한 스펙)을 조정한다  
C. Spot을 중단 불가 서비스의 기본 옵션으로 강제한다  
D. S3 버킷을 퍼블릭으로 연다  
E. 루트 사용자로만 운영 작업을 수행한다  

<details>
<summary>정답/해설</summary>

- 정답: A, B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 큰 절감은 “항상 켜둔 낭비”를 줄이는 데서 자주 나온다(비피크 축소). 동시에 측정 기반 right sizing으로 과한 스펙을 줄인다.
- 소거법
  - C (근접 오답): Spot은 중단 허용 신호가 있어야 한다.
  - D (명확히 틀림): 비용 최적화/보안 모두 악화될 수 있다.
  - E (명확히 틀림): 운영/보안 원칙 위반이다.
- 한 줄 규칙: 절감 레버리지는 **비피크 축소 + 측정 기반 right sizing**.
- 태그: `pillar:cost-optimization` `services:AutoScaling,CloudWatch,EC2` `week:04` `day:02`

</details>

---

## TL;DR (오늘의 규칙)

- “예측 가능”이면 **RI/SP**, “중단 허용”이면 **Spot**, “스파이크”면 **On-Demand + ASG**.  
- right sizing은 **측정 기반**, 큰 절감은 **비피크 축소(스케줄)**에서 자주 나온다.
