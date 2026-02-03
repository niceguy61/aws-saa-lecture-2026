# Hands-on Lab - Step 5

## Step 5: 애플리케이션 테스트

**목표**: 배포된 서비스 기능 검증

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
curl http://localhost:3000
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
HTTP 200 응답 및 애플리케이션 메시지
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
curl http://localhost:3000
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 연결 실패 → docker ps 확인
- 문제: 404 오류 → 애플리케이션 로직 점검

</details>

