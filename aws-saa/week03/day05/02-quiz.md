# 02-quiz - Week 03 Day 05 (Week Summary / Domain 3)

- 문항 수: 10 (Day05 규칙)
- 4지선다 = 정답 1개 / 5지선다 = 정답 2개(복수정답)
- 정답/해설은 `<details>`로 숨김

---

## Q1.

요구사항 문장에 “지속적으로 높은 CPU”, “일관된 성능”, “p95/p99 지연시간이 중요” 같은 신호가 있다. 그런데 선택지에 “싸니까 T 계열로 늘리자”가 있다.  
이때 더 자연스러운 방향은?
A. C/M 계열 등 지속 부하에 맞는 패밀리를 고려한다  
B. T 계열을 더 늘린다(항상 최적)  
C. CloudTrail을 켠다  
D. HDD(st1/sc1)로 바꾼다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: T는 burst에 강하지만 지속 부하에서 크레딧 소진/스로틀링 함정이 있다. 지속 고CPU 신호는 C/M 쪽이 자연스럽다.
- 소거법
  - B (근접 오답): 비용은 싸 보이지만 성능 요구를 못 맞추면 운영/비용이 악화된다.
  - D (명확히 틀림): 스토리지는 CPU 병목 해결책이 아니다.
  - C (명확히 틀림): 감사 로그는 성능 해결책이 아니다.
- 한 줄 규칙: “지속 고CPU/일관 성능”이면 **T가 아니라 C/M**.
- 태그: `pillar:performance-efficiency` `services:EC2` `week:03` `day:05`

</details>

---

## Q2. (복수정답: 2개)

T 계열 인스턴스에서 성능이 나빠졌는데 CPUUtilization만 보면 애매하다. “크레딧 소진”을 빠르게 확인하려 한다.  
CloudWatch에서 가장 먼저 같이 확인할 지표 2개는?
A. VolumeQueueLength  
B. FreeStorageSpace(RDS)  
C. CPUCreditUsage  
D. CloudFrontCacheHitRate  
E. CPUCreditBalance  
<details>
<summary>정답/해설</summary>

- 정답: C, E
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: 진단 루틴을 표준화하면 “CPU만 보고 스펙 업” 같은 실수를 줄인다. T 계열은 크레딧 지표가 직접 힌트다.
- 소거법
  - D (명확히 틀림): CloudFront 지표다.
  - A (근접 오답): I/O 병목 진단엔 유용하지만 크레딧 소진 확인의 1순위는 아니다.
  - B (명확히 틀림): RDS 지표다.
- 한 줄 규칙: “T + 성능 저하”면 **CreditBalance/Usage**부터 본다.
- 태그: `pillar:operational-excellence` `services:CloudWatch,EC2` `week:03` `day:05`

</details>

---

## Q3.

CPU는 여유인데 지연이 튄다. CloudWatch에서 `VolumeQueueLength`가 올라가고 I/O 지표가 포화돼 보인다. “용량은 충분한데 성능(IOPS/처리량)만 올리고 싶다”는 신호가 있다.  
가장 자연스러운 선택은?
A. 더 큰 인스턴스 타입으로만 스케일업한다  
B. S3 Versioning을 켠다  
C. gp3로 전환/튜닝해 IOPS/처리량을 조절한다  
D. Route 53 라우팅을 Failover로 바꾼다  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 비용 최적화 원칙 (Cost Optimization)
- 왜 이게 원칙에 맞나: 요구 축이 스토리지 I/O다. gp3는 “용량과 성능 분리”로 필요한 만큼만 성능을 맞추기 좋다.
- 소거법
  - A (근접 오답): 비용만 늘고 I/O 병목이 그대로일 수 있다.
  - B (명확히 틀림): 객체 실수 복구 기능이다.
  - D (명확히 틀림): DNS는 I/O 병목과 무관하다.
- 한 줄 규칙: “I/O 병목 신호”면 **EBS 타입/튜닝**으로 간다.
- 태그: `pillar:cost-optimization` `services:EBS` `week:03` `day:05`

