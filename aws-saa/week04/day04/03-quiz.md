# Quiz (Mock Questions) - Day 04

## Q1

**Scenario:** 프라이빗 서브넷의 워크로드가 S3에 자주 접근한다. NAT 비용을 줄이려면?

A. NAT Gateway를 더 늘린다  
B. S3 Gateway Endpoint를 사용한다  
C. S3를 퍼블릭 오픈한다  
D. WAF를 추가한다  

**Answer:** B  
**Explanation:** S3 접근이 핵심이면 gateway endpoint가 비용/보안 관점의 정답 후보가 된다.  
**Tags:** `domain:4` `services:VPC,S3`

## Q2

**Scenario:** NAT Gateway 비용이 함정이 되는 문장 신호는?

A. “프라이빗 서브넷에서 외부/서비스로 대량 호출”  
B. “IAM role switching”  
C. “S3 versioning”  
D. “CloudTrail trail”  

**Answer:** A  
**Explanation:** 프라이빗->외부/서비스 트래픽이 많으면 NAT 비용이 급증할 수 있다.  
**Tags:** `domain:4` `services:VPC`

## Q3

**Scenario:** 전 세계 사용자에게 캐시 가능한 정적 콘텐츠를 제공한다. 비용 최적화 관점에서 후보가 되는 것은?

A. CloudFront  
B. KMS  
C. STS  
D. Inspector  

**Answer:** A  
**Explanation:** 엣지 캐시는 오리진 요청/전송량을 줄여 비용에도 영향을 줄 수 있다.  
**Tags:** `domain:4` `services:CloudFront`

## Q4

**Scenario:** “무조건 CloudFront”가 오답이 될 수 있는 신호는?

A. 콘텐츠가 개인화/강한 일관성 요구로 캐시 효과가 낮다  
B. 정적 파일 다운로드가 많다  
C. 글로벌 사용자다  
D. 오리진 부하가 높다  

**Answer:** A  
**Explanation:** 캐시 효과가 없으면 비용/복잡도만 늘 수 있다.  
**Tags:** `domain:4` `services:CloudFront`

