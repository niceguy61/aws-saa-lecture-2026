# 02-quiz - Week 02 Day 05 (Week Summary / Domain 2)

- 문항 수: 10 (Day05 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

요구사항이 명확하다. “장애가 나면 자동으로 secondary로 전환되어야 한다. DNS 단계에서 전환이 일어나고, 헬스 체크로 primary를 감지해야 한다.”  
Route 53에서 가장 자연스러운 라우팅 정책은?
A. Latency  
B. Simple  
C. Weighted  
D. Failover  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 헬스 체크 기반 장애 조치 요구는 Failover로 직결된다.
- 소거법
  - B (근접 오답): 요구가 없을 때의 단순 라우팅에 가깝다.
  - C (근접 오답): 비율/점진 배포가 목적일 때 맞다.
  - A (근접 오답): 지연 시간 최적화가 목적일 때 맞다.
- 한 줄 규칙: “health check + 장애 조치”면 **Failover**.
- 태그: `pillar:reliability` `services:Route53` `week:02` `day:05`

</details>

---

## Q2.

개발팀이 “점진 배포(카나리)”를 요구한다. “전체 트래픽 중 10%만 신규 버전으로 보내고, 문제가 없으면 30% → 100%로 늘리자.”  
Route 53에서 가장 자연스러운 라우팅 정책은?
A. Geolocation  
B. Failover  
C. Weighted  
D. Simple  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 비율 분배/점진 배포는 Weighted로 매핑된다.
- 소거법
  - B (근접 오답): 장애 조치가 목적이 아니다.
  - D (명확히 틀림): 비율 요구를 만족하지 못한다.
  - A (명확히 틀림): 위치 기반 요구가 아니다.
- 한 줄 규칙: “percentage/카나리”면 **Weighted**.
- 태그: `pillar:operational-excellence` `services:Route53` `week:02` `day:05`

</details>

---

## Q3.

리전 장애까지 포함한 DR 전략을 고르는 문제다. “항상 두 곳에서 완전히 돌아가게(Active/Active)”는 빠르지만 비싸고, “백업만”은 싸지만 느리다.  
재무팀이 “DR은 최소 비용으로 가자. 대신 복구가 느린 건 감수하자”라고 결정했다. 이때 가장 자연스러운 선택은?
A. Active/Active  
B. Warm standby  
C. Backup/Restore  
D. 멀티리전 상시 운영  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 비용을 낮추면 평소에 덜 띄워두게 되고, 복구 시간이 길어지는 경향이 있다.
- 소거법
  - A (명확히 틀림): 가장 비싼 편이다.
  - B (근접 오답): 백업보다는 빠르지만 비용이 올라간다.
  - D (명확히 틀림): 비용을 낮추는 방향이 아니다.
- 한 줄 규칙: “싸게” 가면 보통 **RTO가 길어진다**.
- 태그: `pillar:cost-optimization` `services:DR` `week:02` `day:05`

</details>

---

## Q4.

문장에 이런 요구가 있다. “HTTP host/path 기반 라우팅이 필요하고, WAF 연동을 고려한다.”  
가장 자연스러운 선택은?
A. NLB  
B. CloudFront  
C. ALB  
D. S3 Glacier  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: L7(HTTP 규칙) 요구는 ALB가 축이다.
- 소거법
  - A (근접 오답): L4 신호(TCP/정적 IP)가 강할 때 맞다.
  - B (명확히 틀림): 캐시/전송 계층이다.
  - D (명확히 틀림): 저장 클래스다.
- 한 줄 규칙: “host/path/WAF”면 **ALB**.
- 태그: `pillar:performance-efficiency` `services:ALB,ELB` `week:02` `day:05`

</details>

---

## Q5.

인스턴스 한 대가 죽으면 그 인스턴스로 붙은 사용자만 계속 오류를 겪는다. 운영자가 새벽에 수동 재기동하는 패턴을 제거하고, 헬스 체크 실패 시 자동으로 제외/교체(자가 치유)하고 싶다.  
가장 자연스러운 설계는?
A. Route 53 Simple routing  
B. S3 Versioning  
C. ASG + health check(필요 시 ELB health check)  
D. NACL을 모두 Allow  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 자가 치유는 “헬스체크 → 제외/교체” 흐름으로 만든다(ASG).
- 소거법
  - A (명확히 틀림): DNS는 교체 엔진이 아니다.
  - D (근접 오답): 네트워크를 열어도 자동 교체는 생기지 않는다.
  - B (명확히 틀림): 객체 실수 복구 기능이다.
- 한 줄 규칙: “자동 복구/교체”면 **ASG**.
- 태그: `pillar:reliability` `services:AutoScaling` `week:02` `day:05`

</details>

---

## Q6.

문장에 “accidental deletion/overwrite를 복구해야 한다”가 명시돼 있다. 재해(리전 장애) 수준이 아니라 운영 실수 복구가 핵심이다.  
가장 직접적인 1순위 해법은?
A. EBS Snapshot  
B. S3 Versioning  
C. Route 53 Failover  
D. S3 Replication(CRR)  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 운영 실수에서 되돌릴 수 있게 만드는 메커니즘이 Versioning이다.
- 소거법
  - D (근접 오답): 원격 DR/규제 신호가 없으면 과할 수 있다.
  - A (명확히 틀림): 블록 스토리지 복구 단위다.
  - C (명확히 틀림): DNS 전환이다.
- 한 줄 규칙: “accidental”이면 **Versioning**.
- 태그: `pillar:reliability` `services:S3` `week:02` `day:05`

</details>

---

## Q7.

요구사항이 “다른 리전에도 데이터가 복제돼야 한다(리전 DR/규제)”다. 시험에서 복제 설정을 고를 때 같이 따라오는 전제 조건을 빠뜨리면 오답이 된다.  
S3 Replication(SRR/CRR)의 필수 전제는?
A. CloudFront를 반드시 붙여야 한다  
B. 소스/대상 버킷 모두 Versioning이 켜져 있어야 한다  
C. 모든 객체가 Glacier여야 한다  
D. 버킷은 퍼블릭이어야 한다  
<details>
<summary>정답/해설</summary>

- 정답: B
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 복제는 버전 기반이라 Versioning 전제가 같이 나온다.
- 소거법
  - A (명확히 틀림): 캐시/전송 계층이다.
  - D (명확히 틀림): 접근 제어와 복제 기능은 별개다.
  - C (명확히 틀림): 저장 클래스와 무관하다.
- 한 줄 규칙: “S3 복제”는 **Versioning 전제** 체크.
- 태그: `pillar:reliability` `services:S3` `week:02` `day:05`

</details>

---

## Q8.

상태를 디스크(EBS)에 쓰는 워크로드에서 업데이트 도중 디스크가 꼬여 롤백이 필요하다. 인스턴스를 새로 띄워도 디스크 데이터가 없으면 의미가 없다.  
이 상황에서 가장 직접적인 백업/복구 단위는?
A. EBS Snapshot  
B. GuardDuty  
C. Route 53 Weighted  
D. S3 Versioning  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 블록 스토리지 복구는 스냅샷이 기본 단위다.
- 소거법
  - D (근접 오답): 객체 스토리지 실수 복구다.
  - C (명확히 틀림): DNS/트래픽 분배다.
  - B (명확히 틀림): 탐지 서비스다.
- 한 줄 규칙: “디스크 복구”면 **Snapshot**.
- 태그: `pillar:reliability` `services:EBS` `week:02` `day:05`

</details>

---

## Q9.

문장에 “자동 장애 조치(failover)”가 강하게 들어 있다. 읽기 성능 확장은 부차적이다.  
RDS/Aurora에서 가장 자연스러운 선택은?
A. Route 53 Latency routing  
B. S3 Replication  
C. Multi-AZ  
D. Read replica  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 가용성/자동 장애 조치는 Multi-AZ로 매핑된다.
- 소거법
  - D (근접 오답): 읽기 확장 도구다.
  - B (명확히 틀림): S3 기능이다.
  - A (명확히 틀림): DNS 라우팅이다.
- 한 줄 규칙: “failover”면 **Multi-AZ**.
- 태그: `pillar:reliability` `services:RDS,Aurora` `week:02` `day:05`

</details>

---

## Q10. (복수정답: 2개)

요구사항이 동시에 들어왔다.  
1) “장애 시 자동 failover”(가용성)  
2) “read-heavy라 읽기 성능 확장”(읽기 분산)  
두 요구를 가장 자연스럽게 만족하는 구성 2개를 고르시오.
A. CloudTrail Trail 생성  
B. Multi-AZ 구성  
C. Read replica 추가  
D. NACL을 모두 Allow로 바꾸기  
E. S3 Versioning 켜기  
<details>
<summary>정답/해설</summary>

- 정답: B, C
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 요구를 분해해 각각의 기능에 매핑해야 한다. failover=Multi-AZ, read scaling=Read replica.
- 소거법
  - E (명확히 틀림): 객체 스토리지 실수 복구다.
  - A (근접 오답): 감사엔 유용하지만 가용성/읽기 확장의 답은 아니다.
  - D (명확히 틀림): 네트워크를 열어도 DB 기능이 생기지 않는다.
- 한 줄 규칙: “가용성 vs 읽기 확장”을 분리하고 **Multi-AZ + RR**로 조합한다.
- 태그: `pillar:reliability` `services:RDS,Aurora` `week:02` `day:05`

</details>

---

