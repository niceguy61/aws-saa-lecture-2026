# Hands-on Lab - Step 1

## 실습 개요

**제목**: Dockerfile 및 Docker Compose 실습

**목적**: Dockerfile을 사용해 Node.js 애플리케이션을 패키징하고, Docker Compose를 활용한 실시간 파일 동기화 환경을 구축하는 실습

**학습 목표**:
- Dockerfile 작성 방법 익히기
- bind mount를 통한 호스트-컨테이너 파일 동기화 설정
- Docker Compose watch 모드 사용법 이해
- npm 개발 서버와 nodemon 통합 테스트
- 시크릿 마운트 및 SSH 마운트 구성
- 로그 확인 및 실시간 재구성 테스트
- SELinux 옵션 적용 및 보안 검증

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

```mermaid
flowchart TD
  start[시작] --> Step1[단계 1: Dockerfile 작성]
  Step1 --> Step2[단계 2: Docker Compose 구성]
  Step2 --> Step3[단계 3: 시크릿 마운트 설정]
  Step3 --> Step4[단계 4: 컨테이너 실행 및 로그 확인]
  Step4 --> Step5[단계 5: 실시간 파일 동기화 테스트]
  Step5 --> Step6[단계 6: SELinux 옵션 적용]
  Step6 --> Step7[단계 7: 환경 정리 및 검증]
  Step7 --> end[완료]
  style start fill:#4CAF50,stroke:#388E3C
  style end fill:#F44336,stroke:#D32F2F
  style Step1 fill:#2196F3,stroke:#1976D2
  style Step2 fill:#9C27B0,stroke:#8E24AA
  style Step3 fill:#FF9800,stroke:#FB8C00
  style Step4 fill:#795548,stroke:#6D4C41
  style Step5 fill:#FF5722,stroke:#E64A19
  style Step6 fill:#00BCD4,stroke:#0097A7
  style Step7 fill:#607D8B,stroke:#4A5568
```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/dockerfile-structure.png)
- [이미지 보기](https://docs.example.com/secret-mount-setup.png)
- [이미지 보기](https://docs.example.com/ssh-mount-example.png)
- [이미지 보기](https://docs.example.com/watch-mode-diagram.png)


## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker Desktop 설치 및 실행 중인 환경
- Node.js 18 이상 및 npm 설치
- 프로젝트 디렉토리 구조 준비 (src/web, package.json 등)
- AWS 클레어런스 또는 SSH 키 파일 준비

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

프로젝트 디렉토리 생성: `mkdir myapp && cd myapp`

src/web 디렉토리 및 package.json 파일 생성

docker-compose.yml 파일 생성

AWS 시크릿 파일 또는 SSH 키 준비 (필요 시)

</details>

---

## Step 1: Dockerfile 작성

**목표**: Node.js 애플리케이션용 Dockerfile 생성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# node:24-alpine 기반 이미지 사용
FROM node:24-alpine

# 작업 디렉토리 설정
WORKDIR /app

# 호스트 디렉토리와 컨테이너 디렉토리 바인드 마운트
VOLUME ["/app"]

# npm 설치 및 개발 서버 실행 명령어 설정
CMD ["sh", "-c", "npm install && npm run dev"]
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Dockerfile 파일 생성 완료
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
ls -l Dockerfile
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 'node:24-alpine' 이미지 없을 때: `docker pull node:24-alpine` 실행
- 문제: WORKDIR 경로 오류 시: `WORKDIR /app`으로 수정

</details>

