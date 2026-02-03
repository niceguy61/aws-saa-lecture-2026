# Hands-on Lab - Step 1

## 실습 개요

**제목**: DevOps 실습: Docker와 AWS CLI로 간단한 웹 애플리케이션 배포

**목적**: Docker를 사용한 애플리케이션 패키징과 AWS CLI를 활용한 클라우드 배포 프로세스를 실습합니다.

**학습 목표**:
- Docker 컨테이너화 기초 이해
- AWS CLI를 통한 리소스 관리 방법 습득
- CI/CD 파이프라인 기본 흐름 경험

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

`mermaid
flowchart TD
  Step1[프로젝트 디렉토리 생성] --> Step2[DOCKERFILE 작성]
  Step2 --> Step3[DOCKER 이미지 빌드]
  Step3 --> Step4[컨테이너 실행]
  Step4 --> Step5[애플리케이션 테스트]
  Step5 --> Step6[ECR 리포지토리 생성]
  Step6 --> Step7[이미지 태그 및 업로드]
  style Step1 fill:#667eea,color:#fff
  style Step2 fill:#667eea,color:#fff
  style Step3 fill:#667eea,color:#fff
  style Step4 fill:#667eea,color:#fff
  style Step5 fill:#667eea,color:#fff
  style Step6 fill:#667eea,color:#fff
  style Step7 fill:#667eea,color:#fff
  caption DevOps 실습: Docker와 AWS CLI로 간단한 웹 애플리케이션 배포
```


## 사전 요구사항

<details>
<summary>사전 요구사항 보기</summary>

- Docker Desktop 24.0+ 설치
  - 설치 가이드: https://docs.docker.com/desktop/install/
- AWS CLI 구성
  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
- 기본 명령어 이해 (공식 문서: https://docs.docker.com/engine/reference/commandline/docker/)

</details>

## 환경 설정

<details>
<summary>환경 설정 보기</summary>

Docker Desktop 실행 및 호스트 통신 설정
  - 공식 가이드: https://docs.docker.com/desktop/initial-setup/

AWS CLI 구성 검증
  - 명령어: aws configure list

</details>

---

## Step 1: 프로젝트 디렉토리 생성

**목표**: 워크스페이스 구조 생성

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
mkdir devops-practice && cd devops-practice
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
디렉토리 생성 완료 및 진입
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
pwd && ls
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 디렉토리 생성 실패 → sudo 권한 필요
- 문제: 경로 접근 거부 → 파일 시스템 권한 확인

</details>

