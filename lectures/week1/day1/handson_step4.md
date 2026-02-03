# 👉 Hands-on Lab - Step 4

## 👉 Step 4: AWS EC2 인스턴스 생성

**목표**: AWS EC2에서 Ubuntu 인스턴스를 생성합니다.

**명령어**:

```bash
aws ec2 run-instances --image-id ami-0c9485551d1129cd4 --count 1 --instance-type t2.micro --key-name MyKeyPair --security-groups default

```

**예상 출력**:

```

InstanceId: i-0abcdef12345678901

```

**확인 방법**:

```bash
aws ec2 describe-instances --instance-ids i-0abcdef12345678901

```

**문제 해결**:
- 문제: 인스턴스 생성 실패 → IAM 권한 확인 (https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_iam.html)
- 문제: 키 쌍 오류 → EC2 키 쌍 재생성 (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)

