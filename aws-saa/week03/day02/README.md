# Day 02 - Edge + network performance (엣지 캐싱 + 네트워크 경로 최적화)

![고객 사례 삽화 - 캐시 vs 경로 최적화](../../assets/scenario_image/w3d2s0.png)

## Outcomes

- CloudFront의 성능 가치(엣지 캐시/오리진 부하 감소)를 설명한다.
- 캐시 키(쿼리/헤더/쿠키) 선택이 캐시 히트율에 미치는 영향을 설명한다.
- Global Accelerator(개념)와 CloudFront의 차이를 “캐시 vs 네트워크 가속”으로 구분한다.

## Services In Scope

- CloudFront (cache behaviors, TTL, invalidation 개념)
- (개념) Global Accelerator, Route 53 latency

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [CloudFront: TTL/캐시 키/무효화로 지연을 줄인다](01-cloudfront.md)
- [Global Accelerator: Anycast로 네트워크 경로를 최적화한다](02-global-accelerator.md)

## Core Concepts

- 2가지 큰 갈래
  - 캐시: CloudFront (L7, 콘텐츠/응답 캐싱)
  - 경로 최적화: Global Accelerator (Anycast, 네트워크 경로)
- CloudFront 시험 포인트(자주 나오는 2개)
  - TTL/캐시 무효화(invalidation): 신선도 vs 비용/운영
  - 캐시 키: 개인화/정확도 vs 히트율/오리진 부하

![캐싱 레이어와 엣지](../../assets/core/caching-layers.svg)

## Exam Traps (확장)

- 캐시가 가능한 상황에서 “오리진만 스케일 업”으로 끝내는 선택지
- invalidation을 남발하는 선택지(비용/운영 트레이드오프)
- GA를 “캐시 서비스”로 착각하는 선택지
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- 전 세계 사용자 지연을 줄이려면 CloudFront가 정답인 신호는?
- 쿼리 스트링을 캐시 키에 넣으면 어떤 트레이드오프가 생기는가?
- Global Accelerator와 CloudFront 중 무엇이 더 적절한가(요구 문장 기반)?

## TL;DR (한 줄 정리)

- **캐시 가능한 콘텐츠/응답이면 CloudFront**, **캐시가 아니라 네트워크 경로/고정 IP가 문제면 Global Accelerator**가 정답 신호다.
