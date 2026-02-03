# 📘 Week 2 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="service_understanding.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 📚 서비스 이해</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="handson_step1.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: 🛠️ Hands-on Lab - Step 1 ➡️</a>
</div>

---

# Deep Dive - 트러블슈팅

## 🔍 시나리오 1: npm install 실패 시나리오

### 트러블슈팅 흐름도

```mermaid
flowchart TD
  Node_Start[실행 시작] --> CheckWorkdir{WORKDIR 설정 확인?}
  CheckWorkdir -->|아니요| CheckPermissions{package.json 접근 권한 확인?}
  CheckPermissions -->|실패| AdjustMounts[--mount type=bind 추가]
  CheckPermissions -->|성공| SetWorkdir[WORKDIR /app 설정]
  SetWorkdir --> RunCommand{npm install 실행}
  RunCommand -->|성공| VerifyFix[애플리케이션 실행]
  RunCommand -->|실패| Error[권한 문제 발생]
  style Node_Start fill:#667eea,color:#fff
  style Error fill:#ff6b6b,color:#fff
  style CheckWorkdir fill:#ffd43b,color:#000
  style CheckPermissions fill:#ffd43b,color:#000
  style AdjustMounts fill:#51cf66,color:#000
  style SetWorkdir fill:#51cf66,color:#000
  style VerifyFix fill:#51cf66,color:#000

```

### 🔍 시나리오 설명

Docker 컨테이너가 실행 시 npm install이 실패하고 애플리케이션이 시작되지 않는 문제

### 🔬 원인 분석

WORKDIR 설정 누락 또는 권한 문제로 package.json이 실행 디렉토리에서 접근 불가

### 🔎 원인 확인 방법

docker logs <container-id> 명령어로 컨테이너 로그 확인

docker inspect <container-id> | grep -i workingdir 명령어로 WORKDIR 설정 확인

docker exec -it <container-id> ls -l /app 명령어로 디렉토리 권한 점검

### 🔧 수정 방법

Dockerfile에 WORKDIR /app 추가: WORKDIR /app

COPY --chown=node:node package.json . 명령어로 권한 설정

docker build --no-cache -t myapp . 명령어로 이미지 재빌드

### ✔️ 정상 확인 방법

docker run -d --name myapp myapp 명령어로 컨테이너 실행

docker logs -f myapp 명령어로 npm install 로그 확인

npm install --dry-run 명령어로 로컬 환경에서 설치 가능성 검증

---

## 🔍 시나리오 2: watch 모드 동기화 실패 시나리오

### 트러블슈팅 흐름도

```mermaid
flowchart TD
  Node_Start[시작] --> CheckPath{경로 매핑 정확?}
  CheckPath -->|정확| VerifyBinaries[필요한 bin 파일 존재?]
  CheckPath -->|불확실| FixPath[경로 수정]
  VerifyBinaries -->|존재| CheckPermissions[권한 설정 확인]
  VerifyBinaries -->|누락| AddBinaries[bin 파일 추가]
  CheckPermissions -->|적절| WatchEnabled[watch 모드 활성화]
  CheckPermissions -->|불적절| FixPermissions[권한 수정]
  WatchEnabled -->|성공| Success[업데이트 성공]
  style Node_Start fill:#667eea,color:#fff
  style Success fill:#51cf66,color:#fff

```

### 🔍 시나리오 설명

Docker Compose의 watch 모드가 파일 변경을 감지하지 못해 애플리케이션 업데이트가 이루어지지 않는 문제

### 🔬 원인 분석

watch 블록의 경로 매핑 오류 또는 필요한 bin 파일 누락

### 🔎 원인 확인 방법

docker-compose config 명령어로 서비스 정의 검증

docker inspect <container-id> | grep -i mountpoint 명령어로 마운트 포인트 확인

docker exec -it <container-id> which stat 명령어로 stat 실행 파일 존재 여부 확인

### 🔧 수정 방법

docker-compose.yml에서 watch 블록 수정: 
  watch:
    - action: sync
      path: ./web
      target: /app/web
    - action: sync+restart
      path: ./proxy/nginx.conf
      target: /etc/nginx/conf.d/default.conf

RUN apk add --no-cache coreutils 명령어로 stat/mkdir/rmdir 설치

docker-compose up --build 명령어로 구성 재빌드

### ✔️ 정상 확인 방법

docker-compose exec web touch /app/web/test.txt 명령어로 파일 생성 테스트

docker-compose logs -f web 명령어로 동기화 로그 확인

docker-compose exec web ls -l /app/web 명령어로 마운트 상태 검증



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 2 - Day 1 학습 완료!</h3>
  <p style="margin: 0; opacity: 0.9;">다음 단계로 계속 진행하세요</p>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;">
  <a href="service_understanding.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">⬅️ 이전<br/><span style="font-size: 12px; opacity: 0.8;">📚 서비스 이해</span></a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;">🏠<br/><span style="font-size: 12px;">목차로</span></a>
  <a href="handson_step1.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">다음 ➡️<br/><span style="font-size: 12px; opacity: 0.8;">🛠️ Hands-on Lab - Step 1</span></a>
</div>

---

<div style="text-align: center; padding: 10px; color: #666; font-size: 12px;">
  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>
  <p style="margin-top: 5px;">📅 Week 2 Day 1 | 🎯 DevOps 6개월 교육과정</p>
</div>
