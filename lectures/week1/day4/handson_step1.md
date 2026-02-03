# Hands-on Lab - Step 1

## 실습 개요

**제목**: Docker Containers 실습: 실시간 개발 환경 구성

**목적**: Docker를 사용해 실시간 코드 변경을 지원하는 개발 환경을 구축하고, 컨테이너 관리 기법을 익히는 실습

**학습 목표**:
- Dockerfile 작성 및 이미지 빌드
- bind mount를 통한 실시간 코드 동기화
- nodemon을 사용한 개발 서버 실행
- Docker 로그 모니터링 방법
- 컨테이너 포트 매핑 및 접근 테스트
- Docker Compose를 통한 서비스 관리
- 환경 변수 및 비밀 정보 처리

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

```mermaid
graph TD
  A[DOCKER CONTAINERS 실습 시작] --> B[단계1: Dockerfile 작성]
  B --> C[단계2: Docker 이미지 빌드]
  C --> D[단계3: 컨테이너 실행 및 로그 모니터링]
  D --> E[단계4: 코드 수정 및 실시간 동기화 테스트]
  E --> F[단계5: 포트 접근 테스트]
  F --> G[단계6: Docker Compose로 서비스 관리]
  G --> H[단계7: 환경 변수 및 비밀 정보 처리]
  H --> I[실습 완료]
  style A fill:#4CAF50,stroke:#388E3C
  style I fill:#FF9800,stroke:#FFA726
  classDef dockerCommand fill:#2196F3,stroke:#0D47A1
  classDef bindMount fill:#FFA726,stroke:#FFB74D
  classDef portMapping fill:#9C27B0,stroke:#673AB7
  class B,C,D,E,F,G,H dockerCommand
  class --mount type=bind,src=.,target=/app bindMount
  class --publish 8080:80 portMapping
```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/docker-bind-mount.png)
- [이미지 보기](https://docs.example.com/docker-port-mapping.png)
- [이미지 보기](https://docs.example.com/docker-compose-watch.png)


## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker Desktop 설치 및 실행 중인 환경
- node.js 및 npm 설치
- 프로젝트 디렉토리에서 package.json 파일 존재

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

프로젝트 폴더 생성: mkdir myapp && cd myapp

package.json 생성: npm init -y

nodemon 설치: npm install --save-dev nodemon

src/index.js 파일 생성: echo 'console.log("Hello Docker!");' > src/index.js

</details>

---

## Step 1: Dockerfile 작성

**목표**: node:24-alpine 기반 Dockerfile 작성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
FROM node:24-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
EXPOSE 3000
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

- 문제: Dockerfile 문법 오류 -> 해결: docker build --no-cache 명령어 사용
- 문제: 경로 오류 -> 해결: pwd 명령어로 현재 경로 확인

</details>

