# Hands-on Lab - Step 7

## Step 7: 이미지 태그 및 ECR 업로드

**목표**: 클라우드 저장소에 이미지 배포

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.ap-northeast-2.amazonaws.com
docker tag devops-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.ap-northeast-2.amazonaws.com/devops-repo:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.ap-northeast-2.amazonaws.com/devops-repo:latest
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Upload complete 상태 표시
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
aws ecr describe-images --repository-name devops-repo
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 인증 실패 → AWS CLI 구성 재확인
- 문제: 이미지 업로드 실패 → 네트워크 연결 확인

</details>

---

## 실습 완료

Docker를 사용한 애플리케이션 패키징과 AWS ECR을 통한 클라우드 배포 프로세스를 완료했습니다. CI/CD 파이프라인의 기초 개념을 경험했으며, 컨테이너화 및 클라우드 인프라 통합 방법을 습득했습니다.

**다음 단계**:
- CI/CD 파이프라인 구성 실습 (GitHub Actions)
- AWS ECS 클러스터에 컨테이너 배포
- AWS CloudFormation을 활용한 인프라 as Code 실습

