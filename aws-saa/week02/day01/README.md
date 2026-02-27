# Day 01 - Resilience fundamentals + Route 53 routing

## Outcomes

- 가용성/복구를 RPO/RTO 관점으로 설명하고, 설계 선택에 반영한다.
- 단일 장애 지점(SPOF)을 찾아 제거하는 기본 패턴(Multi-AZ, decoupling)을 말로 풀 수 있다.
- Route 53 라우팅 정책(Weighted/Failover/Latency)의 “언제 쓰는가”를 구분한다.

## Services In Scope

- Route 53 (routing policies, health checks 개념)
- (설계 개념) Multi-AZ, DR patterns

## Timebox (4h)

- Theory: 3h
- Hands-on (console): 1h

## Exam-Style Design Questions

- “장애 조치”가 필요한 경우 Route 53에서 어떤 라우팅 정책이 자연스러운가?
- RPO/RTO 요구가 달라지면 DR 전략(backup/restore vs warm standby 등)은 어떻게 바뀌는가?
- “가용성”과 “확장성”은 같은 요구사항인가?

