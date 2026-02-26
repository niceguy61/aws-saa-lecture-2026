# Quiz - Session 02

## Q1

**Scenario:** 워크로드 권한을 설계할 때 "키 공유"를 피하는 기본 답안은?

A. IAM user 액세스 키를 환경변수로 저장  
B. IAM role로 권한을 위임한다  
C. 루트 계정으로만 운영한다  
D. S3를 퍼블릭으로 연다  

**Answer:** B  
**Explanation:** role 기반 위임이 기본 패턴이다.  

## Q2

**Scenario:** S3 접근 제어에서 보안 그룹으로 해결하려는 제안에 대한 반응은?

A. 맞다. S3는 인스턴스다  
B. 틀리다. S3는 정책 기반으로 접근을 제어한다  
C. 맞다. NACL만 있으면 된다  
D. 틀리다. Route 53로 해결한다  

**Answer:** B  
**Explanation:** S3는 SG 대상이 아니며 정책으로 제어한다.  

