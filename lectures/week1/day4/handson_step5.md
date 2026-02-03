# Hands-on Lab - Step 5

## Step 5: 포트 접근 테스트

**목표**: 브라우저를 통한 서버 접근 테스트

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
curl http://localhost:3000
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Hello Docker! 또는 Updated Docker! 응답
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

- 문제: 접근 거부 -> 해결: docker port myapp-container 확인
- 문제: 브라우저 오류 -> 해결: 포트 3000이 열려 있는지 확인

</details>

