# Hands-on Lab - Step 4

## Step 4: 코드 수정 및 실시간 동기화 테스트

**목표**: src/index.js 수정 후 컨테이너 반영 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
echo 'console.log("Updated Docker!");' > src/index.js
docker logs -f myapp-container
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Updated Docker! 메시지 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f myapp-container | grep 'Updated'
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 코드 변경 무반영 -> 해결: --mount type=bind 설정 재확인
- 문제: 로그 출력 지연 -> 해결: docker logs --tail 100 myapp-container

</details>

