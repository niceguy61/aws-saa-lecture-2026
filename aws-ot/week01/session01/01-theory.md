# Theory

## Core Concepts

![Shared responsibility overview](./assets/core.svg)

### Why AWS matters for non-infra roles

- Developer: 기능 개발이 "서버 주문"이 아니라 "표준 서비스 조합"이 되면서 실험 속도가 빨라진다.
- PM or Planner: 요구사항이 리드타임과 비용 모델(고정비 vs 사용량 기반)을 어떻게 바꾸는지 설명할 수 있어야 우선순위를 제대로 잡는다.
- On-prem Ops: 장비 운영 중심에서 정책(IAM), 가시성(CloudWatch/CloudTrail), 자동화(ASG/IaC) 중심으로 운영 모델이 이동한다.

### Shared Responsibility Model (근거 기반)

- AWS 책임: 데이터센터 물리, 하드웨어/가상화, 기본 서비스 운영
- 고객 책임: 계정/권한, 데이터, 설정, 애플리케이션, 모니터링과 대응
- 왜 중요한가
  - 많은 사고는 "하드웨어 고장"이 아니라 "권한/설정 실수"에서 발생한다.
  - 그래서 AWS는 "인프라팀만" 아는 지식이 아니라, 기능 팀이 함께 알아야 하는 업무 언어가 된다.

### Region and AZ (가용성의 최소 단위)

- Region: 물리적으로 분리된 큰 단위(리전 간 지연/법규/재해 위험 고려)
- AZ: 리전 내 장애 격리 단위(AZ 분산은 SPOF 제거의 출발점)
- 왜 AZ가 시험/실무에서 반복되는가
  - "장애는 반드시 난다"라는 전제에서, 장애 영역을 줄이는 가장 단순한 설계가 AZ 분산이다.

## Key Takeaways (Must know)

- 보안 논의는 "누가 책임지나"를 먼저 합의해야 한다.
- 가용성 논의는 "어떤 장애를 가정하나(1 AZ, 1 Region)"부터 시작한다.
- 비용 논의는 "사용량 기반"이므로, 작은 실험은 쉬워지지만 방치 비용도 생긴다.

## Common Confusions (and why)

- "AWS가 보안을 다 해준다"는 오해
  - 왜 틀린가: 고객 책임(계정/권한/설정/데이터)이 사고의 주원인이기 때문이다.
- "멀티 AZ면 무조건 된다"는 오해
  - 왜 틀린가: 상태 저장(세션/DB), 배포 방식, 장애 조치가 함께 설계돼야 한다.

## Visual Mental Model (온프레미스 -> AWS)

| On prem term | AWS mapping idea | Why it matters |
|---|---|---|
| 데이터센터 | Region | 장애/법규/지연의 큰 단위 |
| 랙/스위치 | VPC/Subnet | 논리 네트워크로 모델링 |
| 방화벽 | SG/NACL | SG는 stateful, NACL은 stateless |
| 감사 로그 | CloudTrail | 누가 무엇을 했는지 근거 |

