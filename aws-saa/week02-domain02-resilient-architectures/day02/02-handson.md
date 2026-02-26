# Hands-on Lab (Console): ALB + Auto Scaling Group 구성 (간단 웹 서버)

## Goal

- Launch template + ASG + ALB를 구성해 “인스턴스가 바뀌어도 서비스가 유지”되는 구조를 만든다.
- 타겟 헬스체크가 실패하면 대상이 제외되고(또는 교체되는) 흐름을 이해한다.

## Prereqs

- EC2/ELB/ASG 생성 권한
- Region: 수업 기본 리전

## Cost Notes

- ALB/EC2는 비용이 발생할 수 있다. 실습은 짧게 수행하고 Cleanup을 반드시 한다.

## Steps

### A) Console Steps

#### 1) Security Group 준비

1. ALB용 SG 생성: 인바운드 `80`을 `0.0.0.0/0` 허용(학습용)
2. EC2용 SG 생성: 인바운드 `80`을 “ALB SG”에서만 허용

#### 2) Launch Template 생성(웹 서버 user data)

1. EC2 -> Launch Templates -> Create
2. AMI: Amazon Linux (수업 표준)
3. Instance type: 가능한 작은 타입(예: t3.micro 등)
4. Security group: EC2용 SG
5. User data(예시): Apache 설치 후 간단 페이지

```bash
#!/bin/bash
set -eux
dnf -y update || true
dnf -y install httpd
systemctl enable httpd
echo "hello from $(hostname)" > /var/www/html/index.html
systemctl start httpd
```

#### 3) Target Group 생성

1. EC2 -> Target Groups -> Create target group
2. Target type: Instances
3. Protocol/Port: HTTP:80
4. Health check path: `/`

#### 4) ALB 생성

1. EC2 -> Load Balancers -> Create -> Application Load Balancer
2. Subnets: 2개 AZ 선택(가능하면)
3. SG: ALB용 SG
4. Listener(80) -> Forward to 3) Target Group

#### 5) Auto Scaling Group 생성(Launch Template 연결)

1. ASG 생성
2. Launch template: 2)
3. VPC/Subnets: 2개 AZ 선택(가능하면)
4. Load balancing: 3) Target Group 연결
5. Desired=2, Min=2, Max=4 (학습용)

#### 6) 동작 확인

1. ALB DNS 이름으로 접속
2. 새로고침 시 `hostname`이 바뀌면 분산이 되는 것

#### 7) (옵션) “비정상” 유도 후 복구 흐름 보기

- 대상 인스턴스 하나를 종료(terminate)하면 ASG가 다시 desired를 맞추는 흐름을 관찰

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위. 필요 시 `describe-target-health` 등으로 확인 가능.

## Validation Checklist

- ASG 인스턴스가 Target group에 등록되고 “healthy”가 된다.
- ALB로 접속 시 응답이 나온다.
- 인스턴스 종료 시 ASG가 보충한다(자가 치유).

## Common Errors

- EC2 SG가 `0.0.0.0/0`에 열려 있음: 실무/시험 모두 “ALB에서만 허용”이 더 안전한 설계다.
- 타겟 그룹 포트/헬스체크 경로 오류로 unhealthy.

## Cleanup

1. Auto Scaling Group 삭제
2. Load Balancer 삭제
3. Target Group 삭제
4. Launch Template 삭제
5. Security Groups 삭제

