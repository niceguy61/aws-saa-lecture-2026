# 04-quiz - Week 02 Day 03 (S3 Versioning / S3 Replication / EBS Snapshot)

- 문항 수: 5 (Day 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

배치 작업이 오래된 파일을 정리하다가, 필요한 객체까지 같이 삭제해버렸다. 팀은 “S3는 내구성이 높으니 안전하다”고 생각했지만, 내구성은 하드웨어 장애에 대한 것이고 “사람의 실수(삭제/덮어쓰기)” 복구는 별개라는 걸 깨달았다.  
문장에 “accidental deletion/overwrite를 복구해야 한다”는 요구가 명확할 때, 가장 직접적인 1순위 해법은?
A. S3 Versioning을 켠다  
B. S3 Replication(CRR)을 켠다  
C. Route 53 Failover 라우팅을 설정한다  
D. CloudFront를 붙인다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 신뢰성은 실패(여기서는 운영 실수)에서 “되돌릴 수 있는 메커니즘”을 갖추는 것이다. accidental 삭제/덮어쓰기 복구는 Versioning이 가장 직결된다.
- 소거법
  - B (근접 오답): 복제는 리전 DR/규제 요구에서 빛난다. “실수 복구”만이면 과할 수 있다.
  - D (명확히 틀림): 캐시/전송 계층이다.
  - C (명확히 틀림): DNS는 객체 버전 복구를 제공하지 않는다.
- 한 줄 규칙: “accidental deletion/overwrite”면 **S3 Versioning**.
- 태그: `pillar:reliability` `services:S3` `week:02` `day:03`

</details>

---

## Q2.

새 고객이 요구한다. “데이터는 다른 리전에도 복제돼야 합니다. 리전 장애가 나도 서비스는 계속돼야 해요.” 팀은 “백업”은 하고 있지만, 복제는 “항상 다른 곳에도 존재”하게 만드는 설계다.  
이 요구에서 SRR/CRR을 설계할 때 시험/실무에서 가장 자주 같이 확인해야 하는 필수 전제는?
A. 소스/대상 버킷 모두 Versioning이 켜져 있어야 한다  
B. CloudFront를 반드시 붙여야 한다  
C. S3 버킷은 퍼블릭이어야 복제가 된다  
D. DynamoDB PITR을 켜야 한다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 원격 복제는 DR/규제 요구를 만족시키는 신뢰성 설계다. 그리고 S3 Replication은 “버전 기반”이라 Versioning이 전제 조건으로 붙는다.
- 소거법
  - B (명확히 틀림): 캐시/전송 계층이다.
  - C (명확히 틀림): 접근 제어와 복제 기능은 별개다.
  - D (명확히 틀림): DynamoDB 기능이다.
- 한 줄 규칙: “S3 복제” 문제는 **Versioning 전제**가 같이 딸려온다.
- 태그: `pillar:reliability` `services:S3` `week:02` `day:03`

</details>

---

## Q3.

애플리케이션이 상태를 디스크(EBS)에 쓰는 워크로드다. 업데이트 도중 디스크가 꼬여 롤백이 필요해졌다. 인스턴스를 새로 띄워도 디스크 데이터가 없으면 의미가 없다.  
이 상황에서 “디스크(볼륨) 단위”의 백업/복구 기본 단위로 가장 적절한 것은?
A. EBS Snapshot  
B. S3 Versioning  
C. Route 53 Weighted routing  
D. CloudTrail Trail  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 실패에서 “데이터를 되돌리는 단위”가 핵심이다. 블록 스토리지(EBS) 복구는 스냅샷이 기본 단위다.
- 소거법
  - B (근접 오답): 객체 스토리지 실수 복구에 해당한다.
  - D (명확히 틀림): 행위 감사 로그다.
  - C (명확히 틀림): DNS/트래픽 분배다.
- 한 줄 규칙: “디스크 데이터 복구”면 **EBS Snapshot**.
- 태그: `pillar:reliability` `services:EBS` `week:02` `day:03`

</details>

---

## Q4.

문제 문장을 읽어보니 “리전 DR/규제/원격 복제” 같은 강한 신호는 없고, 핵심은 “실수로 삭제/덮어쓰기 했을 때 빠르게 되돌리고 싶다”는 운영 실수 복구다.  
이 경우 가장 먼저 떠올려야 할 1순위 해법은?
A. CloudFront를 붙인다  
B. S3 Versioning을 켠다  
C. 모든 데이터를 Glacier Deep Archive로 보낸다  
D. S3 Replication(CRR)을 무조건 켠다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 요구를 넘어서 과한 설계를 하면 비용/복잡도가 올라간다. 실수 복구만이면 Versioning이 가장 비용 효율적이고 직결된다.
- 소거법
  - D (근접 오답): 복제는 맞는 기술이지만 요구(실수 복구)에 비해 과하고 비용이 늘 수 있다.
  - C (명확히 틀림): 장기 보관 최적화로 “즉시 복구” 요구와 충돌할 수 있다.
  - A (명확히 틀림): 캐시/전송 계층이다.
- 한 줄 규칙: 요구가 “실수 복구”면 **Versioning 먼저**, “원격/DR”이면 replication.
- 태그: `pillar:cost-optimization` `services:S3` `week:02` `day:03`

</details>

---

## Q5. (복수정답: 2개)

요구사항이 두 축으로 동시에 들어왔다.  
1) “accidental deletion/overwrite를 복구”해야 한다(운영 실수 복구)  
2) “다른 리전에도 데이터가 복제”돼야 한다(리전 DR/규제)  
가장 자연스러운 구성 2개를 고르시오.
A. S3 버킷을 퍼블릭으로 연다  
B. CloudFront를 앞단에 둔다  
C. S3 Cross-Region Replication(CRR)을 설정한다  
D. Route 53 Failover를 설정한다  
E. 소스/대상 버킷 모두 Versioning을 켠다  
<details>
<summary>정답/해설</summary>

- 정답: C, E
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 실수 복구는 Versioning, 원격 복제는 CRR이 축이다. 그리고 CRR 자체가 Versioning 전제와 함께 나온다.
- 소거법
  - B (근접 오답): 성능/전송 최적화에는 도움되지만 “원격 복제” 요구를 만족시키지 않는다.
  - D (명확히 틀림): DNS 전환은 데이터 복제를 만들지 않는다.
  - A (명확히 틀림): 접근 제어/보안 요구와 반대다.
- 한 줄 규칙: “복제”가 보이면 **CRR + Versioning 전제**를 같이 챙긴다.
- 태그: `pillar:reliability` `services:S3` `week:02` `day:03`

</details>

---

