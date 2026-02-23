# Hands-on Lab - Step 2

## Step 2: 첫 커밋 만들기 (작게 커밋의 시작)

**목표**: 변경 사항을 스테이징(add)하고 커밋(commit)한 뒤, 히스토리를 확인합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
git add README.md
git commit -m "docs: add initial README"

# 히스토리 확인
git log --oneline --decorate -n 3
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
[main (root-commit) 1a2b3c4] docs: add initial README
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git status
git show --stat
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `nothing to commit` -> `git status`로 변경 파일이 있는지 확인 후 파일 수정/저장
- `Author identity unknown` -> Step 1에서 `git config user.name/email` 설정

</details>
