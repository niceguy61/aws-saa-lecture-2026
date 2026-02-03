# 👉 Hands-on Lab - Step 7

## 👉 Step 7: 로그 모니터링

**목표**: nodemon 로그 확인

**명령어**:

```bash
docker logs -f <container-id>

```

**예상 출력**:

```

nodemon -L src/index.js 로그

```

**확인 방법**:

```bash
docker logs -f <container-id>

```

**문제 해결**:
- 문제: 로그 출력 없음
  해결: 컨테이너 재시작 후 재확인

---

## 🎉 실습 완료

Docker 기반 Node.js 개발 환경이 성공적으로 구성되었습니다. 실시간 코드 변경 시 자동 재시작 기능을 사용해 개발을 진행할 수 있습니다.

**다음 단계**:
- Docker Compose로 다중 서비스 구성
- AWS Secrets Manager 연동
- Jupyter Notebook 환경 추가

