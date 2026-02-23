# Hands-on Lab - Step 4

## Step 4: 병합 충돌을 일부러 만들고 해결하기

**목표**: main에서도 같은 파일을 수정해서 충돌을 만들고, 표준 절차로 해결합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 1) main에서 같은 파일의 같은 구간을 수정 (충돌 유도)
git checkout main
cat >> README.md << 'EOF'

## Notes
- Automation: automate build/test/deploy.
EOF
git add README.md
git commit -m "docs: add automation note"

# 2) feature 브랜치를 main에 병합 -> 충돌 발생 가능
git merge feature/culture-notes

# 3) 충돌 확인
git status
git diff --name-only --diff-filter=U

# 4) README.md를 열어서 충돌 마커를 정리한 뒤 add/commit
git add README.md
git commit -m "merge: resolve README conflict"
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git status
git log --oneline --decorate -n 5
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 충돌 마커(`<<<<<<<`)를 남긴 채 커밋됨 -> 파일에서 마커를 제거하고 다시 커밋(또는 `git commit --amend`)
- 병합을 취소하고 싶음 -> `git merge --abort` (공식: https://git-scm.com/docs/git-merge)

</details>
