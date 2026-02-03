# 👉 Hands-on Lab - Step 6

## 👉 Step 6: EC2에서 애플리케이션 테스트

**목표**: EC2 인스턴스 IP로 서비스 접근 여부 확인

**명령어**:

```bash
curl http://<EC2_PUBLIC_IP>

```

**예상 출력**:

```

HTTP 200 OK 응답 및 Nginx 기본 페이지 출력

```

**확인 방법**:

```bash
curl http://<EC2_PUBLIC_IP>/index.html

```

**문제 해결**:
- 문제: 연결 거부 → 보안 그룹 설정 확인 (https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html)
- 문제: 포트 전달 실패 → docker port webapp-container 명령어 확인

