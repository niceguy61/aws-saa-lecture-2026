# Hands-on Lab (Console): S3 Gateway Endpoint 만들기(사설 경로 설계)

## Goal

- 기존 VPC에서 S3 Gateway endpoint를 생성하고, 라우팅 테이블에 연결한다.
- “프라이빗 서브넷 -> S3”를 NAT 없이 설계할 수 있음을 설명한다.

## Prereqs

- VPC/Endpoint/Route table 조회/수정 권한
- Region: 수업 기본 리전

## Cost Notes

- S3 Gateway endpoint는 일반적으로 NAT 대비 비용 최적화 힌트로 출제된다(세부 요금은 계정/정책에 따라 다를 수 있으니 최신 문서를 확인).

## Steps

### A) Console Steps

#### 1) VPC와 Route table 파악

1. VPC 콘솔 -> Your VPCs에서 대상 VPC 선택(수업 VPC 또는 default VPC)
2. Route tables에서 해당 VPC의 route table 목록 확인
3. “프라이빗 서브넷이 연결된 route table”을 하나 선택(태그/연결 서브넷으로 판별)

#### 2) S3 Gateway endpoint 생성

1. VPC 콘솔 -> Endpoints -> Create endpoint
2. Service category: AWS services
3. Service name: `com.amazonaws.<region>.s3` 선택
4. VPC: 1)에서 선택한 VPC
5. Route tables: 1)에서 고른 프라이빗 route table 선택
6. (옵션) Endpoint policy는 기본값으로 시작(학습용)
7. Create endpoint

#### 3) Route table에서 endpoint 경로 확인

1. 1)에서 선택한 route table을 열고 Routes 탭 확인
2. S3 prefix list 대상으로 endpoint가 추가되어 있는지 확인

#### 4) (설명 체크) “왜 NAT 없이도 되나”

- S3 트래픽이 인터넷 경유가 아니라 VPC 내 사설 경로로 라우팅된다는 점을 말로 정리한다.
- 시험에서는 이 구성이 “비용(특히 NAT) + 보안” 관점의 정답 후보가 된다.

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위. 필요 시 `describe-vpc-endpoints`, `describe-route-tables`로 검증 가능.

## Validation Checklist

- S3 Gateway endpoint가 생성되어 있고 route table에 연결돼 있다.
- route table에 endpoint 경로가 추가된 것을 확인했다.
- “사설 경로 + NAT 비용 절감” 관점으로 설명할 수 있다.

## Common Errors

- 잘못된 route table에 연결: 프라이빗 서브넷이 실제로 사용하는 route table을 확인한다.
- Interface endpoint와 혼동: S3는 Gateway endpoint가 대표 선택지다.

## Cleanup

1. VPC endpoint 삭제

