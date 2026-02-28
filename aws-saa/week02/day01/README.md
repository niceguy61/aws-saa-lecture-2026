# Day 01 - Resilience fundamentals + Route 53 routing (Resilience: Route 53 + DR)

![고객 사례 삽화 - Route 53 라우팅](../../assets/scenario_image/w2d1s1.png)

## Quick Links

- [오늘의 이야기](#오늘의-이야기)
- [Timeline](#timeline-오늘-학습-타임라인)
- [Flow](#flow-서비스-연결-흐름)
- [Reading](#reading-서비스별-theory)
- [Quiz](#quiz)
- [References](../../references/README.md)

## 오늘의 이야기

월요일 아침에 장애 공지가 뜹니다. “주요 리전에서 장애가 나면 서비스가 얼마 안에 복구되어야 하나요?” 이 질문은 기술보다 먼저 **숫자(RPO/RTO)**가 필요해요. RTO가 짧으면 ‘빨리 켜지는’ 설계가 필요하고, RPO가 짧으면 ‘데이터를 얼마나 자주/어디까지’ 복제해야 하는지가 결정되죠. 그래서 오늘은 DR을 감으로 고르지 않고, 메뉴판처럼 RPO/RTO로 고르는 연습을 합니다. 백업/복구, 파일럿 라이트, 웜 스탠바이, 멀티 사이트처럼 선택지가 달라지는 이유를 말로 설명할 수 있으면, 시험에서도 실무에서도 설계가 흔들리지 않습니다.

그리고 그 복구 설계가 “사용자에게 실제로 전환되는 순간”은 대개 DNS에서 시작합니다. 여기서 Route 53이 등장하죠. “장애 조치”가 목적이면 Failover, “트래픽을 비율로 나누자”면 Weighted, “가까운 리전으로 보내자”면 Latency 같은 식으로 문장 신호가 있습니다. 결국 오늘의 스토리는 하나로 이어져요. **DR 전략으로 ‘어떻게 살아날지’를 정하고, Route 53 라우팅으로 ‘어떻게 보내줄지’를 결정한다.** 이 두 줄이 붙으면, 복구는 ‘운이 좋으면 되는 것’이 아니라 ‘설계대로 되는 것’이 됩니다.

실무에서는 이게 “전환 버튼”처럼 느껴집니다. 평소에는 Primary로 보내다가, 헬스 체크가 깨지면 Failover로 Secondary로 넘기고, 배포는 Weighted로 조금씩 흘려보내며 위험을 낮추고, 글로벌 사용자는 Latency로 가까운 곳으로 보내는 식이죠. 중요한 건 Route 53이 뭔가를 “복구”해주는 게 아니라, **복구 설계가 준비되어 있을 때 트래픽을 올바른 곳으로 ‘보내는’ 역할**이라는 점입니다. 그래서 오늘은 DR 전략과 라우팅 정책을 따로 외우지 않고, 같은 케이스 안에서 같이 굴리는 그림으로 정리합니다.

그리고 한 가지 더, DNS 전환은 “스위치”가 아니라 “캐시/TTL”의 영향을 받습니다. 장애가 났을 때 즉시 바뀌지 않는 것처럼 보일 수 있고, 그래서 RPO/RTO 요구를 맞추려면 라우팅 정책만이 아니라 전체 복구 흐름(데이터/컴퓨트/전환 지점)을 같이 봐야 해요. 오늘은 이 디테일까지 포함해서 “왜 이 선택지가 정답인지”를 한 문장으로 설명할 수 있게 만드는 걸 목표로 합니다.

## Timeline (오늘 학습 타임라인)

```mermaid
flowchart LR
  A[0-10m: 워밍업(RPO/RTO 2줄)] --> B[10-120m: Reading]
  B --> C[120-160m: 미니 정리(DR 메뉴판)]
  C --> D[160-210m: Trap drill(Route 53 정책 소거)]
  D --> E[210-240m: Quiz]
```

## Flow (서비스 연결 흐름)

```mermaid
flowchart LR
  Req[비즈니스 요구(RPO/RTO)] --> DR[DR 전략 선택]
  DR --> Target[복구 타겟(다른 AZ/리전/계정)]
  Client[사용자 요청] --> R53[Route 53 라우팅]
  R53 --> Primary[Primary]
  R53 --> Secondary[Secondary]
  DR --> Secondary
```

## Reading (서비스별 theory)

- [Route 53 Routing Policies (Failover/Weighted/Latency)](01-route53-routing.md)
- [DR Strategy Menu (RPO/RTO로 고르는 복구 전략)](02-dr-strategies.md)

## Quiz

- [Day 01 Quiz](03-quiz.md)

## Back

- `../README.md`
