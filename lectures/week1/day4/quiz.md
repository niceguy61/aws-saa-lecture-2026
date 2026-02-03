# 퀴즈 (Quiz)

## 질문 1

**Docker 컨테이너에서 --mount type=bind 옵션의 주요 목적은 무엇인가요?**

A) 호스트 파일 시스템을 컨테이너에 마운트하여 실시간 동기화
B) 컨테이너 내부의 파일 시스템을 호스트에 공유
C) 네트워크 포트를 호스트와 컨테이너 간에 매핑
D) 컨테이너의 작업 디렉토리를 설정

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: bind 마운트는 호스트의 현재 디렉토리를 컨테이너의 /app 경로에 마운트하여 파일 변경 시 실시간으로 동기화하는 기능을 제공합니다. 이는 개발 중에 코드 수정을 즉시 반영할 수 있도록 합니다.

</details>

---

## 질문 2

**Docker 커맨드에서 -w /app 옵션의 역할은 무엇인가요?**

A) 컨테이너의 루트 디렉토리로 작업 디렉토리를 변경
B) 호스트의 파일 시스템을 컨테이너에 마운트
C) 컨테이너 내부에서 특정 경로를 작업 디렉토리로 설정
D) 컨테이너의 네트워크 포트를 호스트에 매핑

<details>
<summary>정답 및 해설 보기</summary>

**답**: C

**설명**: -w 옵션은 컨테이너가 명령어를 실행할 때 사용할 작업 디렉토리를 지정합니다. 예를 들어, -w /app은 컨테이너 내부에서 /app 경로를 작업 디렉토리로 설정하여 npm 명령어가 해당 경로에서 실행됩니다.

</details>

---

## 질문 3

**Docker Compose에서 watch 모드의 sync+restart 동작은 어떤 상황에서 사용되나요?**

A) 소스 코드 변경 시 즉시 재시작
B) 파일 변경 시 컨테이너를 재빌드하고 재시작
C) 네트워크 설정 변경 시 자동 업데이트
D) 환경 변수 변경 시 로그를 실시간으로 출력

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: sync+restart 동작은 파일 변경 시 컨테이너를 재빌드하고 재시작하여 변경 사항을 반영합니다. 이는 package.json과 같은 의존성 파일 변경 시 이미지 재빌드가 필요한 상황에서 사용됩니다.

</details>

---

## 질문 4

**Docker에서 secret 마운트를 파일과 환경 변수로 동시에 사용하려면 어떤 옵션을 사용해야 하나요?**

A) --mount type=secret,target=/path,env=KEY
B) --mount type=bind,source=/path,target=/path
C) --mount type=volume,source=myvol,target=/path
D) --mount type=secret,target=/path,env=KEY

<details>
<summary>정답 및 해설 보기</summary>

**답**: D

**설명**: secret 마운트는 --mount type=secret을 사용하며, target과 env 옵션을 함께 지정하면 같은 시크릿을 파일과 환경 변수로 동시에 사용할 수 있습니다. 예: --mount type=secret,id=mysecret,target=/etc/secret,env=SECRET_KEY

</details>

---

## 질문 5

**SELinux에서 bind 마운트 옵션 :z와 :Z의 주요 차이점은 무엇인가요?**

A) :z는 여러 컨테이너가 동일 마운트를 공유 가능, :Z는 호스트 파일 시스템과 동일한 권한 적용
B) :z는 컨테이너 내부에서만 파일 수정 가능, :Z는 호스트에서 수정 가능
C) :z는 마운트를 읽기 전용으로 설정, :Z는 쓰기 가능
D) :z는 SELinux 라벨을 무시, :Z는 라벨을 강제 적용

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: :z 옵션은 여러 컨테이너가 동일한 bind 마운트를 공유할 수 있도록 SELinux 라벨을 공유하게 설정합니다. :Z 옵션은 호스트 파일 시스템의 SELinux 라벨을 컨테이너 마운트에 복사하여 보안 정책을 강제합니다.

</details>

---

