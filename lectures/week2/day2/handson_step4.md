# Hands-on Lab - Step 4

## Step 4: Docker 컨테이너 실행

**목표**: 실시간 코드 동기화 기능을 갖춘 컨테이너 실행

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# Docker Compose로 컨테이너 실행
docker-compose up --build
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Application is running at http://localhost:3000
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f <container-id>
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 포트 충돌
해결: 다른 포트로 변경하거나 'docker ps' 명령어로 실행 중인 컨테이너 확인

</details>

