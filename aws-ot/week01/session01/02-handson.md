# Demo or Workshop (Console-First): AWS Console Tour

## Goal

- AWS 콘솔에서 리전, 서비스 검색, 리소스 탐색의 기본 동선을 익힌다.
- (권한이 있으면) IAM Best practice와 Billing 대시보드를 "어디서 보는지"만 확인한다.

## Steps

### A) Console Steps

1. 콘솔 상단에서 Region 변경을 해보고 "리전별 리소스" 개념을 확인한다.
2. 서비스 검색에서 `S3`, `EC2`, `VPC`, `CloudWatch`를 찾아 들어가 본다.
3. Billing 또는 Cost Management 메뉴 위치를 확인한다(권한이 없으면 못 보일 수 있음).
4. IAM에서 MFA, 사용자, 역할 메뉴를 확인한다(생성은 옵션).

### B) Optional

- "계정 보안 체크리스트"를 팀 표준으로 만들기
  - 루트 계정 MFA
  - admin 권한 최소화
  - CloudTrail 기본 활성화 여부

## Cleanup

- 리소스를 생성하지 않는 데모라면 별도 정리 없음

