# Day 02 - Theory Index (엣지 캐싱 + 네트워크 경로 최적화)

> 이 문서는 Day 이론 “인덱스”다. 상세 이론은 Day 폴더 바로 아래 `01-*.md` 서비스별 문서로 분리한다.

## 소개 (이게 뭔가요?)

- Day 02는 네트워크 성능 문제를 **“캐시(CloudFront)”**와 **“경로 최적화(Global Accelerator)”**로 구분해서 푸는 감각을 만든다.
- 시험에서 두 서비스를 섞어 놓고 “둘 다 빠르게 해준다”로 뭉개는 순간 오답이 된다.

## 고객 사례 (스토리)

글로벌 서비스가 성장하자, 사용자 불만의 대부분이 “느리다”로 모인다. 그런데 자세히 보면 두 종류다. 첫 번째는 정적 파일(이미지/JS/다운로드) 때문에 페이지가 늦게 뜨는 케이스다. 두 번째는 API 자체는 빠른데, 해외 사용자만 왕복 지연(RTT) 때문에 체감이 나쁜 케이스다. 팀은 “CDN을 붙이면 다 해결되겠지?”라고 생각하지만, 고객은 “게임/실시간 통신처럼 캐시할 수 없는 트래픽도 있다”고 한다.

여기서부터 선택이 갈린다. **캐시 가능한 콘텐츠/응답**이면 CloudFront가 압도적으로 강하다. TTL(Cache-Control)로 신선도를 조절하고, 필요할 때만 invalidation을 쓰면 오리진(S3/ALB 등) 호출이 줄어 지연/부하/비용이 같이 떨어진다. 반대로 **캐시가 목적이 아니라 네트워크 경로 자체**가 문제라면 Global Accelerator가 더 자연스럽다. Anycast 기반으로 가까운 엔트리 포인트로 붙이고, AWS 백본을 타고 최적 경로로 라우팅한다. 게다가 고정 IP가 필요하거나 멀티 리전 장애 조치가 요구될 때도 GA가 신호가 된다.

지금 문제 문장에는 “캐시 가능(정적/다운로드/TTL)” 신호가 더 강한가요, 아니면 “고정 IP/경로 최적화/TCP·UDP” 신호가 더 강한가요?

## Impact 범위 (어디에 영향을 주나?)

- Performance: 사용자 체감 지연(특히 글로벌) 개선
- Cost: 캐시 히트율이 높으면 오리진 트래픽/부하가 줄어 비용도 내려간다.
- Operations: invalidation 남발/캐시 키 설계는 운영 리스크가 된다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-3-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-3.4%20Network%20arch-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: CloudFront](https://img.shields.io/badge/Service-CloudFront-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Global%20Accelerator](https://img.shields.io/badge/Service-Global%20Accelerator-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 3: Design High-Performing Architectures
- Task focus:
  - 3.4 Determine high-performing and/or scalable network architectures

</details>

## Core Concepts

- 2가지 큰 갈래
  - 캐시: CloudFront (L7, 콘텐츠/응답 캐싱)
  - 경로 최적화: Global Accelerator (Anycast, 네트워크 경로)
- CloudFront 시험 포인트(자주 나오는 2개)
  - TTL/캐시 무효화(invalidation): 신선도 vs 비용/운영
  - 캐시 키: 개인화/정확도 vs 히트율/오리진 부하

![캐싱 레이어와 엣지](../../assets/core/caching-layers.svg)

## Service Theories (서비스별로 읽기)

- [CloudFront: TTL/캐시 키/무효화로 지연을 줄인다](01-cloudfront.md)
- [Global Accelerator: Anycast로 네트워크 경로를 최적화한다](02-global-accelerator.md)

## Exam must-know (요약)

- Key point: “글로벌 사용자 + 정적/캐시 가능”이면 CloudFront, “고정 IP/경로 최적화/TCP·UDP”면 Global Accelerator가 신호다.
- Why: 둘 다 ‘빠르다’지만, 메커니즘이 달라 정답이 갈린다(캐시 vs 라우팅).
- Alternative: “라우팅 정책(장애 조치/비율/지연)” 키워드면 Route 53 라우팅이 더 적절할 수 있다.

## Exam Traps

- 캐시가 가능한 상황에서 “오리진만 스케일 업”으로 끝내는 선택지
- invalidation을 남발하는 선택지(비용/운영 트레이드오프)
- GA를 “캐시 서비스”로 착각하는 선택지

## TL;DR (한 줄 정리)

- **캐시 가능한 콘텐츠/응답이면 CloudFront**, **캐시가 아니라 네트워크 경로/고정 IP가 문제면 Global Accelerator**가 정답 신호다.
