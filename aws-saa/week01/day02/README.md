# Day 02 - KMS + Secrets patterns (데이터 보호: KMS/Secrets/S3 SSE-KMS)

![고객 사례 삽화 - KMS 키 금고와 정책 게이트](../../assets/scenario_image/w1d2s1.png)

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

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [KMS (key policy가 관문인 암호화 통제)](01-kms.md)
- [Secrets Manager vs Parameter Store(SecureString)](02-secrets-vs-parameter-store.md)
- [S3 SSE-KMS (대행 호출로 인한 AccessDenied 함정)](03-s3-sse-kms.md)

## Core Concepts (암기 대신 구조로)

- 데이터 보호 통제 3종 세트(시험형 사고)
  - Encryption at rest: KMS/SSE-KMS/Secrets encryption
  - Access control: IAM/리소스 정책/경계
  - Audit: CloudTrail(누가 키/시크릿을 썼는지)
- KMS가 “정책”에 민감한 이유
  - 암호화/복호화는 KMS API 호출로 귀결되고, KMS는 key policy를 중심으로 통제한다.
  - 다른 서비스(S3, EBS, Secrets Manager)가 KMS를 “호출 대행”할 때도 권한 경계가 중요하다.

![KMS envelope encryption and integration intuition](../../assets/core/kms-envelope-encryption.svg)

## Quick Comparison Table

| Scenario | Best choice | Why | Common trap |
|---|---|---|---|
| 시크릿 rotation 요구 | Secrets Manager | 운영 기능/통합 | Parameter Store만으로 해결하려 함 |
| 단순 설정 값 | Parameter Store | 경량/단순 | 시크릿까지 한곳에 무작정 몰기 |
| S3 객체 보관 암호화 | SSE-KMS | 중앙 키 통제 | S3 권한만 주면 된다고 착각 |

## Exam Traps (확장)

- “KMS는 IAM만 보면 된다”는 오답 유도: key policy가 포인트다.
- “SSE-KMS는 S3만 권한 주면 된다”는 오답 유도: KMS decrypt 경로가 있다.
- “시크릿을 S3/코드/환경변수에 저장” 같은 답안이 보이면 거의 오답(요구사항 따라 예외는 있지만 SAA는 대부분 관리형 선택).
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## Exam-Style Design Questions

- KMS에서 “key policy vs IAM policy” 중 무엇이 실제로 막고 있는지 어떻게 판단할까?
- 애플리케이션 시크릿은 Secrets Manager가 정답인 경우가 많다. 그 이유(기능/운영/보안)는?
- S3 객체를 SSE-KMS로 암호화했을 때, 어떤 권한들이 함께 필요해지는가?
