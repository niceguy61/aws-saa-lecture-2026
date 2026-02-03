# Hands-on Lab - Step 3

## Step 3: Docker 이미지 빌드

**목표**: 애플리케이션 패키징 수행

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker build -t devops-app:latest .
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
BUILD SUCCESS 상태 표시
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker images | grep devops-app
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 빌드 실패 → Dockerfile 검증
- 문제: 네트워크 문제 → docker network ls 확인

</details>

