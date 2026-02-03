# 📘 Week 2 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="deep_dive.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🔍 Deep Dive</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="handson_step2.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: 🛠️ Hands-on Lab - Step 2 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 1

## 🎯 실습 개요

**제목**: Dockerfile 및 실시간 파일 동기화 환경 구성 실습

**목적**: Docker 컨테이너에서 실시간 파일 동기화와 개발 환경을 설정하여 애플리케이션을 실행하는 방법을 학습합니다.

**학습 목표**:
- Dockerfile 구조 이해
- bind mount 및 watch 모드 사용법 익히기
- AWS Secret 환경 변수 설정 방법 배우기
- Docker Compose로 실시간 동기화 환경 구축

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

```mermaid
flowchart TD
  Step1[프로젝트 디렉토리 생성] --> Step2[Dockerfile 작성]
  Step2 --> Step3[docker-compose.yml 작성]
  Step3 --> Step4[AWS Secret 환경 변수 설정]
  Step4 --> Step5[Docker 이미지 빌드]
  Step5 --> Step6[컨테이너 실행]
  Step6 --> Step7[로그 확인 및 테스트]
  classDef primary fill:#667eea,color:#fff,stroke:#764ba2
  class Step1,Step2,Step3,Step4,Step5,Step6,Step7 primary
  caption Dockerfile 및 실시간 파일 동기화 환경 구성 실습 절차

```

## 📋 사전 요구사항

- Docker Desktop 24.0+ 설치
  - 설치 가이드: https://docs.docker.com/desktop/install/
- AWS CLI 구성
  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
- Docker 기초 지식
  - 공식 문서: https://docs.docker.com/get-started/

## ⚙️ 환경 설정

Docker Desktop 설치 및 실행
  - 공식 가이드: https://docs.docker.com/get-started/

AWS CLI 구성 및 테스트
  - aws --version 확인

---

## 👉 Step 1: 프로젝트 디렉토리 생성

**목표**: 작업 디렉토리 구조를 생성합니다.

**명령어**:

```bash
mkdir myapp && cd myapp

```

**예상 출력**:

```

myapp 디렉토리 생성 및 이동 완료

```

**확인 방법**:

```bash
ls -la

```

**문제 해결**:
- 문제: 디렉토리 생성 실패 → 권한 문제 확인: sudo mkdir myapp
- 문제: 경로 접근 불가 → 현재 작업 디렉토리 확인: pwd



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 2 - Day 1 학습 완료!</h3>
  <p style="margin: 0; opacity: 0.9;">다음 단계로 계속 진행하세요</p>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;">
  <a href="deep_dive.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">⬅️ 이전<br/><span style="font-size: 12px; opacity: 0.8;">🔍 Deep Dive</span></a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;">🏠<br/><span style="font-size: 12px;">목차로</span></a>
  <a href="handson_step2.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">다음 ➡️<br/><span style="font-size: 12px; opacity: 0.8;">🛠️ Hands-on Lab - Step 2</span></a>
</div>

---

<div style="text-align: center; padding: 10px; color: #666; font-size: 12px;">
  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>
  <p style="margin-top: 5px;">📅 Week 2 Day 1 | 🎯 DevOps 6개월 교육과정</p>
</div>
