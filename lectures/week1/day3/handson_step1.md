# Hands-on Lab - Step 1

## 실습 개요

**제목**: Docker 이미지 및 실시간 개발 환경 구성

**목적**: Docker 이미지를 생성하고 실시간 코드 변경을 지원하는 개발 환경을 구축하는 실습

**학습 목표**:
- Dockerfile 작성 및 이미지 빌드
- bind mount를 통한 실시간 코드 동기화 설정
- docker-compose watch 모드 적용 방법 이해

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

`mermaid
flowchart TD
  ST[시작] --> S1[단계1: Dockerfile 구성]
  S1 --> S2[단계2: 이미지 빌드]
  S2 --> S3[단계3: 컨테이너 실행]
  S3 --> S4[단계4: 로그 확인]
  S4 --> S5[단계5: 실시간 동기화 테스트]
  S5 --> S6[단계6: docker-compose watch 설정]
  S6 --> S7[단계7: watch 모드 테스트]
  S7 --> EN[완료]

  style ST fill:#4CAF50,stroke:#388E3C
  style EN fill:#4CAF50,stroke:#388E3C
  style S1 fill:#FF9800,stroke:#FFA726
  style S2 fill:#FF9800,stroke:#FFA726
  style S3 fill:#FF9800,stroke:#FFA726
  style S4 fill:#FF9800,stroke:#FFA726
  style S5 fill:#FF9800,stroke:#FFA300
  style S6 fill:#FF9800,stroke:#FFA300
  style S7 fill:#FF9800,stroke:#FFA300
`

**참고 이미지**:
- [이미지 보기](https://docs.example.com/docker-compose-watch.png)
- [이미지 보기](https://docs.example.com/bind-mount-example.png)


## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker 및 Docker Compose 설치 확인
- Node.js 프로젝트 구조 보유
- Dockerfile 파일 생성

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

프로젝트 디렉토리로 이동: cd myproject

package.json 파일에 dev 스크립트 정의 확인

docker-compose.yml 파일 생성

</details>

---

## Step 1: Dockerfile 구성

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

- 문제: npm install 오류 → 'npm install --force'로 패키지 재설치
- 문제: 경로 오류 → 'WORKDIR' 경로 재확인

</details>

