# 👉 Hands-on Lab - Step 8

## 👉 Step 8: 정리 작업

**목표**: 실행 중인 컨테이너 정지 및 삭제

**명령어**:

```bash
docker stop myapp-container && docker rm myapp-container

```

**예상 출력**:

```

Container 정지 및 삭제 완료

```

**확인 방법**:

```bash
docker ps

```

**문제 해결**:
- 문제: 컨테이너 존재하지 않음 -> docker ps -a 확인

---

## 🎉 실습 완료

Docker를 사용한 개발 환경 구성 및 실시간 리로드 기능을 성공적으로 테스트했습니다. 바인드 마운트를 통해 호스트 파일 시스템과 컨테이너 간 실시간 동기화를 확인할 수 있습니다.

**다음 단계**:
- Docker Compose로 다중 서비스 구성 시도
- AWS Secret Manager와 연동한 보안 설정 추가
- Jupyter Notebook 환경에서의 볼륨 마운트 설정

