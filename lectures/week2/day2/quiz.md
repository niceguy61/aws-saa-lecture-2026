# 퀴즈 (Quiz)

## 질문 1

**Docker 컨테이너에서 `-w /app` 플래그의 주요 기능은 무엇인가요?**

A) 컨테이너의 포트를 호스트 포트에 매핑합니다
B) 커맨드가 실행될 작업 디렉토리를 설정합니다
C) 이미지의 기본 이미지를 변경합니다
D) 컨테이너의 로그를 실시간으로 표시합니다

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  `-w /app` 플래그는 커맨드가 실행될 작업 디렉토리를 지정합니다. 이는 컨테이너 내부에서 명령어가 실행될 기준 경로를 설정하는 역할로, 예를 들어 `npm install`과 같은 명령어가 `/app` 디렉토리에서 실행됩니다.

</details>

---

## 질문 2

**Node.js 애플리케이션을 실행하기 위한 Docker 명령어는 무엇인가요?**

A) `docker run --rm -it node:alpine bash`
B) `sh -c "npm install && npm run dev"`
C) `docker-compose up --build`
D) `docker logs -f <container-id>`

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  `sh -c "npm install && npm run dev"` 명령어는 Alpine Linux에서 bash 대신 sh를 사용하여 npm 패키지를 설치하고 개발 서버를 실행합니다. 이는 `package.json` 파일의 `dev` 스크립트가 `nodemon`을 사용하기 때문입니다.

</details>

---

## 질문 3

**Docker Compose에서 `--mount` 옵션을 사용할 때 bind mount의 목적은 무엇인가요?**

A) 호스트 파일 시스템을 컨테이너에 마운트하여 실시간 동기화
B) 네트워크 포트를 호스트에 노출
C) 컨테이너의 로그를 파일로 저장
D) 이미지 버전을 관리

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  `--mount type=bind,src=.,target=/app`는 호스트의 현재 디렉토리를 컨테이너의 `/app` 디렉토리에 바인드 마운트하여, 파일 변경 시 컨테이너 내부에서 즉시 반영되도록 합니다. 이는 개발 중에 소스 코드 변경을 실시간으로 반영할 수 있게 합니다.

</details>

---

## 질문 4

**Docker Compose의 `watch` 모드에서 `sync+restart` 액션의 주요 특징은 무엇인가요?**

A) 파일 변경 시 즉시 동기화 및 컨테이너 재시작
B) 파일 변경 시만 동기화
C) 네트워크 설정을 자동으로 조정
D) 이미지 버전을 자동으로 업데이트

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  `sync+restart` 액션은 특정 파일이 변경되면 해당 파일을 실시간으로 동기화하고 컨테이너를 재시작하여 변경 사항을 반영합니다. 예를 들어 `package.json` 변경 시 Compose가 이미지를 다시 빌드하고 서비스를 재시작합니다.

</details>

---

## 질문 5

**Docker에서 비밀 정보를 파일과 환경 변수로 동시에 마운트할 수 있는 옵션은 무엇인가요?**

A) `--mount type=secret,id=aws-secret-key,env=AWS_SECRET_ACCESS_KEY`
B) `--mount type=bind,src=/secrets,target=/app`
C) `--mount type=ssh,src=/ssh,target=/root/.ssh`
D) `--mount type=volume,src=my-volume,target=/data`

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  `--mount type=secret,id=aws-secret-key,env=AWS_SECRET_ACCESS_KEY`는 비밀 정보를 파일로 마운트하고 동시에 환경 변수로 전달합니다. 이는 AWS secret를 파일과 환경 변수 두 가지 방식으로 접근할 수 있도록 합니다.

</details>

---

