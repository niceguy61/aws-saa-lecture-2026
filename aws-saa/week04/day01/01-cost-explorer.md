# Cost Explorer: 비용을 “분해해서” 본다

## 소개 (이 서비스/주제는 무엇인가?)

- Cost Explorer는 AWS 비용을 서비스/리전/계정/태그 같은 축으로 **필터/그룹핑해서 분석**하는 도구다.

## 고객 사례 (스토리, 600~1000자)

이번 달 비용이 갑자기 2배가 됐다. 팀은 “요즘 배포가 많았으니 EC2가 늘었겠지”라고 짐작하지만, 근거가 없다. 그리고 이런 상황에서 가장 흔한 실수는 ‘일단 뭔가를 끄는 것’이다. 운 좋으면 비용이 줄지만, 보통은 다음 주에 장애가 난다.

Cost Explorer를 열고 먼저 기간을 맞춘 뒤, Group by를 바꿔가며 “어디서” 늘었는지 본다. Service로 보면 NAT Gateway나 데이터 전송이 튀어 있을 수 있고, Region으로 보면 특정 리전에만 트래픽이 몰렸을 수도 있다. 태그가 잘 붙어 있다면(예: CostCenter=TeamA) 팀별로도 바로 분해된다. 이렇게 비용을 한 번 분해하면, 최적화는 “선택지 비교”가 된다. 인스턴스를 줄일지, S3 클래스를 옮길지, NAT를 엔드포인트로 바꿀지의 우선순위가 잡힌다.

시험에서도 Cost Explorer는 “원인 분석/추세/그룹핑” 신호로 등장한다. “비용을 팀/프로젝트별로 나눠 보고 싶다”, “어느 서비스가 많이 나가는지 보고 싶다” 같은 문장이 나오면, Budgets가 아니라 Cost Explorer가 먼저 떠올라야 한다.

지금 문장은 “분석(원인/추세)”이 필요한가요, 아니면 “초과 알림”이 필요한가요?

## Impact 범위 (어디에 영향을 주나?)

- Cost: ‘감’이 아니라 ‘데이터’로 비용 드라이버를 찾는다.
- Operations: 최적화 우선순위가 명확해져 불필요한 변경을 줄인다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-Cost%20analysis-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Cost%20Explorer](https://img.shields.io/badge/Service-Cost%20Explorer-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 4: Design Cost-Optimized Architectures
- Objectives: 비용을 축(서비스/리전/태그)으로 분해해 원인을 설명할 수 있는지

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- Domain 4는 “최적화 아이디어”보다, 먼저 “무엇이 드라이버인지”를 찾는 흐름을 본다.

## VAKOG Anchors

- V(Visual): “비용 막대그래프를 Service/Region/Tag로 갈아 끼운다”를 떠올린다.
- A(Auditory): “분석은 Cost Explorer, 알림은 Budgets”를 말로 고정한다.
- O(Olfactory, smell test): “알림이 필요”한데 Cost Explorer만 고르는 답은 냄새가 난다.
- G(Gustatory, taste test): 요구 문장 1개로 Cost Explorer/Budgets를 고른다.

## Core Concepts

- Cost Explorer가 잘하는 것
  - 기간별 추세/비교
  - Filter + Group by(서비스/리전/계정/태그)
- Cost Explorer가 아닌 것
  - 예산 초과 알림/임계치 통제(이건 Budgets)

## Taste Test (1~3분)

- “비용이 어느 리전/어느 서비스에서 늘었는지 분석하고 싶다” → 무엇이 먼저 떠오르나요?

## Exam Traps (5-8)

- “초과 알림” 요구인데 Cost Explorer만 제시하는 선택지
- 태그가 없는데 “팀별 비용을 정확히 본다”는 선택지(가시화 전제가 없다)

## TL;DR (한 줄 정리)

- “원인 분석/그룹핑/추세”면 **Cost Explorer**가 정답 후보다.

## Back

- `./00-theory-index.md`
