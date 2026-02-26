# Theory

## Core Concepts

![IAM evaluation overview](./assets/core.svg)

### IAM evaluation: 외우는 게 아니라 "규칙"으로 푼다

- 기본은 Deny
- Explicit deny는 항상 Deny
- Allow가 있어야 통과
- 그리고 상한선(SCP, permission boundary)이 있으면 그 안에서만 허용된다

왜 이게 중요한가:
- 문제에서 AccessDenied가 나오면, "정책 평가 규칙"을 따라 원인을 좁힐 수 있어야 한다.
- 외우기만 하면 정책이 겹치는 순간(리소스 정책/경계)부터 답이 흔들린다.

### Secrets and encryption: 데이터 보호는 3종 세트

- Encryption: KMS 등으로 데이터 보호
- Access control: 누가 읽는지(IAM)
- Audit: 누가 읽었는지(CloudTrail)

왜 3개가 같이 나오나:
- 암호화만 하면 "누가 복호화 가능한지"가 남는다.
- 권한만 주면 "누가 언제 읽었는지"가 남는다.
- 시험/실무는 이 3개를 묶어 설계를 요구한다.

### CloudTrail vs Config: 행위 vs 상태

- CloudTrail: "누가 무엇을 했나"(API activity)
- Config: "리소스가 어떤 상태인가"(configuration and compliance)

## Key Takeaways (Must know)

- AccessDenied는 정책 평가 규칙으로 좁힌다(deny, allow, boundary 순서).
- rotation 요구가 있으면 Secrets Manager가 정답 후보가 된다.
- CloudTrail과 Config는 목적이 다르다.

## Frequently Confused (and why)

- "SCP는 권한을 부여한다"
  - 왜 틀린가: SCP는 상한선이다. Allow를 만들어주는 게 아니라 막을 수 있다.
- "KMS는 IAM policy만 보면 된다"
  - 왜 위험한가: KMS는 key policy가 gate로 작동하는 케이스가 많다.
- "로그가 있으면 감사가 된다"
  - 왜 불충분한가: 어떤 로그(CloudTrail)인지, 보관/검색 전략이 무엇인지가 감사를 만든다.

