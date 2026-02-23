# Hands-on Lab - Step 7

## Step 7: 릴리스 단위 만들기 (tag) + 정리

**목표**: 현재 상태를 릴리스 후보로 태깅하고, 다음 단계로 넘어갈 준비를 합니다.

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 태그 생성 (주석 태그 권장)
git tag -a v0.1.0 -m "Day1 lab checkpoint"

# 태그/커밋 확인
git tag --list
git show v0.1.0 --no-patch
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
v0.1.0
tag v0.1.0
Tagger: Student <student@example.com>
Date:   ...

Day1 lab checkpoint
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
git describe --tags --always
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- `fatal: not a git repository` -> 작업 디렉토리가 저장소인지 확인(`cd devops-day1-git-lab`)
- 태그를 잘못 만들었음 -> 삭제: `git tag -d v0.1.0` (공식: https://git-scm.com/docs/git-tag)

</details>

---

## 실습 완료

- "작게 커밋 -> 공유(브랜치/PR) -> 병합 -> 검증"의 기본 루프를 경험했습니다.
- 협업에서 자주 터지는 두 가지 이슈(merge conflict, non-fast-forward)를 표준 절차로 해결했습니다.
- DevOps의 핵심이 도구 하나가 아니라 문화/자동화/측정/공유가 함께 굴러가는 구조라는 점을 확인했습니다.

**다음 단계**:
- Git 원격(remote) 추가 후 push/pull 실습(공식: https://git-scm.com/docs/git-remote)
- CI 입문: GitHub Actions로 간단한 lint/test 워크플로우 만들기(공식: https://docs.github.com/actions)
- Day 2 예고: Docker를 설치하고 첫 컨테이너를 실행하면서 "환경의 재현성"을 체감하기
