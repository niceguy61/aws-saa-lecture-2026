# Quiz (Mock Questions) - Day 02

## Q1

**Scenario:** 전 세계 사용자에게 정적 콘텐츠를 빠르게 제공해야 한다. 가장 적절한 서비스는?

A. CloudFront  
B. KMS  
C. CloudTrail  
D. SQS  

**Answer:** A  
**Explanation:** 글로벌 엣지 캐시는 지연과 오리진 부하를 줄이는 대표 선택지다.  
**Tags:** `domain:3` `services:CloudFront`

## Q2

**Scenario:** CloudFront에서 쿼리 스트링을 캐시 키에 포함시키면 일반적으로 어떤 영향이 있을 수 있는가?

A. 캐시 히트율이 낮아질 수 있다  
B. 항상 히트율이 높아진다  
C. RPO가 줄어든다  
D. DDoS가 자동 차단된다  

**Answer:** A  
**Explanation:** 키가 세분화되면 변종이 늘어 히트율이 떨어질 수 있다.  
**Tags:** `domain:3` `services:CloudFront`

## Q3

**Scenario:** 오리진 객체가 변경됐는데도 사용자가 이전 버전을 본다. 빠르게 갱신하려면?

A. Invalidation 생성  
B. SCP 적용  
C. DLQ 설정  
D. KMS key rotation  

**Answer:** A  
**Explanation:** 캐시 무효화는 즉시성 있는 갱신 수단이다.  
**Tags:** `domain:3` `services:CloudFront`

## Q4

**Scenario:** Global Accelerator와 CloudFront 차이로 가장 적절한 것은?

A. 둘 다 캐시 서비스다  
B. CloudFront는 캐시, GA는 네트워크 경로 최적화(개념)  
C. GA는 KMS 키를 관리한다  
D. CloudFront는 DB 복제 서비스다  

**Answer:** B  
**Explanation:** 시험은 “캐시 vs 네트워크 가속”을 구분시키려 한다.  
**Tags:** `domain:3` `services:CloudFront,GlobalAccelerator`

## Q5

**Scenario:** CloudFront를 정답 후보로 올리는 요구 문장으로 가장 자연스러운 것은?

A. “정적 콘텐츠를 글로벌로 빠르게 제공”  
B. “관계형 조인 쿼리가 필요”  
C. “시크릿 rotation이 필요”  
D. “SQS로 버퍼링 필요”  

**Answer:** A  
**Explanation:** 글로벌 캐시 요구는 CloudFront의 정석 신호다.  
**Tags:** `domain:3` `services:CloudFront`

