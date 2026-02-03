# 퀴즈 (Quiz)

## 질문 1

**Docker Compose에서 실시간 코드 수정을 위해 사용하는 명령어는 무엇인가요?**

A) docker build
B) docker run
C) docker compose up
D) docker watch

<details>
<summary>정답 및 해설 보기</summary>

**답**: D

**설명**: Docker Compose의 watch 모드는 실시간으로 파일 변경을 감지하여 컨테이너를 재시작하거나 동기화하는 기능입니다. 이는 개발 환경에서 빌드 없이 코드 변경을 즉시 반영할 수 있도록 합니다.

</details>

---

## 질문 2

**Docker Compose에서 실시간 동기화와 재시작을 동시에 수행하는 watch 모드의 액션은 무엇인가요?**

A) sync
B) restart
C) sync+restart
D) watch

<details>
<summary>정답 및 해설 보기</summary>

**답**: C

**설명**: sync+restart 액션은 파일 변경 시 즉시 컨테이너를 재시작하고, 변경된 파일을 실시간으로 동기화하여 개발 환경에서 즉시 반영할 수 있도록 합니다. 예를 들어, package.json 변경 시 이미지 재빌드 및 컨테이너 재시작이 자동 수행됩니다.

</details>

---

## 질문 3

**Dockerfile에서 파일 소유권을 설정하기 위한 옵션은 무엇인가요?**

A) --chown
B) -w
C) -v
D) --mount

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: COPY --chown 명령은 파일을 컨테이너에 복사하면서 소유권을 설정합니다. 예를 들어, COPY --chown=app:app package.json ./는 package.json 파일을 app 사용자로 소유권을 설정하여 권한 문제를 방지합니다.

</details>

---

## 질문 4

**Docker Compose에서 파일 변경을 감지하기 위한 watch 모드의 필수 옵션은 무엇인가요?**

A) path
B) action
C) target
D) ignore

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: watch 모드는 path 필드를 통해 감시할 파일 경로를 지정해야 합니다. 예를 들어, path: ./web는 ./web 디렉터리의 변경을 감지하여 컨테이너 동기화를 트리거합니다. action은 path에 따라 선택적으로 추가됩니다.

</details>

---

