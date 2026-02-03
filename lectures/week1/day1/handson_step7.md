# 👉 Hands-on Lab - Step 7

## 👉 Step 7: 로그 모니터링

**목표**: 컨테이너 로그를 실시간으로 확인합니다.

**명령어**:

```bash
docker logs -f webapp-container

```

**예상 출력**:

```

실시간 로그 출력

```

**확인 방법**:

```bash
docker logs webapp-container

```

**문제 해결**:
- 문제: 로그 출력 없음 → docker logs --tail 100 webapp-container로 확인
- 문제: 컨테이너 정지 → docker start webapp-container 실행

---

## 🎉 실습 완료

Docker 컨테이너를 AWS EC2에 성공적으로 배포하고 로그를 확인했습니다. 이 실습을 통해 CI/CD 파이프라인의 기본 흐름을 이해했습니다.

**다음 단계**:
- AWS CodePipeline을 사용한 자동화 배포 구현
- Docker Compose로 다중 컨테이너 배포
- CloudWatch로 로그 모니터링 설정

