# Hands-on Lab - Step 6

## Step 6: AWS ECR 리포지토리 생성

**목표**: 클라우드 저장소 준비

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
aws ecr create-repository --repository-name devops-repo
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
repositoryUri 포함한 JSON 응답
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
aws ecr describe-repositories --repository-names devops-repo
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 권한 오류 → IAM 정책 확인
- 문제: 리포지토리 생성 실패 → AWS 서비스 상태 확인

</details>

