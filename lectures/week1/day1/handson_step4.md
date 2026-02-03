# Hands-on Lab - Step 4

## Step 4: 컨테이너 실행

**목표**: 로컬에서 애플리케이션 테스트

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d -p 3000:3000 --name devops-container devops-app:latest
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
CONTAINER ID 출력 및 포트 매핑 확인
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps | grep devops-container
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌 → docker ps 확인
- 문제: 컨테이너 시작 실패 → docker logs 확인

</details>