</details>

---

## Q4.

Auto Scaling으로 웹 서버를 늘리자 업로드 파일이 인스턴스 로컬에 흩어져 사용자마다 보이는 파일이 다르다. rsync/NFS 직접 구성 같은 운영이 지옥이 된다.  
가장 자연스러운 선택은?
A. DynamoDB Scan으로 파일을 찾는다  
B. 각 인스턴스에만 저장하고 “운”에 맡긴다  
C. EFS로 공유 파일시스템을 마운트한다  
D. NACL을 모두 Allow로 바꾼다  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 운영 우수성 원칙 (Operational Excellence)
- 왜 이게 원칙에 맞나: “공유 파일” 요구는 올바른 레이어(EFS)에서 풀어야 운영이 단순해진다.
- 소거법
  - B (명확히 틀림): 요구사항과 충돌한다.
  - A (명확히 틀림): DB 조회와 파일 공유는 축이 다르다.
  - D (근접 오답): 네트워크를 열어도 공유 파일 문제가 해결되지 않는다.
- 한 줄 규칙: “여러 인스턴스가 같은 파일”이면 **EFS**.
- 태그: `pillar:operational-excellence` `services:EFS` `week:03` `day:05`

</details>

---

## Q5.

대규모 캠페인 후 해외 사용자 로딩이 느리고 S3 오리진 요청 수/비용이 튄다. 서버 CPU는 여유다. 캐시 가능한 정적 리소스가 대부분이다.  
가장 자연스러운 선택은?
A. CloudFront로 엣지 캐시를 붙인다  
B. Route 53 Simple 라우팅만 사용한다  
C. S3를 퍼블릭으로 열어 인증을 제거한다  
D. Global Accelerator로 정적 콘텐츠를 캐시한다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 정적 콘텐츠 지연/오리진 부하는 캐시로 푸는 게 축이다(CloudFront).
- 소거법
  - D (근접 오답): GA는 캐시가 아니라 경로/고정 IP 축이다.
  - B (근접 오답): DNS만으로 오리진 부하를 줄이지 못한다.
  - C (명확히 틀림): 보안 요구와 충돌할 수 있다.
- 한 줄 규칙: “정적/글로벌 지연”이면 **CloudFront**.
- 태그: `pillar:performance-efficiency` `services:CloudFront,S3` `week:03` `day:05`

</details>

---

## Q6.

실시간 기능(TCP/UDP)이 해외에서 지연이 들쭉날쭉하고, 고객사가 “고정 IP 화이트리스트”를 요구한다. 캐시할 성격이 아닌 트래픽이라 CDN만으로는 체감이 안 좋아진다.  
가장 자연스러운 선택은?
A. Global Accelerator  
B. S3 Replication  
C. CloudFront  
D. AWS Config  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: GA는 Anycast 고정 IP + AWS 백본 경로 최적화로 TCP/UDP 경로 변동 영향을 줄인다.
- 소거법
  - C (근접 오답): 캐시 축이다.
  - B (명확히 틀림): 데이터 DR 축이다.
  - D (명확히 틀림): 준수/상태 평가다.
- 한 줄 규칙: “고정 IP + 경로 최적화”면 **GA**.
- 태그: `pillar:performance-efficiency` `services:GlobalAccelerator` `week:03` `day:05`

</details>

---

## Q7.

DynamoDB에서 “status로도 조회해야 한다”는 요구가 추가됐다. 팀은 기존 키로는 Query가 안 되자 Scan으로 전체를 뒤지기 시작했고, 데이터가 커지자 지연/비용이 폭증한다.  
가장 자연스러운 해결은?
A. Scan을 더 자주 돌린다  
B. EBS 타입을 io2로 바꾼다  
C. Route 53 Weighted를 설정한다  
D. GSI를 추가해 새로운 액세스 패턴을 만든다  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: DynamoDB는 키/Query 경로 설계가 핵심이고, 새로운 조회 조건은 GSI로 푸는 게 정답 패턴이다.
- 소거법
  - A (명확히 틀림): Scan은 함정이다.
  - C (명확히 틀림): DNS는 조회 경로를 바꾸지 않는다.
  - B (명확히 틀림): 스토리지 I/O 튜닝과 무관하다.
