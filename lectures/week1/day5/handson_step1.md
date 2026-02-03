# 📘 Week 1 - Day 5

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="deep_dive.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🔍 Deep Dive</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="handson_step2.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: 🛠️ Hands-on Lab - Step 2 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 1

## 🎯 실습 개요

**제목**: Docker Networking with Bind Mounts and Port Mapping

**목적**: Docker 컨테이너에 네트워킹 기능을 설정하고, 포트 매핑 및 바인드 마운트를 통해 개발 환경을 구성하는 실습

**학습 목표**:
- Dockerfile에서 바인드 마운트 설정 방법 학습
- 포트 매핑을 통한 외부 접근 설정
- 실시간 코드 변경을 통한 개발 서버 동기화
- Docker 네트워크 구성 검증

**예상 소요 시간**: 45분

**난이도**: Beginner

### 실습 흐름도

```mermaid
graph TD
  Start[시작] --> Step1[단계1: 프로젝트 디렉토리 생성]
  Step1 --> Step2[단계2: Dockerfile 작성]
  Step2 --> Step3[단계3: package.json 생성]
  Step3 --> Step4[단계4: Docker 이미지 빌드]
  Step4 --> Step5[단계5: 컨테이너 실행]
  Step5 --> Step6[단계6: 로그 확인]
  Step6 --> Step7[단계7: 애플리케이션 테스트]
  Step7 --> End[완료]

```

**참고 이미지**:
- [이미지 보기](https://docs.example.com/docker-networking-1.png)
- [이미지 보기](https://docs.example.com/bind-mounts-2.png)
- [이미지 보기](https://docs.example.com/port-mapping-3.png)

## 📋 사전 요구사항

- Docker Desktop 24.0+ 설치
  - 설치 가이드: https://docs.docker.com/desktop/install/
- AWS CLI 구성
  - 설치: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  - 설정: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
- 기본 Docker 지식
  - 공식 문서: https://docs.docker.com/get-started/

## ⚙️ 환경 설정

Docker Desktop 설치 및 실행
  - 공식 가이드: https://docs.docker.com/get-started/

AWS CLI 설치 및 구성
  - 설정 문서: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

---

## 👉 Step 1: 프로젝트 디렉토리 생성

**목표**: 워크스페이스 디렉토리 생성

**명령어**:

```bash
mkdir my-docker-app && cd my-docker-app

```

**예상 출력**:

```

현재 디렉토리가 my-docker-app로 변경됨

```

**확인 방법**:

```bash
pwd

```

**문제 해결**:
- 문제: 디렉토리 생성 실패 → sudo 권한으로 재시도: sudo mkdir my-docker-app



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 5 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 5 | 🎯 DevOps 6개월 교육과정</p>
</div>
