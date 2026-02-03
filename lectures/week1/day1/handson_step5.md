# 👉 Hands-on Lab - Step 5

## 👉 Step 5: 컨테이너 실행 및 포트 공유

**목표**: Docker 컨테이너를 실행하고 포트를 EC2로 전달합니다.

**명령어**:

```bash
docker run -d -p 80:80 --name webapp-container devops-webapp

```

**예상 출력**:

```

Container ID가 출력됨

```

**확인 방법**:

```bash
docker ps

```

**문제 해결**:
- 문제: 포트 충돌 → docker run -p 8080:80로 변경
- 문제: 컨테이너 정지 → docker start webapp-container 실행

