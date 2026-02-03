# 퀴즈 (Quiz)

## 질문 1

**Dockerfile에서 사용되는 기본 이미지로 적절한 것은 무엇인가요?**

A) ubuntu:latest
B) node:24-alpine
C) python:3.9
D) alpine:3.18

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: 주어진 컨텍스트에서 명시적으로 'node:24-alpine'이 기본 이미지로 사용됨을 확인할 수 있습니다. 이는 Node.js 애플리케이션을 Alpine Linux 기반 컨테이너에서 실행하기 위한 선택입니다.

</details>

---

## 질문 2

**Docker 컨테이너 내에서 npm install과 npm run dev를 실행하기 위한 명령어는 무엇인가요?**

A) bash -c 'npm install && npm run dev'
B) sh -c 'npm install && npm run dev'
C) cmd /c 'npm install && npm run dev'
D) powershell -Command 'npm install && npm run dev'

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: Alpine Linux는 bash가 설치되지 않아 sh를 사용해야 합니다. 컨텍스트에서 명시적으로 'sh -c'가 사용되었으며, 이는 npm 명령어 실행을 위한 올바른 쉘입니다.

</details>

---

## 질문 3

**Docker Compose에서 watch 모드의 sync+restart 액션은 어떤 동작을 수행하나요?**

A) 파일 변경 시 즉시 동기화만 수행
B) 파일 변경 시 컨테이너 재시작을 포함한 동기화
C) 파일 변경 시 이미지를 재빌드하지 않음
D) 파일 변경 시 호스트와 컨테이너의 파일 시스템을 완전히 동기화

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: sync+restart 액션은 파일 변경 시 컨테이너를 재시작하는 동시에 변경된 파일을 동기화합니다. 이는 package.json 변경 시 Compose가 이미지를 재빌드하고 서비스 컨테이너를 재생성하는 동작과 관련이 있습니다.

</details>

---

## 질문 4

**Dockerfile에서 --chown 플래그의 주요 목적은 무엇인가요?**

A) 이미지 크기를 줄이기 위한 최적화
B) 파일 소유권을 특정 사용자에게 할당하여 권한 문제 방지
C) 빌드 시간을 최소화하기 위한 캐시 전략
D) 네트워크 포트를 호스트와 매핑

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: COPY --chown 플래그는 파일을 컨테이너에 복사할 때 특정 사용자 소유권을 설정하여, 컨테이너 내부에서 파일 수정 권한이 필요한 경우 권한 문제를 방지하는 데 사용됩니다.

</details>

---

