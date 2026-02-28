# Right sizing + Auto Scaling: 측정하고, 비피크를 줄인다

## 소개 (이 서비스/주제는 무엇인가?)

- right sizing은 “스펙 줄이기”가 아니라, **요구사항을 만족하는 최소 리소스**를 측정해서 찾는 작업이다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - right sizing과 스케줄 축소](../../assets/scenario_image/w4d2s2.png)

팀은 비용이 부담돼 인스턴스를 작은 타입으로 바꾸려 한다. 그런데 한 번 내리면 장애가 나고, 다시 올리면 “최적화는 실패했다”가 된다. 이유는 단순하다. 어떤 리소스가 병목인지, 지금 스펙이 과한지 부족한지 측정이 없기 때문이다. CPU만 보고 내려도, 실제 병목이 메모리/네트워크/I/O면 결과는 더 나빠진다.

그래서 right sizing은 지표에서 시작한다. CloudWatch에서 CPU/네트워크/I/O를 보고, 가능하면 p95/p99 같은 앱 지표도 함께 본다. “실제로 얼마나 쓰는지”가 나오면 스펙을 내릴지 유지할지 판단이 된다. 그리고 비용 최적화에서 더 큰 레버리지는 “항상 켜두는 낭비”를 줄이는 것이다. 비피크가 명확한 업무 시스템이라면 Auto Scaling의 scheduled action으로 “업무시간만 1, 야간 0” 같은 패턴이 큰 절감을 만든다.

또 한 가지는 “피크만 버티면 된다”는 요구다. 이때 스펙 업으로 끝내면, 24시간 내내 비싼 스펙을 유지하게 된다. 반대로 Auto Scaling으로 피크만 늘리면, 비용을 요구사항에 맞춰 지불할 수 있다. 시험에서도 “비피크에 트래픽이 없다”, “업무시간만 필요하다” 같은 신호가 나오면 scheduled scaling이 후보가 된다. 즉 비용 최적화는 스펙이 아니라 운영 패턴까지 포함한 설계다.

지금 시나리오에는 “비피크 시간대”가 명확히 존재하나요?

## Impact 범위 (어디에 영향을 주나?)

- Cost: 비피크 축소(야간 0)가 큰 절감이 된다.
- Reliability: 측정 없이 스펙을 내리면 요구사항을 깨기 쉽다.
- Operations: 스케줄/자동화가 있으면 운영이 단순해진다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-Right%20sizing%20%26%20ASG-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Auto%20Scaling](https://img.shields.io/badge/Service-Auto%20Scaling-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: CloudWatch](https://img.shields.io/badge/Service-CloudWatch-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 4: Design Cost-Optimized Architectures
- Objectives: 측정 기반 right sizing과 scheduled scaling 같은 운영 패턴을 선택할 수 있는지

</details>

## Core Concepts

- right sizing 신호
  - CPU/메모리/네트워크/I/O 지표(CloudWatch)
  - p95/p99 지연(앱 지표)
- 비용 최적화 패턴
  - 피크만 확장, 비피크는 축소
  - Scheduled scaling으로 “야간 0”(워크로드 성격에 따라)

## Exam Traps (확장)

- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`
- “측정/지표” 없이 스펙만 내리는 선택지
- “비피크가 없다”는데 scheduled scaling을 무리하게 적용하는 선택지

## Exam Trap Drill (O/X, 1~3분)

- “업무시간 외에는 트래픽이 거의 없다” → 무엇이 먼저 떠오르나요?

## TL;DR (한 줄 정리)

- right sizing은 **측정 기반**, 큰 절감은 **비피크 축소(스케줄/자동 확장)**에서 자주 나온다.

## Back

- `./README.md`
