# Day 02 - KMS + Secrets patterns

## Outcomes

- KMS key policy와 IAM policy의 역할을 구분한다(특히 “KMS는 key policy가 핵심”).
- Secrets Manager vs SSM Parameter Store(특히 SecureString) 선택 기준을 설명한다.
- S3 SSE-KMS에서 “S3 권한만 줬는데도 AccessDenied”가 나는 이유를 설명한다.
- 데이터 보호 통제를 “암호화 + 접근 제어 + 감사”로 묶어서 설계한다.

## Services In Scope

- KMS (CMK, key policy, grants 개념)
- Secrets Manager
- SSM Parameter Store (SecureString) 비교
- S3 SSE-KMS (암호화 통합 관점)

## Timebox (4h)

- Theory: 2h
- Hands-on (console): 2h

## Exam-Style Design Questions

- KMS에서 “key policy vs IAM policy” 중 무엇이 실제로 막고 있는지 어떻게 판단할까?
- 애플리케이션 시크릿은 Secrets Manager가 정답인 경우가 많다. 그 이유(기능/운영/보안)는?
- S3 객체를 SSE-KMS로 암호화했을 때, 어떤 권한들이 함께 필요해지는가?

