# Hands-on Lab: IAM Role Switching + Least Privilege (STS)

## TL;DR (무엇이 보이면 성공인가)

- `allowed/`는 읽히고 `denied/`는 막히면 성공이다. 그리고 “누가 호출했는지(Caller identity)”가 **AssumeRole 한 role ARN**으로 바뀌어야 한다.

## Goal

- S3의 “특정 prefix만 읽기” 권한을 IAM 정책으로 구현한다.
- STS AssumeRole로 임시 자격 증명을 발급받아 권한이 실제로 제한되는지 검증한다.
- Session policy로 AssumeRole 이후 권한을 추가로 제한하는 패턴을 확인한다.

## Success Signals (먼저 확인할 것)

- Console role switching 후 `allowed/allowed.txt` 다운로드는 성공한다.
- `denied/denied.txt`는 `AccessDenied`가 뜬다(“막히는 게 정상”).
- (CLI 사용 시) `aws sts get-caller-identity`의 ARN이 AssumeRole 세션으로 보인다.

## Prereqs

- IAM role/policy를 생성할 권한(관리자 권한 권장)
- AWS 콘솔 접근
- (Optional) CloudShell/AWS CLI (검증용)
- Region: 아무거나(S3는 글로벌 네임스페이스, IAM은 글로벌)

## Cost Notes

- S3 소량 사용(거의 무료 수준). 반드시 Cleanup 수행.

## Steps

### A) Console Steps

#### 1) 테스트용 S3 버킷/오브젝트 생성

1. S3 콘솔에서 버킷 생성
  - 버킷 이름은 글로벌 유일해야 한다. 예: `saa-day1-<랜덤>`
  - Block Public Access는 기본값 유지(권장)
2. 폴더(prefix) 2개 생성: `allowed/`, `denied/`
3. 오브젝트 업로드
  - `allowed/allowed.txt` (내용: `hello`)
  - `denied/denied.txt` (내용: `secret`)

#### 2) IAM 정책 생성 (allowed/* 만 GetObject 허용)

정책 이름 예시: `SAA-Day1-S3PrefixReadOnly`

정책 JSON(버킷 이름은 본인 값으로 교체):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListBucket",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::BUCKET_NAME"],
      "Condition": { "StringLike": { "s3:prefix": ["allowed/*"] } }
    },
    {
      "Sid": "GetAllowedPrefix",
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::BUCKET_NAME/allowed/*"]
    }
  ]
}
```

1. IAM 콘솔에서 Policy 생성(위 JSON 붙여넣기)
2. 생성된 정책 ARN/이름을 기록

#### 3) IAM Role 생성 + Trust policy 설정

- Role 이름 예시: `SAA-Day1-RoleSwitch`
- Trusted entity: “AWS account” 선택 후 현재 계정 지정(학습용)
- Permission: 2)에서 만든 정책을 연결

같은 계정의 사용자에 열어두는 단순 예시(학습용):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::ACCOUNT_ID:root" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### 4) Console Role Switching 으로 역할 전환 후 S3 접근 테스트

1. 콘솔 우측 상단 계정 메뉴에서 “Switch role(역할 전환)” 선택
2. Account ID: 현재 계정, Role name: `SAA-Day1-RoleSwitch`
3. 전환 후 S3 콘솔에서:
  - `allowed/` 오브젝트 다운로드 시도: 성공해야 함
  - `denied/` 오브젝트 다운로드 시도: Access Denied가 나야 함

### B) Optional: CLI Equivalents (for validation/automation)

#### 1) STS AssumeRole로 임시 크레덴셜 발급

CloudShell(bash) 예시(ACCOUNT_ID/ROLE_ARN/BUCKET 교체):

```bash
ROLE_ARN="arn:aws:iam::ACCOUNT_ID:role/SAA-Day1-RoleSwitch"
CREDS=$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name saa-day1)
export AWS_ACCESS_KEY_ID=$(echo "$CREDS" | jq -r .Credentials.AccessKeyId)
export AWS_SECRET_ACCESS_KEY=$(echo "$CREDS" | jq -r .Credentials.SecretAccessKey)
export AWS_SESSION_TOKEN=$(echo "$CREDS" | jq -r .Credentials.SessionToken)
aws sts get-caller-identity
```

#### 2) 권한 검증 (allowed/* 는 성공, denied/* 는 실패)

```bash
aws s3 ls "s3://$BUCKET/allowed/"
aws s3 cp "s3://$BUCKET/allowed/allowed.txt" -
aws s3 cp "s3://$BUCKET/denied/denied.txt" - || true
```

#### 3) (옵션) Session policy로 추가 제한 확인

AssumeRole 시점에 session policy를 넣어 “GetObject 자체를 막는” 제한을 추가할 수 있다.

```bash
DENY_GET='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":["s3:GetObject"],"Resource":"*"}]}'
CREDS2=$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name saa-day1-deny --policy "$DENY_GET")
export AWS_ACCESS_KEY_ID=$(echo "$CREDS2" | jq -r .Credentials.AccessKeyId)
export AWS_SECRET_ACCESS_KEY=$(echo "$CREDS2" | jq -r .Credentials.SecretAccessKey)
export AWS_SESSION_TOKEN=$(echo "$CREDS2" | jq -r .Credentials.SessionToken)
aws s3 cp "s3://$BUCKET/allowed/allowed.txt" - || true
```

## Validation Checklist

- `aws sts get-caller-identity` 결과가 AssumeRole 한 ARN으로 바뀐다.
- `allowed/*` 경로의 `GetObject`는 성공한다.
- `denied/*` 경로의 `GetObject`는 `AccessDenied`가 난다.
- (옵션) session policy를 넣으면 `allowed/*`도 막힌다.

## Common Errors

- S3 버킷 이름 중복: 버킷은 글로벌 유일해야 한다.
- AssumeRole 실패: trust policy의 Principal/Action을 확인한다.
- `jq` 없음: CloudShell에는 보통 있지만, 없으면 콘솔/다른 파싱 방법을 사용한다.
- “List는 되는데 GetObject는 안 됨”: `s3:ListBucket`와 `s3:GetObject`는 리소스 ARN이 다르다(버킷 vs 오브젝트).

## Cleanup

1. S3 버킷 오브젝트 삭제 후 버킷 삭제
2. IAM Role 삭제
3. IAM 정책 삭제
