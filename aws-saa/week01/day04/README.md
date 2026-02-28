# Day 04 - VPC security (네트워크 경계: SG/NACL/Endpoints)

![고객 사례 삽화 - SG vs NACL](../../assets/scenario_image/w1d4s1.png)

## Outcomes

- Security Group과 NACL의 차이를 “상태 저장/서브넷 범위/규칙 평가”로 구분한다.
- VPC Endpoint가 필요한 이유를 “사설 경로 + 비용/보안” 관점으로 설명한다.
- S3 Gateway endpoint와 Interface endpoint(개념)의 차이를 설명한다.
- S3 Gateway endpoint의 동작을 예시로 이해하고 “NAT 없이도 S3로 사설 접근”하는 설계를 말로 풀 수 있다.

## Services In Scope

- VPC security: Security Groups, NACLs
- VPC Endpoints (Gateway: S3/DynamoDB, Interface: PrivateLink)
- (개념) Endpoint policy

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [Security Group vs NACL (네트워크 문지기 2종)](01-sg-vs-nacl.md)
- [VPC Endpoints/PrivateLink (사설 경로 + NAT 비용/보안)](02-vpc-endpoints-privatelink.md)

> 네트워크 경계는 “문지기(SG/NACL)”와 “길(Endpoints)”을 분리해서 읽는 게 제일 덜 헷갈린다.

## Core Concepts

- 네트워크 경계는 2겹으로 생각한다
  - Instance/ENI 단위: Security Group(상태 저장)
  - Subnet 단위: NACL(무상태, 양방향 규칙 필요)
- “사설 경로”는 시험에서 자주 정답으로 이어진다
  - 인터넷 경유를 피하고(보안), NAT 비용/운영을 줄인다(비용)

![VPC endpoints: gateway vs interface](../../assets/core/vpc-endpoints-types.svg)

## Exam Traps (확장)

- “S3는 보안 그룹으로 막는다”는 오답 유도: S3는 SG 대상이 아니다(대신 bucket policy/VPC endpoint policy).
- “NACL은 상태 저장”이라는 착각: NACL은 무상태라 리턴 트래픽 포트까지 고려해야 한다.
- NAT를 무조건 정답으로 고르는 실수: 요구사항이 “사설 경로/비용”이면 endpoint가 정답 후보가 된다.
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- “프라이빗 서브넷에서 S3 접근”을 인터넷 없이(또는 NAT 비용 최소로) 설계하려면?
- SG로 막을 수 없는 요구사항(예: S3 접근 제어)은 어떤 도구로 해결해야 하나?
- Gateway endpoint와 Interface endpoint는 무엇이 다르고, 어떤 신호로 선택해야 하나?

## TL;DR (한 줄 정리)

- **SG(인스턴스) + NACL(서브넷)로 경계를 세우고**, “인터넷 없이/비용 줄여”가 보이면 **VPC Endpoints(필요 시 PrivateLink)**로 사설 경로를 만든다.
