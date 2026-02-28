# Special Lecture - Domain 4: Cost-Optimized Architectures (Top Services)

## Why This Matters On The Exam

- 비용 최적화는 “요구사항 충족 + 비용 드라이버 제거”의 설계 문제로 나온다.
- 헷갈리는 포인트는 “SP/RI/Spot 선택”, “S3 storage class”, “NAT 비용 vs VPC endpoint”다.

## Services In Scope (Draft Top 10~15)

- EC2 pricing (Savings Plans, RIs, Spot)
- S3 storage classes + lifecycle
- Budgets/Cost Explorer(개념)
- NAT Gateway vs VPC endpoints
- DynamoDB capacity modes

## Confusing Similar Cases (Choose-This-Not-That)

| Scenario | Best choice | Why | Common wrong choice | Why it's wrong |
|---|---|---|---|---|
| S3 비용 최적화 | lifecycle + storage class | 자동 전환 | 무조건 Standard | 장기 보관에 비효율 |
| 프라이빗 S3 접근 비용 | Gateway endpoint(S3) | NAT egress 제거 | NAT Gateway | 시간/트래픽에 따라 급증 |

## Deep Dive (Stubs)

- TODO

## References

- Internal references:
  - [References index](../references/README.md)
  - [Exam guide (SAA-C03)](../references/exam-guide.md)
  - [Glossary](../references/glossary.md)
  - [AWS services list](../references/aws-services.md)
  - [Exam keypoints](../exam-keypoints.md)
  - [Exam trap bank](../exam-trap-bank.md)

- Official AWS documentation:
  - [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
  - [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  - [Search: VPC endpoints](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=VPC%20endpoints)
  - [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
  - [Search: S3 lifecycle rules](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=S3%20lifecycle%20rules)
  - [Search: S3 storage classes](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=S3%20storage%20classes)
  - [Search: S3 SSE-KMS](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=S3%20SSE-KMS)
  - [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
  - [Search: EC2 purchase options (RI/Savings Plans/Spot)](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=EC2%20purchase%20options%20Reserved%20Instances%20Savings%20Plans%20Spot)
  - [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
  - [Search: AWS Cost Explorer](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Cost%20Explorer)
  - [Search: AWS Budgets](https://docs.aws.amazon.com/search/doc-search.html?searchQuery=AWS%20Budgets)
