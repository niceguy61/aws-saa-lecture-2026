# Mermaid Lint (GitHub Rendering Safety)

이 저장소의 Mermaid 다이어그램은 GitHub 렌더러에서 깨지는 케이스가 있어, 최소한의 안전 규칙을 강제한다. 기본 검사 대상은 현재 활성 과정인 `cloud-native/`이다.

## Run

```powershell
powershell -File scripts/mermaid_lint.ps1
```

Strict mode(경고도 실패 처리):

```powershell
powershell -File scripts/mermaid_lint.ps1 -Strict
```

## Rules (What Fails)

- Mermaid fence 미종료: ` ```mermaid ` 이후 closing fence ` ``` ` 누락
- Mermaid 블록 안에 탭(tab) 문자
- Mermaid 블록 안에 스마트 따옴표(“ ”)
- `-. (label) .->` 형태의 dashed edge 라벨
- `sequenceDiagram`의 `participant ... as ...` 별칭에 `()`, `/` 포함
- flowchart 노드 라벨 `ID[Label]`의 `Label`에 `()`, `/` 포함
- (기본은 경고) `ID[Label]`의 `Label`에 `:` 포함 (렌더러에 따라 깨질 수 있음)

## Fix Patterns

- `/` 대신 공백 또는 `and` 사용: `Instance ENI`, `R and X family`
- `()` 제거: `Workload - Role`, `S3 - versioning on`
- `:` 제거: `CloudWatch metrics` 또는 `SCP - Org OU Account`
- dashed edge 라벨은 괄호 없이: `A -. alternative .-> B`

