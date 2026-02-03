# 퀴즈 (Quiz)

## 질문 1

**Dockerfile에서 사용되는 기본 이미지로 올바른 것은 무엇인가요?**

A) ubuntu:latest  
B) node:24-alpine  
C) python:3.9  
D) alpine:3.18  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  
**node:24-alpine**는 Node.js 애플리케이션을 실행하기 위한 기본 이미지입니다. **Alpine Linux**는 경량 Linux 배포판으로, 일반적인 Ubuntu나 Debian 대비 약 50% 적은 크기로 작동합니다. 이는 Docker 컨테이너의 부팅 시간을 단축하고, 네트워크 사용량을 줄이는 데 유리합니다.  
예를 들어, `FROM node:24-alpine` 명령어는 Node.js 24 버전을 기반으로 한 Alpine Linux 이미지를 선택하는 뜻입니다. 이는 이미지 크기를 최소화하면서도 필요한 기능은 모두 제공합니다.  
**오답 이유**:  
- A) ubuntu:latest는 일반적인 Ubuntu 이미지로, 크기가 더 큽니다.  
- C) python:3.9는 Python 환경을 제공하지만, Node.js 애플리케이션과 관련이 없습니다.  
- D) alpine:3.18은 Alpine Linux의 버전이지만, Node.js가 포함되어 있지 않아 사용할 수 없습니다.  
**최적화 이유**: Alpine Linux를 사용하면 컨테이너의 크기를 약 50% 줄일 수 있어 배포 시 네트워크 대역폭과 스토리지 사용량을 절약할 수 있습니다.

</details>

---

## 질문 2

**Dockerfile에서 작업 디렉토리를 설정하는 옵션은 무엇인가요?**

A) --mount  
B) -w  
C) -v  
D) --workdir  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  
**-w**는 Dockerfile에서 작업 디렉토리를 설정하는 옵션입니다. 이는 컨테이너 내에서 파일을 처리할 때 기준으로 사용하는 경로를 정의하는 역할을 합니다. 예를 들어, `-w /app`는 `/app` 디렉토리를 작업 디렉토리로 설정하는 뜻입니다.  
**WORKDIR** 설정은 파일 경로를 통일화하는 데 도움을 줍니다. 예를 들어, `COPY . /app` 명령어로 파일을 복사할 때 `/app` 경로를 기준으로 파일을 위치시키면, 경로 오류를 줄일 수 있습니다.  
**오답 이유**:  
- A) --mount는 볼륨 마운트를 위한 옵션입니다.  
- C) -v는 볼륨 마운트를 위한 옵션입니다.  
- D) --workdir는 Docker Compose에서 사용하는 옵션입니다.  
**최적화 이유**: 작업 디렉토리 설정은 파일 경로 관리에 도움을 주고, Dockerfile의 가독성을 높이는 데 기여합니다.

</details>

---

## 질문 3

**Node.js 개발 서버를 실행하기 위한 Docker 명령어는 무엇인가요?**

A) npm start  
B) sh -c "npm install && npm run dev"  
C) docker run  
D) docker build  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  
**npm install && npm run dev**는 Node.js 애플리케이션을 실행하기 위한 명령어입니다.  
- `npm install`은 프로젝트에 필요한 패키지를 설치합니다.  
- `npm run dev`는 `package.json`에 정의된 `dev` 스크립트를 실행합니다. 이 스크립트는 일반적으로 `nodemon`을 사용해 개발 서버를 실행합니다.  
**nodemon**은 개발 중 코드 변경 시 자동으로 서버를 재시작하는 도구로, 실시간으로 코드 변경을 반영할 수 있습니다.  
**오답 이유**:  
- A) npm start는 `package.json`에 정의된 `start` 스크립트를 실행하지만, 개발 환경에서는 `dev` 스크립트가 더 적합합니다.  
- C) docker run은 이미지 실행을 위한 명령어입니다.  
- D) docker build는 이미지 생성을 위한 명령어입니다.  
**최적화 이유**: `npm install`과 `npm run dev`를 함께 실행하면 개발 환경에서 필요한 의존성을 설치하고, 즉시 개발 서버를 시작할 수 있어 효율성을 높입니다.

</details>

---

## 질문 4

**Docker Compose에서 파일 변경 시 컨테이너를 재빌드해야 하는 경우 어떤 작업 방식을 사용해야 하나요?**

A) sync  
B) sync+restart  
C) watch  
D) rebuild  

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  
**sync+restart**는 Docker Compose에서 파일 변경 시 컨테이너를 재빌드하고 재시작하는 방식입니다.  
- **sync**는 파일 변경을 감지해 컨테이너를 재빌드하지만, 컨테이너를 재시작하지 않습니다.  
- **sync+restart**는 파일 변경 시 컨테이너를 재빌드하고, 기존 컨테이너를 종료한 후 새 컨테이너를 실행합니다.  
예를 들어, `package.json` 파일을 변경하면 `sync+restart`는 이미지 재빌드 후 컨테이너를 재시작해 변경 사항을 반영합니다.  
**오답 이유**:  
- A) sync는 파일 변경 시 재빌드만 수행합니다.  
- C) watch는 파일 변경을 감지하지만, 컨테이너 재시작 기능이 없습니다.  
- D) rebuild는 명시적으로 이미지를 재빌드하는 명령어입니다.  
**최적화 이유**: `sync+restart`는 개발 중 파일 변경을 즉시 반영할 수 있어 개발 생산성을 높이고, 실시간으로 문제가 발생할 수 있는 요소를 조기에 검증할 수 있습니다.

</details>