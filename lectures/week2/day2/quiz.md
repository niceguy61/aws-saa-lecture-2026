# 퀴즈 (Quiz)

## 질문 1

**Docker 컨테이너에서 -w /app 플래그의 주요 역할은 무엇인가요?**

A) 컨테이너의 루트 디렉토리로 작업 디렉토리를 변경
B) 호스트의 현재 디렉토리를 컨테이너의 /app 디렉토리에 바인드 마운트
C) 컨테이너 내부에서 실시간 파일 변경을 감시
D) 컨테이너의 네트워크 포트를 호스트에 매핑

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: -w /app은 컨테이너 실행 시 작업 디렉토리를 /app으로 설정하는 옵션입니다. 이는 컨테이너 내부에서 명령어가 실행되는 기준 경로를 변경하는 역할을 합니다. 예를 들어 npm install 명령어가 /app 디렉토리 내부에서 실행됩니다.

</details>

---

## 질문 2

**--mount type=bind,src=.,target=/app 옵션의 주요 목적은 무엇인가요?**

A) 호스트의 현재 디렉토리를 컨테이너의 /app 디렉토리에 마운트
B) 컨테이너의 파일 시스템을 호스트에 공유
C) Dockerfile의 COPY 명령어 대체
D) 네트워크 포트를 호스트에 매핑

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: 이 옵션은 호스트의 현재 작업 디렉토리를 컨테이너의 /app 디렉토리에 바인드 마운트하여, 호스트와 컨테이너 간 파일 변경을 실시간으로 동기화하는 역할을 합니다. 이는 개발 중에 소스 코드 수정을 즉시 컨테이너에 반영할 수 있도록 합니다.

</details>

---

## 질문 3

**npm install && npm run dev 명령어가 실행할 때 어떤 동작을 수행하나요?**

A) 컨테이너의 포트를 호스트에 오픈
B) 패키지 의존성을 설치하고 개발 서버를 실행
C) Dockerfile을 실시간으로 재구성
D) 컨테이너 로그를 실시간으로 출력

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: npm install은 패키지 의존성을 설치하고, npm run dev는 package.json의 dev 스크립트를 실행합니다. 이 스크립트는 nodemon을 통해 서버를 실행하여 코드 변경 시 자동 재시작하는 기능을 제공합니다.

</details>

---

## 질문 4

**Docker Compose의 watch 모드에서 sync와 sync+restart의 차이는 무엇인가요?**

A) sync는 파일 변경 시 재시작, sync+restart는 이미지 재빌드
B) sync는 실시간 동기화, sync+restart는 파일 변경 시 재빌드
C) sync는 네트워크 재설정, sync+restart는 포트 재할당
D) sync는 파일 무시, sync+restart는 로그 재출력

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: sync는 파일 변경 시 즉시 컨테이너를 재시작하지 않고 파일을 동기화하는 반면, sync+restart는 파일 변경 시 이미지 재빌드 및 컨테이너 재생성을 수행합니다. package.json 변경 시 Compose는 이미지 재빌드를 트리거하는 이벤트를 발생시킵니다.

</details>

---

## 질문 5

**Docker에서 secret을 파일과 환경 변수로 동시에 마운트하는 옵션은 무엇인가요?**

A) --mount type=secret,id=aws-key-id,env=AWS_ACCESS_KEY_ID
B) --mount type=bind,src=/secrets,target=/app
C) --mount type=volume,source=myvol,target=/data
D) --mount type=ssh,source=github.com,target=/src

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: secret 마운트 옵션에서 target과 env 필드를 함께 사용하면, secret 파일을 컨테이너 파일 시스템에 마운트하고 동시에 환경 변수로 전달할 수 있습니다. 예시에서 AWS凭证은 파일과 환경 변수로 동시에 사용됩니다.

</details>

---