- 한 줄 규칙: “새 조건”이면 **GSI**, Scan은 소거.
- 태그: `pillar:performance-efficiency` `services:DynamoDB` `week:03` `day:05`

</details>

---

## Q8.

“특정 고객만 느리다”, “특정 키에서만 throttling” 같은 문장이 있다. 전체가 아니라 일부만 느린 패턴이다.  
가장 자연스러운 원인/진단 포인트는?
A. Route 53 Failover 미구성  
B. CloudTrail 미설정  
C. 핫 파티션(키 분산 깨짐)  
D. CloudFront TTL 미설정  
<details>
<summary>정답/해설</summary>

- 정답: C
- 근거 원칙: 신뢰성 원칙 (Reliability)
- 왜 이게 원칙에 맞나: 특정 키 집중은 처리량을 불안정하게 만들어 스로틀링/지연을 유발한다(신뢰성 저하).
- 소거법
  - B (명확히 틀림): 감사 로그와 성능은 축이 다르다.
  - D (근접 오답): 캐시 문제처럼 보이게 하지만 DynamoDB 핫 파티션과는 무관하다.
  - A (명확히 틀림): DNS는 DB 키 분산과 무관하다.
- 한 줄 규칙: “특정 키만”이면 **핫 파티션**.
- 태그: `pillar:reliability` `services:DynamoDB` `week:03` `day:05`

</details>

---

## Q9.

홈 화면 추천처럼 “대부분 비슷한 데이터 반복 조회”가 많고, “몇 분 정도 지연은 허용”된다. DB 연결 수가 늘며 지연이 튄다.  
가장 자연스러운 선택은?
A. DynamoDB Scan  
B. Route 53 Geolocation  
C. NACL Allow-all  
D. ElastiCache  
<details>
<summary>정답/해설</summary>

- 정답: D
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 반복 읽기 핫패스는 캐시로 DB 호출 수를 줄이는 게 효과가 크다.
- 소거법
  - A (명확히 틀림): Scan은 느리고 비싸다.
  - C (명확히 틀림): 네트워크를 열어도 읽기 핫패스가 사라지지 않는다.
  - B (명확히 틀림): DNS는 DB 읽기 지연을 해결하지 못한다.
- 한 줄 규칙: “반복 읽기 + 약간의 지연 허용”이면 **캐시**.
- 태그: `pillar:performance-efficiency` `services:ElastiCache` `week:03` `day:05`

</details>

---

## Q10.

관계형 기능(조인/트랜잭션)은 유지해야 한다. 그런데 “읽기가 매우 많고 리포트/조회가 병목”이라는 문장이 강하다.  
가장 자연스러운 패턴은?
A. Aurora/RDS Read replica(읽기 확장)로 읽기 트래픽 분산  
B. Multi-AZ만 붙여 읽기 성능을 늘린다  
C. S3 Replication으로 읽기 성능을 늘린다  
D. DynamoDB로 무조건 전환한다  
<details>
<summary>정답/해설</summary>

- 정답: A
- 근거 원칙: 성능 효율성 원칙 (Performance Efficiency)
- 왜 이게 원칙에 맞나: 관계형을 유지하면서 읽기 병목을 풀 때 read replica/읽기 엔드포인트가 대표 패턴이다.
- 소거법
  - B (근접 오답): Multi-AZ는 HA(failover) 목적이지 read scaling 도구가 아니다.
  - D (근접 오답): 요구사항(관계형 기능)을 무시하면 오답이다.
  - C (명확히 틀림): 스토리지 DR 축이다.
- 한 줄 규칙: “관계형 + 읽기 많음”이면 **Read replica**.
- 태그: `pillar:performance-efficiency` `services:Aurora,RDS` `week:03` `day:05`

</details>

---

