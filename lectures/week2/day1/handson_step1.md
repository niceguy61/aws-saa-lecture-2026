# 📘 Week 2 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="deep_dive.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🔍 Deep Dive</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="handson_step2.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: 🛠️ Hands-on Lab - Step 2 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 1

## 🎯 실습 개요

**제목**: Dockerfile 및 실시간 파일 동기화 설정 실습

**목적**: Dockerfile을 통해 Node.js 애플리케이션을 배포하고, 실시간 파일 동기화 및 비밀 변수 마운트 기능을 구현하는 실습

**학습 목표**:
- Dockerfile 작성하여 Node.js 환경 설정
- bind mount을 사용한 실시간 파일 동기화 구현
- 비밀 변수를 환경 변수 및 파일로 동시에 마운트
- Docker Compose로 서비스 실행 및 로그 확인

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

```mermaid
graph TD
  Start[시작] --> Step1[단계1: 프로젝트 디렉토리 생성]
  Step1 --> Step2[단계2: Dockerfile 작성]
  Step2 --> Step3[단계3: package.json 생성]
  Step3 --> Step4[단계4: src 디렉토리 및 인덱스 파일 생성]
  Step4 --> Step5[단계5: Docker 이미지 빌드]
  Step5 --> Step6[단계6: 컨테이너 실행 및 로그 확인]
  Step6 --> Step7[단계7: 실시간 파일 동기화 설정]
  Step7 --> End[완료]

```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/image1.png)
- [이미지 보기](https://docs.example.com/image2.png)
- [이미지 보기](https://docs.example.com/image3.png)

## 📋 사전 요구사항

- Docker Desktop 24.0+ 설치
  - 설치 가이드: https://docs.docker.com/desktop/install/
- AWS CLI 구성
  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
- Docker Compose 기본 지식
  - 공식 문서: https://docs.docker.com/compose/

## ⚙️ 환경 설정

Docker Desktop 실행 및 가상화 기능 활성화
  - 설정 가이드: https://docs.docker.com/desktop/configure/

AWS CLI 환경 변수 설정
  - 설정 방법: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

---

## 👉 Step 1: 프로젝트 디렉토리 생성

**목표**: 작업 디렉토리 생성

**명령어**:

```bash
mkdir myapp && cd myapp

```

**예상 출력**:

```

myapp 디렉토리 생성 및 진입

```

**확인 방법**:

```bash
ls

```

**문제 해결**:
- 문제: 디렉토리 생성 실패 → 'mkdir' 명령어 권한 문제 확인
- 문제: 경로 접근 거부 → 'chmod'로 디렉토리 권한 변경



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
