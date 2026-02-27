# Quiz (Mock Questions) - Day 01

## Q1

**Scenario:** “장애 시 자동으로 secondary로 전환” 요구가 명확하다. Route 53에서 가장 적절한 라우팅 정책은?

A. Weighted  
B. Failover  
C. Simple  
D. Geolocation  

**Answer:** B  
**Explanation:** 헬스체크 기반 장애 조치 요구는 Failover 라우팅이 대표 정답 후보다.  
**Tags:** `domain:2` `services:Route53`

## Q2

**Scenario:** “점진적으로 새 버전 트래픽을 늘려” 배포하고 싶다. 적절한 Route 53 라우팅 정책은?

A. Weighted  
B. Failover  
C. Latency  
D. Multivalue answer  

**Answer:** A  
**Explanation:** 카나리/AB 테스트/점진 분산은 Weighted가 자연스럽다.  
**Tags:** `domain:2` `services:Route53`

## Q3

**Scenario:** RPO의 의미로 가장 적절한 것은?

A. 복구 시간 목표  
B. 복구 시점 목표(데이터 손실 허용량)  
C. 응답 시간 목표  
D. 비용 목표  

**Answer:** B  
**Explanation:** RPO는 허용 가능한 데이터 손실 시점이다.  
**Tags:** `domain:2` `services:DR`

## Q4

**Scenario:** RTO의 의미로 가장 적절한 것은?

A. 복구 시간 목표  
B. 복구 시점 목표  
C. 암호화 키 회전 주기  
D. 캐시 TTL  

**Answer:** A  
**Explanation:** RTO는 허용 가능한 복구 시간이다.  
**Tags:** `domain:2` `services:DR`

## Q5

**Scenario:** “글로벌 사용자에게 지연시간을 최소화”하고 싶다. Route 53에서 후보가 되는 라우팅 정책은?

A. Latency  
B. Failover  
C. Simple  
D. Geolocation(무조건)  

**Answer:** A  
**Explanation:** 지연시간 기반 라우팅 요구는 Latency가 직접적으로 매핑된다.  
**Tags:** `domain:2` `services:Route53`

## Q6

**Scenario:** 다음 중 DR 전략에서 일반적으로 “비용은 낮지만 RTO가 큰” 선택은?

A. Active/Active  
B. Warm standby  
C. Backup/Restore  
D. 멀티리전 상시 운영  

**Answer:** C  
**Explanation:** Backup/Restore는 비용은 낮지만 복구 시간이 길어지는 경향이 있다.  
**Tags:** `domain:2` `services:DR`

## Q7

**Scenario:** 단일 장애 지점(SPOF) 제거에 가장 직접적인 설계는?

A. 단일 AZ에 더 큰 인스턴스 1대  
B. Multi-AZ 분산 + 자동 복구  
C. CloudTrail 활성화  
D. KMS 키 생성  

**Answer:** B  
**Explanation:** AZ 분산과 자동 복구는 SPOF 제거의 기본 패턴이다.  
**Tags:** `domain:2` `services:HA`

## Q8

**Scenario:** Resilience와 Scalability에 대한 설명으로 가장 적절한 것은?

A. 둘은 항상 동일하다  
B. 확장성은 부하 대응, 복원력은 장애 대응에 더 직접적이다  
C. 복원력은 캐시만 의미한다  
D. 확장성은 보안 기능이다  

**Answer:** B  
**Explanation:** 시험에서는 요구사항 문장을 분리해 해석해야 한다.  
**Tags:** `domain:2` `services:Architecture`

