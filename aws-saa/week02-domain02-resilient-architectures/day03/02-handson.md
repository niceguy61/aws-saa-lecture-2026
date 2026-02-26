# Hands-on Lab (Console): S3 Versioning + Same-Region Replication 설정

## Goal

- S3 versioning으로 덮어쓰기/삭제 복구 흐름을 확인한다.
- (선택) SRR(동일 리전 복제) 규칙을 만들고 대상 버킷에 객체가 복제되는지 확인한다.

## Prereqs

- S3 버킷 생성/설정 권한
- Region: 수업 기본 리전

## Cost Notes

- S3 저장/요청 비용이 발생할 수 있다(소량 테스트 후 Cleanup).

## Steps

### A) Console Steps

#### 1) 소스/대상 버킷 2개 생성

1. 버킷 A(소스): `saa-week2-s3-src-<랜덤>`
2. 버킷 B(대상): `saa-week2-s3-dst-<랜덤>`
3. 둘 다 Block Public Access 유지

#### 2) Versioning 활성화(둘 다)

1. 버킷 A -> Properties -> Bucket Versioning -> Enable
2. 버킷 B도 동일

#### 3) Versioning 복구 흐름 확인(버킷 A)

1. `demo.txt` 업로드(내용: v1)
2. 같은 이름으로 다시 업로드(내용: v2)
3. `demo.txt` 삭제
4. Versions 탭에서 delete marker/이전 버전 확인
5. 이전 버전을 복원(필요 시 delete marker 삭제)

#### 4) (옵션) Replication rule 생성(SRR)

1. 버킷 A -> Management -> Replication rules -> Create rule
2. Rule scope: 전체 또는 prefix 지정(학습용은 전체)
3. Destination: 버킷 B 선택
4. IAM role은 자동 생성(학습용)
5. 저장

#### 5) (옵션) 복제 확인

1. 버킷 A에 `replicate.txt` 업로드
2. 잠시 후 버킷 B에 동일 객체가 생성되는지 확인

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위.

## Validation Checklist

- versioning에서 “이전 버전/삭제 마커”를 확인하고 복구할 수 있다.
- (옵션) SRR 설정 후 대상 버킷으로 복제가 일어난다.

## Common Errors

- versioning을 대상 버킷에 안 켬: 복제 구성이 막히거나 동작하지 않는다.
- 복제는 즉시가 아닐 수 있다(지연 가능).

## Cleanup

1. (옵션) Replication rule 삭제
2. 두 버킷의 모든 오브젝트/버전 삭제
3. 두 버킷 삭제

