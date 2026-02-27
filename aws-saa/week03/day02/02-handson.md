# Hands-on Lab (Console): CloudFront 캐시 정책 튜닝(쿼리 스트링/TTL)

## Goal

- CloudFront + S3 오리진으로 간단한 캐시 구조를 만든다.
- 캐시 키에 쿼리 스트링을 포함/미포함 했을 때의 의미를 이해한다.
- invalidation으로 객체 갱신 흐름을 확인한다.

## Prereqs

- S3/CloudFront 생성 권한
- Region: S3는 수업 기본 리전(CloudFront는 글로벌)

## Cost Notes

- CloudFront/S3는 트래픽이 발생하면 비용이 생길 수 있다. 테스트는 소량으로 진행하고 Cleanup한다.

## Steps

### A) Console Steps

#### 1) S3 버킷 생성 + 파일 업로드

1. S3 버킷 생성(글로벌 유일): `saa-week3-cf-<랜덤>`
2. Block Public Access 유지
3. 파일 업로드: `index.html` (내용에 `version=v1` 포함)

#### 2) CloudFront distribution 생성(OAC)

1. CloudFront -> Create distribution
2. Origin: S3 버킷 선택
3. Origin access: OAC 생성/선택
4. Default behavior: Viewer protocol policy `Redirect HTTP to HTTPS`
5. 생성 후 CloudFront가 제시하는 bucket policy를 S3에 적용

#### 3) Cache behavior에서 쿼리 스트링 포함 설정 확인

1. Distribution -> Behaviors -> Default behavior 편집
2. Cache key and origin requests에서 “쿼리 스트링을 캐시 키에 포함할지” 설정 확인
3. 학습용:
  - 1차: 쿼리 스트링 미포함(기본)
  - 2차: 쿼리 스트링 포함으로 변경(비교)

#### 4) 테스트(브라우저) + invalidation

1. Distribution domain으로 접속: `https://<domain>/index.html?x=1`
2. S3에서 index.html을 `version=v2`로 바꾸고 업로드
3. 바로 접속하면 캐시로 v1이 보일 수 있음
4. CloudFront -> Invalidations -> Create: `/index.html`
5. 완료 후 다시 접속해 v2 확인

### B) Optional: CLI Equivalents (for validation/automation)

- 헤더의 `x-cache`를 확인하면 hit/miss를 관찰할 수 있다(선택).

## Validation Checklist

- OAC 기반으로 CloudFront만 S3에 접근하는 구조를 만들 수 있다.
- 쿼리 스트링을 캐시 키에 포함하면 캐시 변종이 늘어날 수 있음을 설명한다.
- invalidation으로 갱신 흐름을 설명할 수 있다.

## Common Errors

- bucket policy 미적용: CloudFront에서 403이 난다.
- 배포 상태가 Deploying: 완료까지 시간이 걸릴 수 있다.

## Cleanup

1. CloudFront distribution Disable 후 삭제(전파 시간 필요)
2. S3 버킷 오브젝트 삭제 후 버킷 삭제

