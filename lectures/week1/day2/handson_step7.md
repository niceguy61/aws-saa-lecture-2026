# Hands-on Lab - Step 7

## Step 7: 정리 작업

**목표**: 실행 중인 컨테이너 및 이미지 제거

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
docker stop node-dev
docker rm node-dev
docker rmi node-app:latest
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Container 및 이미지 삭제 완료
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

- 문제: 이미지 제거 실패 → 'docker rmi -f node-app:latest' 사용
- 문제: 컨테이너 중지 실패 → 'docker kill node-dev' 명령

</details>

---

## 실습 완료

Node.js 애플리케이션을 Docker로 패키징하고 실시간 개발 환경을 구성하는 방법을 마스터했습니다. 바인드 마운트를 통한 코드 변경 감지, 포트 매핑, 로그 모니터링 기능을 익히게 되었습니다.

**다음 단계**:
- Docker Secrets 사용해 민감 정보 처리
- SSH 마운트로 GitHub 개인 저장소 클론
- BuildKit을 활용한 고급 이미지 빌드
- Kubernetes와 연동한 Docker 컨테이너 배포

