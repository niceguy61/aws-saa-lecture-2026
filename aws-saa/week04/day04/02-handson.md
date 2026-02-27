# Hands-on Lab (Console): S3 Gateway Endpoint로 NAT 비용 함정 회피(설정 확인)

## Goal

- VPC에서 S3 Gateway endpoint를 만들고 route table에 연결한다.
- “프라이빗 서브넷 -> S3”를 NAT 없이 설계할 수 있음을 비용 관점으로 설명한다.

## Prereqs

- VPC/Endpoint/Route table 조회/수정 권한
- Region: 수업 기본 리전

## Cost Notes

- 이 실습은 주로 “설정 확인” 중심이며, 실제 NAT를 만들지 않아도 비용 최적화 논리를 설명할 수 있다.

## Steps

### A) Console Steps

#### 1) 대상 VPC/Route table 확인

1. VPC -> Your VPCs에서 VPC 선택
2. Route tables에서 프라이빗 서브넷이 연결된 route table 선택

#### 2) S3 Gateway endpoint 생성

1. VPC -> Endpoints -> Create endpoint
2. Service: `com.amazonaws.<region>.s3`
3. VPC: 1)의 VPC
4. Route tables: 1)의 route table 선택
5. Create

#### 3) route table 경로 확인

1. route table -> Routes 탭
2. S3 prefix list가 endpoint 대상으로 연결된 것을 확인

#### 4) (설명 체크) 시험형 답안 문장 만들기

- “NAT 경유 대신 endpoint로 사설 연결해 NAT 비용/보안 위험을 줄인다.”

### B) Optional: CloudFront 비용 최적화 연결(설명)

- “정적 콘텐츠/다운로드”라면 CloudFront 캐시로 오리진 전송량/요청 수를 줄일 수 있다.

## Validation Checklist

- S3 gateway endpoint가 생성되어 route table에 연결돼 있다.
- NAT 비용 함정 회피 논리를 말로 설명할 수 있다.

## Cleanup

1. VPC endpoint 삭제

