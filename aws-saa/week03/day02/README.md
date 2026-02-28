# Day 02 - Edge + network performance (엣지 캐싱 + 네트워크 경로 최적화)

![고객 사례 삽화 - 캐시 vs 경로 최적화](../../assets/scenario_image/w3d2s0.png)

## Quick Links

- [오늘의 이야기](#오늘의-이야기)
- [Timeline](#timeline-오늘-학습-타임라인)
- [Flow](#flow-서비스-연결-흐름)
- [Reading](#reading-서비스별-theory)
- [Quiz](#quiz)
- [References](../../references/README.md)

## 오늘의 이야기

글로벌 서비스에서 성능 이슈가 터지면 회의가 이렇게 시작됩니다. “해외에서만 느리대요. 서버는 괜찮다는데요?” 이때 답은 두 갈래로 나뉩니다. 응답 자체를 반복해서 써먹을 수 있다면 **CloudFront** 같은 캐시가 답이고, 캐시할 수 없지만 네트워크 경로가 문제라면 **Global Accelerator** 같은 경로 최적화가 답이죠. 오늘은 이 차이를 ‘말로’ 설명하는 연습을 합니다. CloudFront는 엣지에서 응답을 캐싱해서 오리진 부하를 줄이고, TTL/캐시 키(쿼리/헤더/쿠키) 설계로 히트율을 끌어올리는 게 핵심입니다. 반대로 Global Accelerator는 캐시가 아니라 Anycast 기반으로 네트워크 경로를 최적화하고 고정 엔드포인트를 제공하는 쪽에 가깝습니다.

실무에서도 선택은 문장으로 결정됩니다. “정적/반정적 콘텐츠”, “오리진 부하 감소”, “캐시로 빠르게”라는 신호가 보이면 CloudFront가 자연스럽고, “캐시가 안 된다”, “전 세계에서 TCP/UDP 경로를 안정적으로”, “고정 IP가 필요” 같은 문장이 나오면 Global Accelerator가 떠야 해요. 오늘의 결론은 간단합니다. **캐시냐 경로냐**. 이걸 먼저 갈라야, TTL/무효화(invalidation) 같은 비용·운영 트레이드오프도 제대로 판단할 수 있습니다.

CloudFront를 쓸 때도 “켜면 빨라진다”로 끝나지 않습니다. 캐시 키를 어떻게 잡느냐(쿼리/헤더/쿠키)에 따라 히트율이 완전히 달라지고, invalidation을 남발하면 비용/운영 부채가 생길 수 있어요. 반대로 Global Accelerator는 캐시가 아니라, 경로/엔드포인트 문제를 해결해주는 도구라서 “개인화 응답이라 캐시가 힘들다” 같은 조건에서 더 빛납니다. 오늘 Day는 이 둘을 비교해서 외우는 게 아니라, 문장을 읽고 “지금은 캐시 레버를 당길 타이밍인지, 경로 레버를 당길 타이밍인지”를 바로 판정하는 감각을 만드는 데 초점을 둡니다.

정리하자면, CloudFront는 캐시 behaviors/TTL/키 설계가 성패를 좌우하고, Global Accelerator는 “캐시 없이도” 전 세계 네트워크 경로를 안정화하는 쪽에 강점이 있습니다. 오늘은 이 결론을 한 문장으로 말해보는 연습까지 하고 넘어갑니다.

## Timeline (오늘 학습 타임라인)

```mermaid
flowchart LR
  A[0-10m: 워밍업(캐시 vs 경로)] --> B[10-120m: Reading]
  B --> C[120-150m: 미니 정리(TTL/캐시 키)]
  C --> D[150-210m: Trap drill(GA를 캐시로 착각)]
  D --> E[210-240m: Quiz]
```

## Flow (서비스 연결 흐름)

```mermaid
flowchart LR
  Users[Global users] --> Choice{캐시 가능?}
  Choice -- Yes --> CF[CloudFront<br/>(엣지 캐시)]
  Choice -- No --> GA[Global Accelerator<br/>(경로 최적화)]
  CF --> Origin[Origin]
  GA --> Origin
```

## Reading (서비스별 theory)

- [CloudFront: TTL/캐시 키/무효화로 지연을 줄인다](01-cloudfront.md)
- [Global Accelerator: Anycast로 네트워크 경로를 최적화한다](02-global-accelerator.md)

## Quiz

- [Day 02 Quiz](03-quiz.md)

## Back

- `../README.md`
