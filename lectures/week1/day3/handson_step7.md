# Hands-on Lab - Step 7

## Step 7: watch 모드 테스트

**목표**: nginx.conf 수정 후 컨테이너 재시작 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
echo "server {
  listen 80;
  location / {
    proxy_pass http://localhost:3000;
  }
}" > proxy/nginx.conf
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
docker logs에서 nginx 재시작 확인
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker-compose up --build -d && docker logs -f dev-container
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 재시작 없음 → 'docker-compose down' 후 재시도
- 문제: 포트 충돌 → 'docker ps --format "{{.Ports}}"'로 포트 확인

</details>

---

## 실습 완료

Docker 이미지 생성 및 실시간 개발 환경이 성공적으로 설정되었습니다. bind mount와 watch 모드를 통해 코드 변경 시 자동 재시작이 가능합니다.

**다음 단계**:
- Secrets를 사용한 AWS 자격 증명 설정
- SSH 마운트로 프라이빗 리포지토리 클론
- 다중 컨테이너 서비스 구성

