# VPC 보안 경계 + VPC Endpoints/PrivateLink

## 소개 (이게 뭔가요?)

- SG/NACL은 “네트워크 문지기”이고, VPC Endpoints/PrivateLink는 “인터넷을 거치지 않는 사설 길”이다.
- 시험에서는 NAT를 당연하게 쓰지 말고, **사설 경로/비용/보안** 신호가 있으면 Endpoints가 먼저다.

## 고객 사례 (스토리)

보안팀이 말했다. “백엔드는 프라이빗 서브넷에만 두고, 인터넷으로는 절대 나가면 안 돼요.” 그런데 개발팀은 S3에 파일을 올리고 내려받아야 한다. 처음엔 NAT Gateway를 붙였더니 기능은 되는데 비용이 생각보다 크고, “인터넷을 경유했다”는 사실 자체가 찜찜하다. 또 한 명이 묻는다. “그럼 보안 그룹에서 S3를 막으면 되죠?” — 여기서부터 함정이 시작된다.

SG(Security Group)는 인스턴스(ENI)에 붙는 ‘출입문’이고, NACL은 서브넷의 ‘건물 경비’다. 둘의 축이 다르다. S3는 SG 대상으로 막는 게 아니라, 버킷 정책이나 VPC Endpoint policy 같은 “리소스/경로” 쪽에서 통제한다. 그래서 VPC Endpoints를 쓰면, 프라이빗 서브넷에서 S3/DynamoDB로 가는 사설 길을 만들 수 있다(게이트웨이 엔드포인트). 다른 서비스는 Interface Endpoint(PrivateLink)로 ENI 형태의 사설 엔드포인트를 둔다. NAT는 “일반 인터넷 아웃바운드”가 필요할 때 후보지만, 문제에서 “사설/비용 절감” 신호가 보이면 엔드포인트가 우선이다.

지금 요구가 “인터넷 없이 S3 접근”이라면, NAT와 Endpoint 중 어떤 선택이 더 자연스럽나요?

## Impact 범위 (어디에 영향을 주나?)

- Security: 프라이빗 서브넷 설계, 데이터 유출 경로(인터넷 경유) 차단과 직결된다.
- Cost: NAT Gateway 비용을 줄이는 대표 카드가 VPC Endpoints다.

## Exam Guide (Badges)

![Domain](https://img.shields.io/badge/Domain-1-0ea5e9?style=flat&logo=amazonwebservices&logoColor=white)
![Task](https://img.shields.io/badge/Task-1.2%20Network%20boundaries-22c55e?style=flat&logo=amazonwebservices&logoColor=white)
![Service: VPC](https://img.shields.io/badge/Service-VPC-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: Security%20Group](https://img.shields.io/badge/Service-Security%20Group-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: NACL](https://img.shields.io/badge/Service-NACL-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: VPC%20Endpoints](https://img.shields.io/badge/Service-VPC%20Endpoints-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)
![Service: PrivateLink](https://img.shields.io/badge/Service-PrivateLink-8b5cf6?style=flat&logo=amazonwebservices&logoColor=white)

<details>
<summary>Exam guide mapping (details)</summary>

- Domain: Domain 1: Design Secure Architectures
- Task focus:
  - 1.1 Design secure access to AWS resources (프라이빗 접근/경계)
  - 1.2 Design secure workloads and applications (네트워크 경계)

</details>

## Why This Matters (시험/실무에서 걸리는 지점)

- “Private subnet에서 S3 접근” 문제는 거의 항상 **NAT vs VPC Endpoint** 선택 문제다.

## Core Concepts

- 네트워크 경계는 2겹으로 생각한다
  - Instance/ENI 단위: Security Group(상태 저장)
  - Subnet 단위: NACL(무상태, 양방향 규칙 필요)
- “사설 경로”는 시험에서 자주 정답으로 이어진다
  - 인터넷 경유를 피하고(보안), NAT 비용/운영을 줄인다(비용)

![VPC endpoints: gateway vs interface](../../assets/core/vpc-endpoints-types.svg)

## Deep Dive

### Security Group vs NACL (시험형 비교)

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

### VPC Endpoints: NAT 없이 “사설로 AWS 서비스 접근”

- Gateway endpoint
  - S3, DynamoDB
  - 라우팅 테이블에 경로가 추가되는 형태(개념)
  - 비용/운영 측면에서 “NAT 비용 절감” 선택지로 빈출
- Interface endpoint(PrivateLink)
  - ENI 형태로 VPC 안에 엔드포인트가 생긴다(개념)
  - 다양한 AWS 서비스/사설 연결에 사용
- Endpoint policy(개념)
  - 엔드포인트를 통해 허용되는 요청을 추가로 제한
- Exam must-know (포인트 + Why + 대안)
  - Key point: S3/DynamoDB 는 gateway endpoint, 대부분의 다른 서비스는 interface endpoint(PrivateLink)다.
  - Why: gateway는 라우팅 테이블 경로로 “목적지”를 바꾸는 모델이고(S3/DDB 전용), interface는 VPC 안 ENI로 사설 엔드포인트를 제공하는 모델(서비스 범용)이다.
  - Alternative: endpoint가 지원되지 않거나 요구가 “인터넷 아웃바운드 일반”이면 NAT가 후보가 되지만, “사설 경로/비용 절감”이면 endpoint가 우선이다.

```mermaid
flowchart LR
  App[Private subnet workload] --> RT[Route table]
  RT --> EP[S3 Gateway Endpoint]
  EP --> S3[S3]
  App -. alternative .-> NAT[NAT GW] -.-> IGW[Internet] -.-> S3
```

## Exam Traps

- “S3는 보안 그룹으로 막는다”는 오답 유도: S3는 SG 대상이 아니다(대신 bucket policy/VPC endpoint policy).
- “NACL은 상태 저장”이라는 착각: NACL은 무상태라 리턴 트래픽 포트까지 고려해야 한다.
- NAT를 무조건 정답으로 고르는 실수: 요구사항이 “사설 경로/비용”이면 endpoint가 정답 후보가 된다.

## TL;DR (한 줄 정리)

- **SG(인스턴스) + NACL(서브넷)로 경계를 세우고**, “인터넷 없이/비용 줄여”가 보이면 **VPC Endpoints(필요 시 PrivateLink)**로 사설 경로를 만든다.
