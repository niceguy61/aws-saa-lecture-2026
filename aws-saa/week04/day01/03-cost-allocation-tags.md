# Cost allocation tags: 팀/프로젝트 비용을 나눠 본다

## 소개 (이 서비스/주제는 무엇인가?)

- Cost allocation tags(비용 할당 태그)는 비용을 “팀/프로젝트/환경” 단위로 분해하기 위한 **가시성의 기준**이다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - 비용 할당 태그](../../assets/scenario_image/w4d1s3.png)

팀이 4개로 늘면서부터 비용 회의가 지옥이 됐다. “이번 달 비용은 누가 쓴 거죠?”를 아무도 답하지 못한다. 계정은 하나고, S3 버킷/EC2 이름도 제각각이다. 결국 비용을 ‘대충’ 나눠 부담하거나, 가장 큰 팀에게 떠넘기게 된다. 이러면 최적화가 아니라 정치가 된다.

태그를 표준화하면 상황이 바뀐다. 리소스를 만들 때 `CostCenter`, `Service`, `Env`, `Owner` 같은 태그를 붙이고, 비용 할당 태그를 활성화하면 Cost Explorer에서 그 태그로 Group by가 가능해진다. 그러면 “TeamA가 NAT를 많이 썼다”처럼 원인이 선명해지고, 해결도 선명해진다. “NAT를 엔드포인트로 바꾸자” 같은 대안이 근거를 얻는다.

여기서 중요한 건 “태그를 붙이자”가 아니라 “태그가 계속 붙게 하자”다. 키 이름이 팀마다 달라지면(예: costcenter vs CostCenter) 분석이 깨지고, 리소스가 태그 없이 만들어지면 다시 ‘추측’으로 돌아간다. 그래서 표준 키를 정하고, 가능하면 생성 시점에 자동으로 붙이거나(템플릿/파이프라인) 최소한 누락을 빨리 발견하는 흐름이 필요하다.

시험에서도 “팀/프로젝트별 비용을 나눠 보고 싶다(차지백/쇼백)”는 문장이 나오면, 태그 표준화(또는 계정 분리)가 먼저다. 할인 모델/스토리지 클래스 같은 최적화는 그 다음이다.

지금 당신 조직은 리소스 생성 시 태그를 ‘자동으로 강제’하고 있나요, 아니면 ‘권장’만 하고 있나요?

## Impact 범위 (어디에 영향을 주나?)

- Cost: 팀별/프로젝트별 비용 분해(차지백/쇼백)의 기반
- Operations: 태그 표준화 없이는 분석과 최적화가 반복해서 흔들린다

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-4-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-Cost%20allocation-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Concept: Tags](https://img.shields.io/badge/Concept-Tags-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Cost%20Explorer](https://img.shields.io/badge/Service-Cost%20Explorer-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 4: Design Cost-Optimized Architectures
- Objectives: 팀/프로젝트 비용 분리 요구를 태그/계정 구조로 연결할 수 있는지

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- 태그가 없으면 “최적화”는 맞아도 “설명”을 못 한다. 시험은 그 지점을 찌른다.

## VAKOG Anchors

- V(Visual): 리소스에 붙은 “색깔 라벨(태그)”로 비용이 쪼개지는 모습을 상상한다.
- A(Auditory): “팀별 비용=태그(또는 계정)”을 한 문장 규칙으로 말한다.
- O(Olfactory, smell test): 태그 없이 차지백이 된다는 답은 냄새가 난다.
- G(Gustatory, taste test): 요구 문장 1개를 보고 ‘태그’가 먼저 떠오르는지 확인한다.

## Core Concepts

- 태그 표준 키 예시
  - `CostCenter`, `Service`, `Env`, `Owner`
- 시험형 규칙
  - “팀/프로젝트별 비용” → 태그 표준화/강제 + Cost Explorer 분해

## Taste Test (1~3분)

- “서비스를 여러 팀이 함께 운영한다. 팀별로 비용을 나눠 보고 싶다” → 무엇부터 해야 할까요?

## Exam Traps (5-8)

- 태그 없이 “팀별 비용”을 정확히 분리하겠다는 선택지
- 태그 키가 팀마다 달라서(표준 없음) 분석이 안 되는 상황을 무시하는 선택지

## TL;DR (한 줄 정리)

- “팀/프로젝트 비용 분리”의 첫 단추는 **태그 표준화(그리고 가능하면 강제)**다.

## Back

- `./00-theory-index.md`
