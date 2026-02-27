# Hands-on Lab (Console): gp3 볼륨 구성 + 간단 I/O 테스트(SSM)

## Goal

- gp3 EBS 볼륨을 만들고 IOPS/throughput을 변경해볼 수 있다.
- EC2에 붙여 간단 I/O 테스트를 실행하고(SSM), CloudWatch 지표를 확인한다.

## Prereqs

- EC2/EBS 생성 권한
- IAM role 생성/부착 권한(SSM)
- Region: 수업 기본 리전

## Cost Notes

- EC2/EBS는 비용이 발생할 수 있다. 짧게 테스트하고 Cleanup한다.

## Steps

### A) Console Steps

#### 1) EC2용 IAM Role(SSM) 준비

- Day01에서 만든 `SAA-Week3-SSMRole`이 있으면 재사용.

#### 2) EC2 인스턴스 1대 생성

1. Amazon Linux + 작은 타입(t3.micro 등)
2. IAM instance profile: SSM role
3. Launch

#### 3) gp3 볼륨 생성 + IOPS/throughput 설정

1. EC2 -> Volumes -> Create volume
2. Type: gp3
3. Size: 예) 20GiB
4. IOPS/Throughput: 기본값에서 변경(학습용, 과도하게 올리지 않기)
5. AZ: 2)의 인스턴스와 같은 AZ
6. Create

#### 4) 볼륨을 인스턴스에 Attach

1. 볼륨 선택 -> Attach volume
2. Instance: 2)의 인스턴스
3. Device 예: `/dev/xvdf`

#### 5) Session Manager로 접속 후 디스크 준비 + 간단 테스트

1. 인스턴스 -> Connect -> Session Manager
2. 아래 명령 실행(마운트 후 간단 write 테스트)

```bash
lsblk
sudo mkfs -t xfs /dev/xvdf || sudo mkfs -t ext4 /dev/xvdf
sudo mkdir -p /mnt/test
sudo mount /dev/xvdf /mnt/test
sudo dd if=/dev/zero of=/mnt/test/blob bs=1M count=512 conv=fsync
sync
```

#### 6) CloudWatch 지표 확인

1. EC2 -> Monitoring 또는 CloudWatch metrics
2. VolumeWriteBytes/VolumeWriteOps/VolumeQueueLength 등을 확인

### B) Optional: CLI Equivalents (for validation/automation)

- 수업은 콘솔이 1순위.

## Validation Checklist

- gp3 볼륨을 만들고 IOPS/throughput 설정을 확인했다.
- 인스턴스에 attach 후 파일시스템/마운트를 했다.
- 간단 I/O 수행 후 지표 변화를 설명할 수 있다.

## Common Errors

- AZ 불일치: EBS는 같은 AZ 인스턴스에만 attach 가능.
- 장치명이 다르게 보임: `lsblk`로 실제 디바이스를 확인한다.

## Cleanup

1. 인스턴스 종료
2. EBS 볼륨 삭제
3. (선택) IAM role 삭제

