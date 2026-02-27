# Integrated Mini Lab (Console): KMS + Secrets Manager + IAM Guardrails

## Goal

- KMS CMK로 보호되는 시크릿을 만들고, “읽을 수 있는 역할/못 읽는 역할”을 콘솔에서 명확히 확인한다.
- CloudTrail Event history로 `GetSecretValue` 호출 흔적을 확인한다.

## Prereqs

- IAM role/policy, KMS key, Secrets Manager secret 생성 권한
- Region: 아무거나(권장: 수업 기본 리전)

## Cost Notes

- Secrets Manager는 비용이 발생할 수 있다(실습 후 즉시 삭제 권장).

## Steps

### A) Console Steps

#### 1) KMS 키 생성

1. KMS 콘솔에서 “대칭 키” 생성
2. Alias 예: `alias/saa-week1-secret`
3. Key 관리자/사용자는 기본값(학습용)으로 시작하되, “키 사용 권한”이 보안의 핵심임을 확인

#### 2) Secrets Manager 시크릿 생성(사용자 정의 값)

1. Secrets Manager에서 “Other type of secret” 선택
2. Key/Value 예: `db_user=app`, `db_pass=ChangeMe123!`
3. 암호화 키: 1)에서 만든 KMS 키 선택
4. 이름 예: `saa/week1/demo-secret`

#### 3) “읽기 전용 역할” 생성

1. IAM 콘솔에서 Role 생성
  - Trusted entity: AWS account(현재 계정) 학습용
  - Role 이름: `SAA-Week1-SecretReader`
2. Role permission policy를 최소 권한으로 구성
  - Secrets Manager: `secretsmanager:GetSecretValue` 를 “해당 secret ARN”으로 제한
  - KMS: `kms:Decrypt` 를 “해당 key ARN”으로 제한

정책 예시(ARN은 교체):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadSpecificSecret",
      "Effect": "Allow",
      "Action": ["secretsmanager:GetSecretValue"],
      "Resource": ["SECRET_ARN"]
    },
    {
      "Sid": "DecryptWithSpecificKey",
      "Effect": "Allow",
      "Action": ["kms:Decrypt"],
      "Resource": ["KMS_KEY_ARN"]
    }
  ]
}
```

#### 4) 역할 전환(Role switching)으로 시크릿 읽기 테스트

1. 콘솔 우측 상단 계정 메뉴에서 “Switch role”
2. Role: `SAA-Week1-SecretReader`
3. Secrets Manager에서 시크릿을 열고 “Retrieve secret value” 수행

#### 5) (옵션) “권한 없는 역할”로 실패 확인

1. 별도 Role `SAA-Week1-NoSecretAccess` 생성(Secrets/KMS 권한 없이)
2. Switch role 후 시크릿 읽기 시도 -> AccessDenied 확인

#### 6) CloudTrail Event history로 감사 확인

1. CloudTrail 콘솔 -> Event history
2. Event name 필터: `GetSecretValue`
3. `SAA-Week1-SecretReader` 역할로 실행된 이벤트가 찍히는지 확인

### B) Optional: CLI Equivalents (for validation/automation)

- CLI로 `aws secretsmanager get-secret-value` 를 수행해도 된다(수업은 콘솔 기준).

## Validation Checklist

- SecretReader 역할로는 시크릿 값을 조회할 수 있다.
- 권한 없는 역할로는 AccessDenied가 난다.
- CloudTrail Event history에 조회 이벤트가 남는다.

## Common Errors

- KMS `kms:Decrypt` 권한 누락: Secrets 권한이 있어도 복호화가 안 된다.
- 리소스 범위를 `*`로 열어두는 실수: 시험에서는 “최소 권한”이 핵심이다.

## Cleanup

1. Secrets Manager 시크릿 삭제
2. IAM Role(SecretReader/NoSecretAccess) 삭제 및 정책 삭제
3. KMS 키 비활성화 후 스케줄 삭제(필요 시)

