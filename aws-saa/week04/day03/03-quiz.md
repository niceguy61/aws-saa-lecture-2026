# 03-quiz - Week 04 Day 03 (S3 Storage Classes / Lifecycle / Intelligent-Tiering)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

팀이 로그/백업/릴리즈 파일을 전부 S3 Standard에 넣어두고 있었는데, 데이터가 몇 TB를 넘어가면서 매달 비용이 눈에 띄게 늘었다. “모두 Glacier로 옮기자”는 의견이 나오지만, 일부 데이터는 사고 조사 때 즉시 꺼내야 할 때도 있다.  
문장 신호가 “가끔 접근하지만, 조회 시 즉시(즉각) 복구가 필요하다”일 때 가장 자연스러운 클래스 후보는?
A. S3 Standard-IA  
B. S3 버킷을 퍼블릭으로 연다  
C. S3 One Zone-IA(단일 AZ 허용이 핵심 신호)  
D. S3 Glacier Deep Archive  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용만 보고 최저 클래스를 고르면 “복구 요구”를 깨기 쉽다. “가끔 접근 + 즉시 복구”는 IA 계열 신호다.
- 소거법
  - D (근접 오답): 장기 보관/느린 복구(대기 가능) 신호가 강할 때 후보가 된다.
  - C (근접 오답): 단일 AZ 허용 신호가 없으면 위험/요구 미스가 될 수 있다.
  - B (명확히 틀림): 접근 제어를 무너뜨리는 선택이다.
- 한 줄 규칙: “가끔 접근 + 즉시 필요”면 **Standard-IA**부터 본다.
- 태그: `pillar:cost-optimization` `services:S3` `week:04` `day:03`

</details>

---

## Q2.

요구사항이 “거의 안 보고, 장기 보관이 목적이며, 복구가 느려도 된다(대기 허용)”로 명확하다. 비용을 최소화하는 게 최우선이다.  
이 신호에서 가장 자연스러운 클래스 후보는?
A. S3 Glacier 계열(특히 Deep Archive 같은 장기/최저 비용 방향)  
B. S3 Intelligent-Tiering(항상 정답)  
C. EBS io2  
D. S3 Standard  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: “거의 안 봄 + 장기 보관 + 느린 복구 허용” 신호는 아카이브 계열(Glacier)로 매핑된다. 저장비는 낮지만 복구/요청 비용/시간 트레이드오프가 있다.
- 소거법
  - D (근접 오답): 즉시/자주 접근 신호가 없으면 과할 수 있다.
  - B (근접 오답): 패턴 예측 어려움 신호가 강할 때 후보가 된다. “항상 콜드”면 명시 선택이 더 자연스럽다.
  - C (명확히 틀림): 블록 스토리지다.
- 한 줄 규칙: “장기 보관/느린 복구 OK”면 **Glacier 계열**.
- 태그: `pillar:cost-optimization` `services:S3` `week:04` `day:03`

</details>

---

## Q3.

팀이 비용을 줄이려고 “오래된 데이터는 사람이 직접 클래스를 바꾸거나 삭제”하는 방식으로 운영했다. 담당자가 바뀌면 규칙이 깨지고, 어떤 데이터는 지워져 사고가 난다. 비용 최적화가 오히려 품질을 깎는 상황이다.  
“사람의 기억”이 아니라 “정책”으로 전환/만료를 고정하려면 가장 자연스러운 선택은?
A. S3 Lifecycle rule로 Transition/Expiration을 자동화한다  
B. 매달 수동으로 콘솔에서 클래스를 옮긴다  
C. Route 53 Failover를 설정한다  
D. 모든 데이터를 즉시 Glacier Deep Archive로 이동한다(요구 무시)  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 수동 작업/사람 의존을 정책/자동화로 바꾸는 게 핵심이다. 라이프사이클은 전환/만료를 자동화한다.
- 소거법
  - B (명확히 틀림): 운영 실수/누락이 반복되는 패턴이다.
  - D (근접 오답): 비용은 줄 수 있어도 복구 요구/핫 데이터 요구를 깨기 쉽다.
  - C (명확히 틀림): DNS다.
- 한 줄 규칙: “자동 전환/보관 정책”이면 **Lifecycle**.
- 태그: `pillar:operational-excellence` `services:S3` `week:04` `day:03`

</details>

---

## Q4.

릴리즈 아카이브 파일이 어떤 달엔 많이 내려받고, 어떤 달엔 거의 안 본다. 액세스 패턴을 예측해서 정책을 만들려 해도 제품/마케팅 일정에 따라 변동이 커서 자주 틀린다. “자동 최적화” 신호가 명확하다.  
이 요구에 가장 자연스러운 선택은?
A. S3 Standard만 유지(항상 안전)  
B. S3 Intelligent-Tiering  
C. S3 Glacier Deep Archive(항상 최저)  
D. EFS  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 “규칙을 유지하는 비용/실수”를 줄이는 방향이 정답이다. 패턴 예측이 어렵다면 Intelligent-Tiering이 자동으로 티어를 이동한다.
- 소거법
  - C (근접 오답): 항상 콜드/복구 느림 OK일 때는 맞지만, ‘갑자기 핫해질 수 있음’ 신호와 충돌할 수 있다.
  - A (근접 오답): 안전하지만 과지출 가능성이 크다(요구가 비용 최적화/자동화 쪽).
  - D (명확히 틀림): 공유 파일시스템이다.
- 한 줄 규칙: “예측 어려움/자동 최적화”면 **Intelligent-Tiering**.
- 태그: `pillar:operational-excellence` `services:S3` `week:04` `day:03`

</details>

---

## Q5. (복수정답: 2개)

로그는 1년 보관해야 하지만, 90일이 지나면 거의 보지 않는다. `logs/`와 `app/` 데이터 성격이 다르고, 핫 데이터까지 같이 내려버리면 사고가 난다. “자동 전환/만료” 요구가 있다.  
가장 자연스러운 조치 2개를 고르시오.
A. 수동으로 매달 콘솔에서 옮긴다  
B. S3 버킷을 퍼블릭으로 연다  
C. `logs/` prefix에만 적용되는 Lifecycle rule을 만들어 전환/만료를 자동화한다  
D. prefix/범위를 분리해 데이터 성격별로 다른 정책을 적용한다  
E. 버킷 전체에 동일한 전환을 걸어 모든 데이터를 한 번에 Glacier로 내린다  
<details>
<summary>정답/해설</summary>

- 정답: C, D
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: “정책 자동화 + 범위 분리”로 운영 실수와 사고를 줄인다. 데이터 성격이 다르면 정책도 달라야 한다.
- 소거법
  - E (근접 오답): 비용은 줄어도 핫 데이터 요구를 깨기 쉬운 함정이다.
  - A (명확히 틀림): 사람 의존/누락으로 사고가 반복된다.
  - B (명확히 틀림): 접근 제어를 무너뜨린다.
- 한 줄 규칙: Lifecycle은 **자동화**, 그리고 **범위(prefix) 분리**가 같이 나온다.
- 태그: `pillar:operational-excellence` `services:S3` `week:04` `day:03`

</details>

---

