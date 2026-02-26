# Hands-on Lab (Console): S3 SSE-KMS 권한 함정 재현 + 해결

## Goal

- SSE-KMS로 암호화된 S3 객체에 대해 “S3 권한은 있는데 읽기 실패” 상황을 재현한다.
- `kms:Decrypt` 권한을 최소 범위로 추가해 문제를 해결한다.
- (옵션) Secrets Manager 시크릿을 생성하고 KMS 통합을 확인한다.

## Prereqs

- IAM role/policy, KMS key, S3 버킷 생성 권한
- Region: 수업 기본 리전

## Cost Notes

- S3/KMS 사용량이 소량이면 비용은 작지만, 리소스를 정리한다.
- (옵션) Secrets Manager는 비용이 발생할 수 있으니 생성 후 삭제한다.

## Steps

### A) Console Steps

#### 1) KMS 키 생성

1. KMS 콘솔에서 대칭 키 생성
2. Alias 예: `alias/saa-day2-s3`

#### 2) S3 버킷 생성 + SSE-KMS 업로드

1. S3 버킷 생성(글로벌 유일): `saa-day2-ssekms-<랜덤>`
2. 업로드 시 Server-side encryption 선택
  - SSE-KMS
  - KMS key: 1)에서 만든 CMK
3. 파일 업로드: `sample.txt`

#### 3) “S3만 허용” 역할 생성(의도적 실패)

1. IAM Role 생성(학습용: 같은 계정 Trust)
  - 이름: `SAA-Day2-S3Reader-WithoutKMS`
2. 아래 정책을 Role에 연결(버킷/오브젝트 ARN 교체)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListAndRead",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::BUCKET_NAME"]
    },
    {
      "Sid": "GetObject",
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::BUCKET_NAME/*"]
    }
  ]
}
```

#### 4) Role Switching 후 다운로드 시도(실패 확인)

1. 콘솔에서 Switch role -> `SAA-Day2-S3Reader-WithoutKMS`
2. S3에서 `sample.txt` 다운로드/열기 시도
3. AccessDenied(또는 KMS 관련 오류) 확인

#### 5) KMS Decrypt 권한 최소 추가(해결)

1. `SAA-Day2-S3Reader-WithoutKMS`에 아래 권한 추가(키 ARN 교체)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DecryptOnlyThisKey",
      "Effect": "Allow",
      "Action": ["kms:Decrypt"],
      "Resource": ["KMS_KEY_ARN"]
    }
  ]
}
```

2. 다시 다운로드 시도 -> 성공 확인

#### 6) (옵션) Secrets Manager로 시크릿 생성(암호화 키 선택)

1. Secrets Manager -> new secret
2. KMS 키 선택: 1)의 키
3. secret value 확인 후 바로 삭제 준비

### B) Optional: CLI Equivalents (for validation/automation)

- 콘솔이 1순위. 검증용으로 `aws s3 cp`를 사용할 수 있다.

## Validation Checklist

- S3 권한만으로는 SSE-KMS 객체 접근이 실패할 수 있음을 확인했다.
- `kms:Decrypt`를 최소 범위로 추가하면 성공한다.
- (옵션) 시크릿 생성 시 KMS 키를 선택/변경할 수 있음을 확인했다.

## Common Errors

- KMS 키 정책이 너무 제한적: IAM Allow를 줘도 key policy에서 막힐 수 있다.
- `kms:*`로 과도하게 열어버림: 시험/실무 모두 최소 권한이 핵심이다.

## Cleanup

1. (옵션) Secrets Manager 시크릿 삭제
2. IAM Role/Policy 삭제
3. S3 오브젝트 삭제 후 버킷 삭제
4. KMS 키 비활성화 후 스케줄 삭제(필요 시)

