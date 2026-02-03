# 👉 Hands-on Lab - Step 5

## 👉 Step 5: 컨테이너 실행

**목표**: 실시간 개발 환경 실행

**명령어**:

```bash
docker run -p 3000:3000 -v $(pwd):/app -w /app myapp

```

**예상 출력**:

```

nodemon 로그 출력

```

**확인 방법**:

```bash
docker logs -f <container-id>

```

**문제 해결**:
- 문제: 포트 충돌
  해결: 다른 포트로 변경 후 재시도

