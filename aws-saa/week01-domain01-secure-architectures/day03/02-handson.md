# Hands-on Lab (Console): CloudTrail Trail 생성 + 변경 이벤트 추적

## Goal

- Trail을 생성해 CloudTrail 로그가 S3로 저장되는 흐름을 만든다.
- 콘솔에서 보안 그룹 규칙을 변경하고, CloudTrail Event history/로그에서 “누가 무엇을 했는지”를 확인한다.

## Prereqs

- CloudTrail/S3/IAM 권한(학습용 관리자 권장)
- Region: 수업 기본 리전

## Cost Notes

- Trail 로그가 S3에 저장되며, 저장/조회에 따라 비용이 발생할 수 있다(소량 테스트 후 Cleanup).

## Steps

### A) Console Steps

#### 1) CloudTrail 로그 버킷 준비

1. S3 버킷 생성(글로벌 유일): `saa-day3-cloudtrail-<랜덤>`
2. Block Public Access 유지

#### 2) Trail 생성

1. CloudTrail 콘솔 -> Trails -> Create trail
2. Trail name: `saa-day3-trail`
3. Storage location: 1) 버킷 선택(또는 CloudTrail이 생성하도록)
4. (학습용) Management events는 기본값 유지
5. 생성

#### 3) 이벤트 생성(보안 그룹 규칙 변경)

1. EC2 콘솔 -> Security Groups
2. 기존 SG를 하나 선택(또는 새 SG 생성)
3. Inbound rules에 임시로 규칙 추가(예: 자기 IP에만 443 허용)
4. 저장

#### 4) CloudTrail에서 이벤트 확인

1. CloudTrail -> Event history
2. Event name 필터: `AuthorizeSecurityGroupIngress` 또는 `RevokeSecurityGroupIngress`
3. 이벤트 상세에서 `userIdentity`/`sourceIPAddress`/`requestParameters` 확인

#### 5) (옵션) S3에 로그 파일이 쌓이는지 확인

1. S3 버킷에서 `AWSLogs/` 프리픽스가 생성되는지 확인

### B) Optional: CLI Equivalents (for validation/automation)

- 콘솔이 1순위. 필요하면 CloudShell로 `aws cloudtrail lookup-events`를 사용할 수 있다.

## Validation Checklist

- Trail이 생성되어 S3로 저장 위치가 잡혀 있다.
- 보안 그룹 변경 이벤트가 Event history에 기록된다.
- 이벤트에서 “누가/언제/어디서(source IP)/무엇을(request)”를 설명할 수 있다.

## Common Errors

- 이벤트가 바로 안 보임: 약간의 지연이 있을 수 있다.
- 필터 키워드가 다름: UI에서 Event name 목록을 확인한다.

## Cleanup

1. 2)에서 만든 Trail 삭제
2. S3 버킷의 로그 오브젝트 삭제 후 버킷 삭제
3. 3)에서 추가한 SG 규칙 원복

