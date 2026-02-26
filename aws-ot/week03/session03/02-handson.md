# Demo or Workshop (Console-First): IAM and secrets posture review

## Goal

- IAM과 Secrets Manager 콘솔에서 "정책과 시크릿의 위치"를 확인한다.
- 팀의 기본 보안 체크리스트 초안을 만든다.

## Steps

### A) Console Steps

1. IAM에서 Users, Roles, Policies 메뉴를 확인한다.
2. Secrets Manager에서 Create secret 화면을 열고, KMS 키 선택 위치를 확인한다(생성은 옵션).
3. CloudTrail Event history 화면에서 최근 이벤트를 확인한다.

### B) Workshop

- 체크리스트 초안
  - 루트 MFA
  - 역할 기반 권한 위임
  - 시크릿 서비스 사용
  - CloudTrail 로그 전략

## Cleanup

- 리소스를 생성하지 않으면 정리 없음

