# Hands-on Lab - Step 3

## Step 3: 브랜치로 변경을 격리하고 PR을 가정하기

**목표**: 기능 브랜치를 만들고 작은 변경을 커밋하여, 리뷰/공유(PR)를 가정한 흐름을 만듭니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 브랜치 생성 및 이동
git checkout -b feature/culture-notes

# 파일 수정
cat >> README.md << 'EOF'

## Notes
- Culture: blame less, learn more.
- Small batch changes reduce risk.
EOF

git add README.md
git commit -m "docs: add DevOps culture notes"

# 브랜치 확인
git branch --show-current
git log --oneline --decorate -n 3
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
feature/culture-notes
abcd123 (HEAD -> feature/culture-notes) docs: add DevOps culture notes
1a2b3c4 (main) docs: add initial README
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git diff main..HEAD
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `pathspec 'README.md' did not match` -> 현재 디렉토리가 저장소인지 확인(`pwd`, `git status`)
- `cat: command not found` -> Git Bash 또는 WSL 사용(에디터로 직접 수정해도 됨)

</details>
