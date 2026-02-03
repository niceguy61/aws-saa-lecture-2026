# Hands-on Lab - Step 7

## Step 7: 네트워크 정리

**목표**: 사용한 리소스 정리 및 상태 점검

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker stop web-app db dev-env # 컨테이너 정지
docker network prune # 네트워크 정리
docker system prune -f # 전체 정리
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
정리 완료 메시지 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker ps -a && docker network ls
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 강제 정리 필요 → docker rm -f 컨테이너 명령어 사용
- 문제: 권한 문제 → sudo로 명령어 재실행

</details>

---

## 실습 완료

Docker 네트워크 구성, 컨테이너 통신, 포트 맵핑, 바인드 마운트, Docker Compose 설정 등을 통한 네트워킹 기초 이해 완료

**다음 단계**:
- Docker 네트워크 정책 설정 실습
- Swarm 모드에서의 네트워크 구성
- Linking 기능을 활용한 컨테이너 연결
- Kubernetes 네트워크 개념 이해
- 컨테이너 간 DNS 설정 구성

