# Hands-on Lab (Console): T 계열 크레딧 지표 관찰 + CPU 병목 확인

## Goal

- EC2(t3.micro 등)를 띄우고 Session Manager로 접속해 CPU 부하를 걸어본다.
- CloudWatch에서 CPUUtilization/CPUCreditBalance 변화를 확인한다.
- “지속 부하에는 T 계열이 함정”이라는 시험 포인트를 체감한다.

## Prereqs

- EC2 생성 권한
- IAM role 생성/부착 권한(SSM)
- Region: 수업 기본 리전

## Cost Notes

- 작은 인스턴스로 짧게 테스트하고 종료한다.

## Steps

### A) Console Steps

#### 1) EC2용 IAM Role 생성(SSM)

1. IAM -> Roles -> Create role
2. Trusted entity: AWS service -> EC2
3. Policy: `AmazonSSMManagedInstanceCore` 연결
4. Role name: `SAA-Week3-SSMRole`

#### 2) EC2 인스턴스 생성

1. EC2 -> Launch instance
2. AMI: Amazon Linux
3. Instance type: `t3.micro`(가능하면)
4. IAM instance profile: 1)의 role 선택
5. (학습용) 인바운드는 열 필요 없음(Session Manager 사용)
6. Launch

#### 3) Session Manager로 접속 후 CPU 부하

1. EC2 -> Instances -> 해당 인스턴스 선택
2. Connect -> Session Manager
3. 아래 명령 실행(5분 정도 부하)

```bash
sudo dnf -y install stress-ng || sudo yum -y install stress-ng
stress-ng --cpu 1 --timeout 300s
```

#### 4) CloudWatch 지표 확인

1. EC2 인스턴스 -> Monitoring 탭 또는 CloudWatch metrics
2. CPUUtilization 확인
3. (T 계열이면) CPUCreditBalance/CPUCreditUsage 확인

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위.

## Validation Checklist

- Session Manager로 접속해 부하를 걸 수 있다.
- CloudWatch에서 CPUUtilization이 상승하는 것을 확인한다.
- (T 계열) CPUCreditBalance가 감소할 수 있음을 설명한다.

## Common Errors

- Session Manager 접속이 안 됨: 인스턴스 프로파일/SSM role 연결, SSM agent 상태 확인(Amazon Linux는 기본 포함이 일반적).
- 지표가 바로 안 보임: 약간의 지연이 있다.

## Cleanup

1. 인스턴스 종료(terminate)
2. (선택) IAM role 삭제

