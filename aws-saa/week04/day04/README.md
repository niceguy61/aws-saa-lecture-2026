# Day 04 - Data transfer + NAT vs endpoints + CloudFront caching

## Outcomes

- 데이터 전송 비용(특히 인터넷 egress/NAT)이 왜 함정인지 설명한다.
- 프라이빗 서브넷에서 S3 접근 시 NAT 대신 S3 Gateway endpoint가 비용 최적화 후보인 이유를 설명한다.
- CloudFront 캐시가 전송/오리진 비용에 미치는 영향을 “요청 수/전송량” 관점으로 설명한다.

## Services In Scope

- VPC: NAT Gateway (개념), VPC Endpoints(S3 gateway)
- CloudFront (캐시로 오리진 트래픽 감소)

## Timebox (4h)

- Theory + mini-action: 4h

## Exam-Style Design Questions

- “프라이빗 서브넷 -> S3” 요구에서 NAT 비용을 줄이려면?
- CloudFront가 비용 최적화 정답이 되는 신호는?
- 교차 AZ/리전 트래픽이 비용 드라이버가 되는 신호는?
