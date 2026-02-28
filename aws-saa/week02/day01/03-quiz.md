# 03-quiz - Week 02 Day 01 (Route 53 Routing / DR Strategies)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

서비스가 단일 리전/단일 엔드포인트로 운영되다가, 이제 “장애가 나면 자동으로 다른 곳으로 넘어가야 한다”는 요구가 명확해졌다. 운영팀은 DNS 단계에서 primary/secondary를 두고, 헬스 체크 기반으로 전환되길 원한다.  
Route 53 라우팅 정책으로 가장 자연스러운 선택은?
A. Failover  
B. Simple  
C. Geolocation  
D. Weighted  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 장애 감지/전환 요구는 “헬스체크 기반 장애 조치”로 매핑되고, Route 53 Failover가 대표 선택이다.
- 소거법
  - B (근접 오답): 요구가 없을 때의 단순 라우팅에 가깝다.
  - D (근접 오답): 비율/점진 배포가 목적일 때 맞다.
  - C (명확히 틀림): 장애 조치가 아니라 위치 기반 요구에서 등장한다.
- 한 줄 규칙: “health check + 장애 조치”면 **Failover**.
- 태그: `pillar:reliability` `services:Route53` `week:02` `day:01`

</details>

---

## Q2.

개발팀이 새 버전을 위험하게 한 번에 올리고 싶지 않다. “전체 트래픽 중 10%만 새 버전으로 보내고, 문제가 없으면 30% → 100%로 늘리자”는 점진 배포(카나리) 요구가 들어왔다.  
Route 53 라우팅 정책으로 가장 적절한 것은?
A. Latency  
B. Failover  
C. Simple  
D. Weighted  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 위험을 통제하며 변경을 배포하는 방식(점진 배포)이 중요하다. “비율 조정” 요구는 Weighted로 직접 매핑된다.
- 소거법
  - B (근접 오답): 장애 조치가 아니라 “비율”이 핵심이다.
  - C (명확히 틀림): 비율/점진 분배 요구를 만족시키지 못한다.
  - A (근접 오답): 지연 시간 최적화가 목적일 때 선택한다.
- 한 줄 규칙: “percentage/카나리/AB 테스트”면 **Weighted**.
- 태그: `pillar:operational-excellence` `services:Route53` `week:02` `day:01`

</details>

---

## Q3.

글로벌 사용자 비중이 늘었다. 요구사항은 “가장 가까운(지연 시간이 낮은) 리전으로 보내달라”는 것이다. 단순히 국가별로 나누는 게 아니라, 실제 네트워크 지연 시간을 기준으로 라우팅하고 싶다.  
Route 53 라우팅 정책으로 가장 자연스러운 선택은?
A. Failover  
B. Latency  
C. Weighted  
D. Multivalue answer  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 성능 효율성은 요구 성능(지연 시간)을 만족시키는 설계를 고르는 것이다. “lowest latency/closest” 신호는 Latency 기반 라우팅으로 매핑된다.
- 소거법
  - A (근접 오답): 장애 조치가 목적이 아니다.
  - C (근접 오답): 비율 분산이 목적이 아니다.
  - D (명확히 틀림): 다중 값 응답은 ‘지연 시간 최적화’와 직접 매핑되지 않는다.
- 한 줄 규칙: “가까운 리전/지연 시간”이면 **Latency**.
- 태그: `pillar:performance-efficiency` `services:Route53` `week:02` `day:01`

</details>

---

## Q4.

경영진이 묻는다. “리전 장애가 나면 얼마나 빨리 복구돼야 하나요?” 계약/규제 때문에 복구 시간(RTO)과 데이터 손실 허용량(RPO)을 정의해야 한다. 팀은 비용도 고려해야 한다. “항상 두 곳에서 완전히 운영(Active/Active)”은 빠르지만 비싸고, “백업만”은 싸지만 느리다.  
재무팀이 “DR 예산은 최소로, 대신 복구는 몇 시간 걸려도 된다”라고 못 박았다. 이 조건에서 가장 흔한 DR 전략 선택은?
A. Multi-site Active/Active  
B. Always-on Multi-Region  
C. Warm standby  
D. Backup/Restore  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용을 낮추려면 평소에 덜 띄워두는 방향(백업 중심)으로 가지만, 그만큼 복구 시간이 길어지기 쉽다.
- 소거법
  - A (명확히 틀림): 가장 빠르지만 비용이 가장 크다.
  - C (근접 오답): 백업보다 RTO를 줄이려고 “축소 운영”을 유지한다.
  - B (명확히 틀림): 상시 운영은 비용을 낮추는 선택이 아니다.
- 한 줄 규칙: “싸게” 가면 보통 **RTO가 길어진다**(백업/복구).
- 태그: `pillar:cost-optimization` `services:DR` `week:02` `day:01`

</details>

---

## Q5. (복수정답: 2개)

DR은 “리소스를 만들어두는 것”으로 끝나지 않는다. 장애 시 어떤 순서로 전환/복구할지, 그리고 그 계획이 실제로 작동하는지까지 운영에 포함돼야 한다.  
운영 우수성 관점에서, DR 계획에 “반드시 포함돼야 하는 것” 2개를 고르시오.
A. S3 버킷을 퍼블릭으로 열어 접근을 단순화한다  
B. 정기적으로 DR 전환 연습(Game day)을 수행한다  
C. 모든 사용자가 루트 사용자로만 복구 작업을 수행한다  
D. RPO/RTO 정의 없이 “최대한 빨리”라고만 적는다  
E. 장애 시 전환/복구 절차(runbook)를 문서화한다  
<details>
<summary>정답/해설</summary>

- 정답: B, E
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 “계획 + 반복 가능한 절차 + 연습”으로 위험을 줄인다. DR은 특히 연습 없는 계획은 실전에서 잘 깨진다.
- 소거법
  - A (명확히 틀림): 보안 요구와 정반대다.
  - C (명확히 틀림): 루트 사용은 통제/감사/분리 관점에서 오답이다.
  - D (근접 오답): 의지는 좋지만 기준(RPO/RTO) 없이 설계가 흔들린다.
- 한 줄 규칙: DR은 **runbook + 연습**이 있어야 ‘운영’이 된다.
- 태그: `pillar:operational-excellence` `services:DR` `week:02` `day:01`

</details>

---

