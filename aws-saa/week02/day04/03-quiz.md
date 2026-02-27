# 03-quiz - Week 02 Day 04 (RDS/Aurora: Multi-AZ vs Read Replica / DynamoDB PITR)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

DB 장애가 한 번 나고 나서 운영팀이 요구한다. “몇 분 다운도 안 됩니다. 장애가 나면 자동으로 넘어가야 합니다(failover).”  
이 문장이 핵심일 때, RDS/Aurora에서 가장 자연스러운 선택은?

A. Read replica만 추가한다  
B. Multi-AZ를 구성한다  
C. S3 Versioning을 켠다  
D. CloudFront를 붙인다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: “자동 장애 조치/가용성” 신호는 Multi-AZ로 매핑된다. Read replica는 읽기 확장이지 HA failover의 standby가 아니다.
- 소거법
  - A (근접 오답): 읽기 확장에는 도움 되지만, 자동 failover 요구를 만족하지 못한다.
  - C (명확히 틀림): 객체 실수 복구 기능이다.
  - D (명확히 틀림): 캐시/전송 계층이다.
- 한 줄 규칙: “failover/가용성”이면 **Multi-AZ**.
- 태그: `pillar:reliability` `services:RDS,Aurora` `week:02` `day:04`

</details>

---

## Q2.

이번엔 장애가 아니라 성능이 문제다. 요구사항은 “read-heavy, 읽기 트래픽이 폭증해서 읽기 성능을 늘려야 한다”이다. 자동 장애 조치가 핵심 문장으로 등장하지는 않는다.  
이때 가장 자연스러운 선택은?

A. Multi-AZ만 구성한다  
B. Read replica를 추가해 읽기 트래픽을 분산한다  
C. NACL을 모두 Allow로 바꾼다  
D. Route 53 Weighted 라우팅을 설정한다  

<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 성능 효율성은 병목 신호에 맞는 확장 수단을 고르는 것이다. “읽기 확장” 신호는 Read replica로 매핑된다.
- 소거법
  - A (근접 오답): Multi-AZ는 HA(failover) 중심이지 read scaling 도구가 아니다.
  - C (명확히 틀림): 네트워크를 여는 건 DB 읽기 확장을 만들지 못한다.
  - D (명확히 틀림): DNS는 DB 내부 읽기 확장과 축이 다르다.
- 한 줄 규칙: “read-heavy”면 **Read replica**.
- 태그: `pillar:performance-efficiency` `services:RDS,Aurora` `week:02` `day:04`

</details>

---

## Q3.

다음 중 “대표 함정”을 가장 잘 짚은 문장은?

A. Read replica는 자동 장애 조치(HA)용 standby이므로 Multi-AZ를 대체한다  
B. Multi-AZ는 읽기 성능을 늘리는 기능이므로 read-heavy 문제에 1순위다  
C. Read replica는 ‘읽기 확장’, Multi-AZ는 ‘자동 장애 조치(가용성)’로 목적이 다르다  
D. 두 기능은 모두 DNS 라우팅 정책이다  

<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 운영 우수성은 요구사항을 올바른 기능으로 분해해(가용성 vs 읽기 확장) 오해로 인한 잘못된 변경을 줄인다. 시험도 이 혼동을 노린다.
- 소거법
  - A (근접 오답): “read replica로 HA”는 단골 오답이다.
  - B (근접 오답): 목적이 반대다.
  - D (명확히 틀림): DB 옵션이지 DNS가 아니다.
- 한 줄 규칙: **Multi-AZ=failover, Read replica=read scaling**.
- 태그: `pillar:operational-excellence` `services:RDS,Aurora` `week:02` `day:04`

</details>

---

## Q4.

운영 중 배치가 잘못 돌아 특정 파티션 키의 값이 전부 덮어써졌다. 장애(리전 장애)가 아니라 “실수로 데이터가 망가졌다”가 핵심이고, 팀은 “몇 시간 전 상태로만 되돌릴 수 있으면 된다”고 한다.  
이 요구에 가장 자연스러운 DynamoDB 기능은?

A. DynamoDB PITR(Point-in-time recovery)  
B. CloudFront 캐시 무효화  
C. Route 53 Failover  
D. S3 Replication(CRR)  

<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: “실수 롤백/시점 복구” 요구에 직접 대응하는 기능이 PITR이다. 재해(리전 DR)와 실수 복구를 먼저 분리해야 한다.
- 소거법
  - B (명확히 틀림): 캐시는 데이터 복구를 제공하지 않는다.
  - C (명확히 틀림): DNS 전환은 데이터 롤백이 아니다.
  - D (근접 오답): 복제는 원격 DR/규제에서 등장한다. “시점 복구” 요구와 축이 다르다.
- 한 줄 규칙: “실수로 업데이트/삭제”면 DynamoDB는 **PITR**.
- 태그: `pillar:reliability` `services:DynamoDB` `week:02` `day:04`

</details>

---

## Q5. (복수정답: 2개)

요구사항이 두 가지로 동시에 들어왔다.  
1) “장애 시 자동 failover”(가용성)  
2) “read-heavy라 읽기 성능 확장”(읽기 분산)  
두 요구를 가장 자연스럽게 만족시키는 구성 2개를 고르시오.

A. Multi-AZ 구성  
B. Read replica 추가  
C. S3 Versioning 켜기  
D. NLB로 교체하기  
E. CloudTrail Trail 생성  

<details>
<summary>정답/해설</summary>

- 정답: A, B
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 요구를 분해해 각각의 기능에 매핑해야 한다. failover는 Multi-AZ, read scaling은 Read replica다(목적 분리 후 조합).
- 소거법
  - C (명확히 틀림): 객체 스토리지 실수 복구다.
  - D (명확히 틀림): 로드밸런서는 DB의 failover/read scaling을 직접 제공하지 않는다.
  - E (근접 오답): 감사/추적엔 필요할 수 있지만, 가용성/읽기 확장 요구의 답이 아니다.
- 한 줄 규칙: “가용성 vs 읽기 확장”을 먼저 분리하고 **Multi-AZ + RR**로 조합한다.
- 태그: `pillar:reliability` `services:RDS,Aurora` `week:02` `day:04`

</details>

---

## TL;DR (오늘의 규칙)

- “failover”면 **Multi-AZ**, “read-heavy”면 **Read replica**.  
- DynamoDB는 “실수 롤백”이면 **PITR**이 1순위 후보.
