# Day 04 - Data transfer + NAT vs endpoints + CloudFront caching (네트워크/엣지 비용 최적화)

![고객 사례 삽화 - NAT/엔드포인트/CloudFront 비용 레버](../../assets/scenario_image/w4d4s0.png)

## Outcomes

- 데이터 전송 비용(특히 인터넷 egress/NAT)이 왜 함정인지 설명한다.
- 프라이빗 서브넷에서 S3 접근 시 NAT 대신 S3 Gateway endpoint가 비용 최적화 후보인 이유를 설명한다.
- CloudFront 캐시가 전송/오리진 비용에 미치는 영향을 “요청 수/전송량” 관점으로 설명한다.

## Services In Scope

- VPC: NAT Gateway (개념), VPC Endpoints(S3 gateway)
- CloudFront (캐시로 오리진 트래픽 감소)

## Timebox (4h)

- Theory + mini-action: 4h

## Reading (서비스별 theory)

- [VPC Endpoints vs NAT: 사설 경로로 비용 함정 회피](01-vpc-endpoints.md)
- [CloudFront: 캐시로 전송/오리진 비용을 줄인다](02-cloudfront-cost.md)

## Core Concepts

- 네트워크 비용은 “숨은 드라이버”가 많다
  - NAT 경유, 인터넷 egress, 교차 AZ/리전 전송
- 시험형 최적화 방향
  - S3/DynamoDB 접근이면 endpoint로 NAT를 피한다
  - 다운로드/정적 콘텐츠면 CloudFront로 전송량/오리진 부하를 줄인다

![네트워크 비용 레버](../../assets/core/network-cost-nat-endpoint-cloudfront.svg)

## Exam Traps (확장)

- NAT를 무조건 정답으로 고르는 선택지(요구가 S3 접근/비용이면 endpoint 후보)
- 캐시 불가능(개인화/항상 최신)인데 CloudFront를 고르는 선택지
- 더 많은 연계/고급 함정: `../../exam-trap-bank.md`

## TL;DR (한 줄 정리)

- “프라이빗 서브넷 → S3 + 비용”이면 **S3 Gateway Endpoint**, “글로벌 다운로드/정적”이면 **CloudFront 캐시**가 대표 후보다.

## Exam-Style Design Questions

- “프라이빗 서브넷 -> S3” 요구에서 NAT 비용을 줄이려면?
- CloudFront가 비용 최적화 정답이 되는 신호는?
- 교차 AZ/리전 트래픽이 비용 드라이버가 되는 신호는?
