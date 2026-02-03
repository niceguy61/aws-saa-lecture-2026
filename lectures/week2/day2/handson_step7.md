# Hands-on Lab - Step 7

## Step 7: 환경 정리

**목표**: 실행 중인 컨테이너 및 이미지 정리

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 컨테이너 중지
docker-compose down
# 이미지 삭제
docker image prune -f
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Container and image removed
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps && docker images
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 강제 중단 필요 시
해결: 'docker kill <container-id>' 명령어로 컨테이너 종료

</details>

---

## 실습 완료

Docker Registry 서비스와 실시간 코드 동기화 기능을 통합한 개발 환경을 성공적으로 구성했습니다. 이 실습을 통해 Docker Compose와 볼륨 마운트를 활용한 개발 흐름을 익혔습니다.

**다음 단계**:
- Docker Registry를 외부 네트워크에 노출하는 방법 학습
- CI/CD 파이프라인과의 통합 방법 탐색
- 다중 컨테이너 구성에서의 네트워크 설정 연습

