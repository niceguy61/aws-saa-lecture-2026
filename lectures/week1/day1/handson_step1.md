# Hands-on Lab - Step 1

## 실습 개요

**제목**: DevOps 협업의 시작: Git으로 "작게, 자주" 통합하기

**목적**: DevOps의 핵심(짧은 피드백 루프, 공유, 자동화)의 출발점인 "형상관리 + 협업 흐름"을 Git으로 직접 경험합니다. 팀에서 문제가 생기는 지점(충돌, push 거절)을 일부러 만들고, 표준 절차로 해결하는 연습을 합니다.

**학습 목표**:
- Git 저장소를 초기화하고 커밋/브랜치/병합의 기본 흐름을 수행한다
- 충돌(conflict)과 non-fast-forward 같은 협업 이슈를 진단하고 해결한다
- "작게, 자주" 변경을 통합하는 이유를 지표(리드타임/실패율/복구시간) 관점으로 설명한다

**예상 소요 시간**: 60-90분

**난이도**: Beginner

### 실습 흐름도

```mermaid
flowchart LR
  Work[작업] --> Commit[작게 커밋]
  Commit --> PR[리뷰/공유]
  PR --> Merge[빠른 병합]
  Merge --> Verify[검증]
  Verify --> Work
```

## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Git 설치
  - 설치 가이드(공식): https://git-scm.com/downloads
- 터미널 환경(Git Bash 또는 WSL)
  - WSL 설치(공식): https://learn.microsoft.com/windows/wsl/install
- 텍스트 에디터(예: VS Code)
  - 설치/설정(공식): https://code.visualstudio.com/docs/setup/windows

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

- Git 버전 확인
  - 명령어: `git --version`
  - 문서(공식): https://git-scm.com/docs/git
- Git 사용자 정보 설정(커밋 작성자)
  - 문서(공식): https://git-scm.com/docs/git-config
- 기본 브랜치명을 `main`으로 통일(선택)
  - 문서(공식): https://git-scm.com/docs/git-config#Documentation/git-config.txt-initdefaultBranch

</details>

---

## Step 1: 작업 공간 준비 및 저장소 초기화

**목표**: 실습용 폴더를 만들고 Git 저장소를 초기화한 뒤, 커밋 작성자 정보를 설정합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 작업 폴더 생성 및 이동
mkdir -p devops-day1-git-lab
cd devops-day1-git-lab

# Git 저장소 초기화 및 기본 브랜치 설정
git init
git branch -M main

# 커밋 작성자 설정(프로젝트 범위)
git config user.name "Student"
git config user.email "student@example.com"

# 첫 파일 생성
cat > README.md << 'EOF'
# DevOps Day 1 Git Lab
This repo is for practicing small, frequent integrations.
EOF
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Initialized empty Git repository in .../devops-day1-git-lab/.git/
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git status
git config --list --local | grep -E "user.name|user.email"
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `git: command not found` -> Git 설치 후 터미널 재시작(공식 다운로드: https://git-scm.com/downloads)
- `grep: command not found` -> Windows 기본 cmd/powershell이 아니라 Git Bash 또는 WSL 사용

</details>
