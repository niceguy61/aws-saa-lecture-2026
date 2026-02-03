# Hands-on Lab - Step 1

## 실습 개요

**제목**: Docker 실습: Node.js 애플리케이션 배포

**목적**: Docker를 사용하여 Node.js 애플리케이션을 패키징하고 실시간 개발 환경을 구성하는 방법을 학습합니다.

**학습 목표**:
- Dockerfile 작성 및 이미지 빌드
- Container 실행 및 포트 매핑 설정
- 바인드 마운트를 통한 실시간 코드 변경 감지
- docker-compose를 활용한 개발 서버 구동
- 로그 확인 및 디버깅 방법 습득

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

`mermaid
graph TD
  A[시작] --> B[단계1: Dockerfile 작성]
  B --> C[단계2: 이미지 빌드]
  C --> D[단계3: 컨테이너 실행]
  D --> E[단계4: 로그 확인]
  E --> F[단계5: 코드 변경 감지]
  F --> G[단계6: 이미지 재빌드]
  G --> H[단계7: 정리 작업]
  H --> I[완료]
  style A fill:#4CAF50,stroke:#4CAF50
  style I fill:#F44336,stroke:#F44336
  classDef step fill:#2196F3,stroke:#2196F3
  class B,C,D,E,F,G,H class step


**참고 이미지**:
- [이미지 보기](https://docs.example.com/dockerfile-syntax.png)
- [이미지 보기](https://docs.example.com/sync-restart-pattern.png)


## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker Desktop 설치 완료
- Node.js 프로젝트 소스 코드 준비
- docker-compose.yml 파일 생성

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

프로젝트 루트 디렉토리에 Dockerfile 생성

docker-compose.yml 파일에 서비스 정의 작성

package.json 파일에 dev 스크립트 확인

</details>

---

## Step 1: Dockerfile 작성

**목표**: Node.js 애플리케이션을 실행할 Docker 이미지 구조 정의

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
#!/bin/sh
FROM node:24-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
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

- 문제: npm install 실패 → 'npm install --force'로 강제 reinstall
- 문제: 경로 오류 → 'WORKDIR' 경로 재확인

</details>

