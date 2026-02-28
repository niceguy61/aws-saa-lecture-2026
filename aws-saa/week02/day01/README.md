# Day 01 - Resilience fundamentals + Route 53 routing (Resilience: Route 53 + DR)

![고객 사례 삽화 - Route 53 라우팅](../../assets/scenario_image/w2d1s1.png)

## Outcomes

- 가용성/복구를 RPO/RTO 관점으로 설명하고, 설계 선택에 반영한다.
- 단일 장애 지점(SPOF)을 찾아 제거하는 기본 패턴(Multi-AZ, decoupling)을 말로 풀 수 있다.
- Route 53 라우팅 정책(Weighted/Failover/Latency)의 “언제 쓰는가”를 구분한다.

## Services In Scope

- Route 53 (routing policies, health checks 개념)
- (설계 개념) Multi-AZ, DR patterns

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [Route 53 Routing Policies (Failover/Weighted/Latency)](01-route53-routing.md)
- [DR Strategy Menu (RPO/RTO로 고르는 복구 전략)](02-dr-strategies.md)

## Core Concepts

- Resilience = “장애를 전제로” 유지되는 시스템 특성
  - HA(High Availability): 장애가 나도 서비스 지속(또는 빠른 자동 복구)
  - Fault tolerance: 장애 시에도 기능 유지(더 강한 요구, 비용↑)
- RPO/RTO
  - RPO: 허용 가능한 데이터 손실 시점(Recovery Point)
  - RTO: 허용 가능한 복구 시간(Recovery Time)
- SPOF 제거 패턴
  - AZ 분산(Multi-AZ)
  - stateless + Auto Scaling
  - decouple(큐/이벤트)

![DR strategies by RPO/RTO](../../assets/core/dr-rpo-rto-strategies.svg)

## Exam Traps (확장)

- “Failover가 필요”한데 Weighted를 고르는 실수(요구 문장에 health check/장애 조치가 있으면 Failover 후보).
- “Latency 기반” 요구인데 단일 리전 배포로 끝내는 실수.
- RPO/RTO를 “성능 지표”로 착각하는 선택지.
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “장애 조치”가 필요한 경우 Route 53에서 어떤 라우팅 정책이 자연스러운가?
- RPO/RTO 요구가 달라지면 DR 전략(backup/restore vs warm standby 등)은 어떻게 바뀌는가?
- “가용성”과 “확장성”은 같은 요구사항인가?

## TL;DR (한 줄 정리)

- “자동 전환/헬스체크/장애 조치”가 보이면 **Route 53 Failover(+ Health check)**, DR은 **RPO/RTO에 맞춰 전략을 고른다**.
