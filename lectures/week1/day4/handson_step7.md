# Hands-on Lab - Step 7

## Step 7: 환경 변수 및 비밀 정보 처리

**목표**: AWS secret 환경 변수 통합

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker run -d --name myapp-secret \
  -e AWS_ACCESS_KEY_ID=mock_key \
  -e AWS_SECRET_ACCESS_KEY=mock_secret \
  -e AWS_SESSION_TOKEN=mock_token \
  myapp:dev \
  sh -c "aws s3 cp s3://test-bucket/file.txt ./"

```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
S3 파일 다운로드 완료
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
ls -l file.txt
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 권한 오류 -> 해결: --mount type=secret 옵션 추가
- 문제: S3 접근 실패 -> 해결: AWS CLI 구성 및 키 검증

</details>

---

## 실습 완료

Docker 컨테이너를 통해 실시간 코드 동기화 및 개발 서버 실행을 성공적으로 구현했습니다. Dockerfile 작성, bind mount 설정, 로그 모니터링, 포트 테스트, Docker Compose 사용법, 비밀 정보 처리 기법을 익혔습니다.

**다음 단계**:
- Docker Swarm으로 서비스 확장
- Kubernetes로 컨테이너 오케스트레이션
- CI/CD 파이프라인 구성
- Docker Desktop에 GPU 지원 추가
- Multi-stage Build 최적화

