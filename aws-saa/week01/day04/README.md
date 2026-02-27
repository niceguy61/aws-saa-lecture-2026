# Day 04 - VPC security (SG/NACL) + Private connectivity (Endpoints/PrivateLink)

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

## Exam-Style Design Questions

- “프라이빗 서브넷에서 S3 접근”을 인터넷 없이(또는 NAT 비용 최소로) 설계하려면?
- SG로 막을 수 없는 요구사항(예: S3 접근 제어)은 어떤 도구로 해결해야 하나?
- Gateway endpoint와 Interface endpoint는 무엇이 다르고, 어떤 신호로 선택해야 하나?
