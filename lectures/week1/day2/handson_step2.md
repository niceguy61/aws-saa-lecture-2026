# Hands-on Lab - Step 2

## Step 2: 첫 컨테이너 실행 (hello-world)

**목표**: "이미지 pull -> 컨테이너 실행 -> 종료" 흐름을 가장 단순한 예제로 확인합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run --rm hello-world
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker images | head -n 5
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 다운로드가 오래 걸림 -> 네트워크 상태 확인 후 재시도, 프록시/미러 검토
- `head: command not found` -> Git Bash/WSL 사용 또는 `docker images` 출력만 확인

</details>

