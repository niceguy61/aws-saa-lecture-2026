# 📘 Week 1 - Day 2

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="deep_dive.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🔍 Deep Dive</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="handson_step2.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: 🛠️ Hands-on Lab - Step 2 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 1

## 🎯 실습 개요

**제목**: Docker 실습: 개발 환경 구성

**목적**: Node.js 애플리케이션을 Docker 컨테이너로 실행하고 실시간 코드 변경을 통한 개발 환경을 설정합니다

**학습 목표**:
- Dockerfile 작성
- bind mount을 사용한 실시간 코드 동기화
- nodemon을 통한 개발 서버 실행
- Docker 로그 확인 방법 이해

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

```mermaid
graph TD
  A[시작] --> B[단계1: 프로젝트 디렉토리 생성]
  B --> C[단계2: package.json 생성]
  C --> D[단계3: Dockerfile 작성]
  D --> E[단계4: 이미지 빌드]
  E --> F[단계5: 컨테이너 실행]
  F --> G[단계6: 애플리케이션 테스트]
  G --> H[단계7: 로그 모니터링]
  H --> I[완료]

```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/docker-command-example.png)
- [이미지 보기](https://docs.example.com/sync-restart-example.png)
- [이미지 보기](https://docs.example.com/bind-mount-diagram.png)

## 📋 사전 요구사항

- Docker Desktop 24.0+ 설치
  - 설치 가이드: https://docs.docker.com/desktop/install/
- AWS CLI 구성
  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
- Node.js 기본 지식
  - 공식 문서: https://nodejs.org/en/docs/

## ⚙️ 환경 설정

Docker Desktop 설치 및 구성
  - 설정 가이드: https://docs.docker.com/desktop/get-started/

AWS CLI 구성
  - 설정 가이드: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

---

## 👉 Step 1: 프로젝트 디렉토리 생성

**목표**: 작업 디렉토리 생성

**명령어**:

```bash
mkdir myapp && cd myapp

```

**예상 출력**:

```

myapp 디렉토리 생성됨

```

**확인 방법**:

```bash
ls

```

**문제 해결**:
- 문제: 디렉토리 생성 실패
  해결: sudo 권한으로 다시 시도



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 2 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 2 | 🎯 DevOps 6개월 교육과정</p>
</div>
