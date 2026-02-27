# Integrated Mini Lab (Console): CloudFront + Private S3 (OAC) Caching

## Goal

- S3 버킷을 퍼블릭으로 열지 않고(Private), CloudFront(OAC)로만 접근하게 만든다.
- 캐시 동작(객체 변경 후 캐시 유지, invalidation)을 확인한다.

## Prereqs

- S3/CloudFront 생성 권한
- Region: S3 버킷은 수업 기본 리전(CloudFront는 글로벌)

## Cost Notes

- CloudFront/S3는 트래픽이 발생하면 비용이 생길 수 있다. 테스트는 소량으로 진행하고 정리한다.

## Steps

### A) Console Steps

#### 1) S3 버킷 생성 + 테스트 파일 업로드

1. S3 버킷 생성(예: `saa-week3-cf-oac-<랜덤>`)
2. Block Public Access 유지(퍼블릭 금지)
3. 파일 업로드: `index.html` (내용에 버전 문자열 포함: `v1`)

#### 2) CloudFront Distribution 생성(OAC 사용)

1. CloudFront에서 distribution 생성
2. Origin: S3 버킷 선택
3. Origin access: “Origin access control (OAC)” 생성/선택
4. Default behavior: GET/HEAD 허용, Viewer protocol policy는 Redirect to HTTPS 권장
5. 생성 후 CloudFront가 제시하는 “S3 bucket policy”를 복사

#### 3) S3 bucket policy에 OAC 정책 적용

1. S3 버킷 -> Permissions -> Bucket policy
2. 2)에서 복사한 정책을 붙여넣고 저장

#### 4) 배포 완료 후 접근 확인

1. Distribution domain name(예: `dxxxx.cloudfront.net`) 확인
2. `https://<domain>/index.html` 접근
3. S3 직접 URL 접근은 거부되고, CloudFront로만 접근되는지 확인

#### 5) 캐시 확인(객체 변경 + invalidation)

1. S3에서 `index.html` 내용을 `v2`로 변경 업로드
2. 즉시 CloudFront로 접근하면 여전히 `v1`이 보일 수 있다(캐시)
3. CloudFront -> Invalidation 생성: `/index.html`
4. 완료 후 다시 접근하면 `v2`로 갱신되는지 확인

### B) Optional: CLI Equivalents (for validation/automation)

- invalidation은 `aws cloudfront create-invalidation`으로도 가능(수업은 콘솔 기준).

## Validation Checklist

- S3 버킷은 퍼블릭이 아니고, CloudFront로만 콘텐츠가 제공된다.
- invalidation 전후로 캐시 갱신 동작을 설명할 수 있다.

## Common Errors

- 버킷 정책 미적용: CloudFront가 `403`을 반환한다.
- 배포 상태(Deploying) 중 테스트: 완료까지 시간이 걸린다.

## Cleanup

1. CloudFront distribution 비활성화(Disable) 후 삭제(전파에 시간이 걸릴 수 있음)
2. S3 버킷 오브젝트 삭제 후 버킷 삭제

