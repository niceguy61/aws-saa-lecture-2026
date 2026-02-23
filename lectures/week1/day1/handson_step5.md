# Hands-on Lab - Step 5

## Step 5: 변경 이력을 읽기 좋게 만들기 (log, diff, blame)

**목표**: 히스토리/변경 내역을 확인하는 기본 명령을 익혀, "왜 이렇게 됐지?"를 빠르게 답할 수 있게 합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 최근 커밋 확인
git log --oneline --decorate --graph -n 10

# 특정 파일 변경 내역
git log -p -- README.md -n 3

# 누가 어느 줄을 바꿨는지(협업에서 매우 자주 씀)
git blame README.md | head -n 20
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
* 9f8e7d6 (HEAD -> main) merge: resolve README conflict
* abcd123 docs: add automation note
* 1a2b3c4 docs: add initial README
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git log --oneline -n 1
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `head: command not found` -> Git Bash/WSL 사용 또는 출력 줄 수만 눈으로 확인
- `fatal: no such path` -> 파일명/경로를 확인(`ls`, `git ls-files`)

</details>
