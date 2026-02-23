# Hands-on Lab - Step 6

## Step 6: 안전하게 되돌리기 (revert)

**목표**: 협업 환경에서 권장되는 되돌리기 방법인 `git revert`를 사용해 "원인을 보존한 채" 수정합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 실수로 넣은 한 줄을 추가했다고 가정
echo "- Mistake: temporary note" >> README.md
git add README.md
git commit -m "docs: add temporary note (mistake)"

# 마지막 커밋을 되돌리기 (히스토리는 남김)
git revert --no-edit HEAD

# 결과 확인
git log --oneline --decorate -n 5
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
[main 7e6d5c4] Revert "docs: add temporary note (mistake)"
 1 file changed, 1 deletion(-)
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git show -n 1 --stat
tail -n 5 README.md
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `revert` 중 충돌 발생 -> Deep Dive 시나리오 1 절차와 동일하게 해결 후 커밋
- `tail: command not found` -> Git Bash/WSL 사용 또는 에디터로 파일 확인

</details>
