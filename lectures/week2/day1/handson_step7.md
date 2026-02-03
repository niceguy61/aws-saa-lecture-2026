# Hands-on Lab - Step 7

## Step 7: 환경 정리 및 검증

**목표**: 실행 결과 검증 및 자원 해제

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 컨테이너 정지 및 삭제
docker-compose down

# Docker 이미지 및 볼륨 정리
docker system prune -f
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
모든 컨테이너/이미지/볼륨 제거됨
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps -a && docker volume ls
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 이미지 삭제 실패 시: `docker rmi node:24-alpine` 실행
- 문제: 볼륨残留 시: `docker volume rm <volume-name>` 실행

</details>

---

## 실습 완료

Dockerfile을 통한 애플리케이션 패키징, bind mount를 활용한 실시간 파일 동기화, Docker Compose watch 모드 설정 및 SELinux 옵션 적용을 완료했습니다. 개발 환경에서의 빌드/재구성 프로세스를 정확히 이해했습니다.

**다음 단계**:
- AWS 시크릿 마운트와 SSH 마운트 연동 실습
- Multi-stage build로 이미지 최소화
- Docker Compose 네트워크 설정 구성
- CI/CD 파이프라인 연동 테스트
- Kubernetes 배포 준비

