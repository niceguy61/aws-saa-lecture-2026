# Security Group vs NACL (네트워크 문지기 2종)

## 소개 (이게 뭔가요?)

- Security Group(SG)은 인스턴스/ENI 단위의 상태 저장 방화벽이고, NACL은 서브넷 단위의 무상태 필터다.
- 시험에서는 “둘을 섞어서 말하는 선택지”가 단골 함정이다.

## 고객 사례 (스토리, 600~1000자)

![고객 사례 삽화 - SG vs NACL](../../assets/scenario_image/w1d4s1.png)

백엔드를 프라이빗 서브넷에 올리자 갑자기 연결이 안 된다. 개발자는 SG 인바운드를 열고 다시 테스트한다. 그래도 안 된다. 누군가 “NACL도 열어야 한다”고 한다. 그런데 무엇을 어디까지 열어야 하는지 감이 없다. 운영자는 “열어두면 되는 것 아닌가”라고 하지만, 보안팀은 “최소 권한”을 요구한다. 이때 SG와 NACL의 차이를 모르고 열어버리면, 문제는 해결되지만 위험만 남는다.

핵심은 축이 다르다는 것이다. SG는 인스턴스(ENI)에 붙고 상태 저장이라 리턴 트래픽을 자동으로 허용한다. 반대로 NACL은 서브넷 레벨이고 무상태라, 인바운드만 열면 끝이 아니라 아웃바운드/리턴 포트까지 고려해야 한다. 시험에서도 “NACL은 allow only” 같은 문장이나 “SG는 deny 가능” 같은 문장이 나오면 오답을 유도하는 신호다. 즉, SG는 ‘애플리케이션 포트 문’이고, NACL은 ‘서브넷 경계의 출입 통제’다. 둘의 역할을 분리하면, 무엇을 열어야 하는지(그리고 무엇을 열면 안 되는지)가 명확해진다.

실무 트러블슈팅에서도 같은 패턴이 반복된다. “인바운드는 열었는데 연결이 안 된다”면, SG가 아니라 NACL의 리턴 트래픽/에페메랄 포트가 막힌 경우가 자주 나온다. 그래서 NACL은 ‘추가 방어선’으로 쓰되, 기본 방어는 SG로 잡는 설계가 더 흔하다.

지금 연결 문제를 보고, SG 문제일까요? NACL 문제일까요? 구분 기준은 무엇인가요?

## Impact 범위 (어디에 영향을 주나?)

- Security: 네트워크 경계에서 최소 노출을 만드는 기본기
- Operations: 연결 장애(타임아웃) 트러블슈팅 속도를 좌우

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.2%20Network%20boundaries-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Security%20Group](https://img.shields.io/badge/Service-Security%20Group-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus: 네트워크 경계(SG/NACL) 개념 구분

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- SG/NACL 혼동은 오답으로 직결된다.
- NACL은 무상태라 리턴 트래픽을 “명시적으로” 고려해야 한다.

## Core Concepts

| Topic | Security Group | NACL |
|---|---|---|
| Scope | ENI/인스턴스(논리적) | Subnet |
| State | Stateful | Stateless |
| Rule type | Allow only | Allow + Deny |
| Return traffic | 자동 허용(상태 저장) | 명시적 허용 필요 |

```mermaid
flowchart TB
  subgraph Subnet
    N[NACL]
    I[Instance ENI]
    SG[Security Group]
  end
  N --> SG --> I
```

## Deep Dive

### 언제 SG로 풀고, 언제 NACL이 필요한가

- **기본 방어선(대부분의 케이스)**: SG로 “인스턴스/ENI 단위 최소 노출”을 만든다. 애플리케이션 포트(예: 443)만 열고, 나머지는 닫아두는 방식이 자연스럽다.
- **서브넷 단위 가드레일이 필요할 때**: 특정 서브넷 전체에 공통 규칙(예: 특정 CIDR 차단, 특정 포트 차단)을 걸어야 하거나, “Deny가 꼭 필요”한 요구가 있을 때 NACL이 후보로 올라온다.

### NACL에서 자주 터지는 장애 패턴(무상태의 대가)

NACL은 **stateless**라서 “요청 트래픽을 허용”하는 것만으로 끝나지 않는다.

- 인바운드 허용 후에도 **아웃바운드(리턴 트래픽)** 규칙이 막히면 타임아웃이 난다.
- 특히 클라이언트가 사용하는 **에페메랄 포트(임시 포트)** 범위를 고려하지 않으면, “포트는 열었는데도 안 됨” 같은 증상이 반복된다.

즉, 시험에서 “인바운드는 열었는데 계속 타임아웃” 신호가 보이면 SG보다 **NACL 리턴 트래픽**을 먼저 의심하는 흐름이 자연스럽다.

### 자주 나오는 디테일(룰 순서/에페메랄 포트)

- NACL은 보통 **룰 번호/우선순위** 개념이 따라오므로, “어떤 규칙이 먼저 적용되는가”가 함정 포인트가 될 수 있다.
- 리턴 트래픽은 애플리케이션 포트만이 아니라 **클라이언트 임시 포트(에페메랄 포트)**가 함께 걸릴 수 있어, “80/443만 열었는데도 안 됨” 같은 증상이 설명된다.

### Best Practices (운영 관점)

- SG는 “허용 리스트(allow list)”로 단순하게 유지하는 편이 운영에 유리하다(규칙이 많아질수록 사고가 난다).
- NACL은 룰 번호/우선순위까지 포함해 관리해야 하므로, “그냥 다 열어두자”로 가면 오히려 운영/보안 리스크가 커진다.

### 핵심 정리 (Deep Dive)

- **SG=인스턴스/상태 저장/Allow only**, **NACL=서브넷/무상태/Allow+Deny**.
- “리턴 트래픽을 자동 허용”은 SG 신호, “리턴까지 명시”는 NACL 신호다.

## Quick Comparison Table

| Symptom | Likely cause | First check |
|---|---|---|
| 인바운드 열었는데 응답 없음 | NACL 리턴 포트 미허용 | NACL 아웃바운드/리턴 |

## Exam Traps (확장)

- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`
- “SG에 Deny 규칙 추가” 같은 선택지
- “NACL은 stateful” 같은 선택지

## Exam Trap Drill (O/X, 1~3분)

- “리턴 트래픽을 자동 허용”하는 쪽은 SG일까, NACL일까?

## TL;DR (한 줄 정리)

- **SG는 상태 저장(ENI 단위)**, **NACL은 무상태(서브넷 단위)**다.

## Back

- `./README.md`
