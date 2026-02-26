# Hands-on Lab (Console): Scheduled Scaling으로 “야간 0” 비용 최적화 설계(학습용)

## Goal

- Auto Scaling Group에 scheduled action을 추가해 “업무시간만 켜고 야간에는 0” 패턴을 만든다.
- 실제로 인스턴스를 오래 켜지 않고, 설정 흐름 중심으로 학습한다.

## Prereqs

- EC2/ASG 생성 권한
- Region: 수업 기본 리전

## Cost Notes

- 인스턴스/ALB를 실제로 띄우면 비용이 발생할 수 있다.
- 학습용으로 min/desired를 0으로 두고 “설정만” 확인해도 된다.

## Steps

### A) Console Steps

#### 1) Launch Template 생성(간단)

1. EC2 -> Launch Templates -> Create
2. AMI: Amazon Linux
3. Instance type: 가능한 작은 타입
4. Security group: 기본(실습 목적상 인바운드 불필요)

#### 2) Auto Scaling Group 생성

1. ASG 생성(Launch template 연결)
2. Subnets: 2개 AZ 선택(가능하면)
3. Desired=0, Min=0, Max=2 (학습용)

#### 3) Scheduled action 추가(업무시간 1, 야간 0)

1. ASG -> Automatic scaling -> Scheduled actions
2. “scale-up” 액션: 특정 시간에 desired/min을 1로
3. “scale-down” 액션: 특정 시간에 desired/min을 0으로
4. 타임존/반복 주기는 수업 운영에 맞게 설정

#### 4) (설명 체크) 시험형 문장으로 정리

- “비피크에 리소스를 줄인다” 요구가 있으면 scheduled scaling은 정답 후보가 된다.

### B) Optional: 실제 동작 관찰(비용 주의)

- scale-up 시점에 인스턴스가 생성되고 scale-down 시점에 0으로 내려가는 것을 관찰할 수 있다.

## Validation Checklist

- ASG의 min/desired를 시간 기반으로 바꾸는 구성이 가능함을 확인했다.
- 비용 최적화 관점(비피크 0)으로 설명할 수 있다.

## Cleanup

1. ASG 삭제
2. Launch Template 삭제

