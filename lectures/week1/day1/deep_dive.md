# 📘 Week 1 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="service_understanding.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 📚 서비스 이해</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="handson_step1.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: 🛠️ Hands-on Lab - Step 1 ➡️</a>
</div>

---

# Deep Dive - 트러블슈팅

## 🔍 시나리오 1: CI/CD 파이프라인 실패

### 💬 개념 설명
CI/CD는 "코드 변경사항을 자동으로 테스트하고 배포하는 프로세스"입니다.  
예를 들어, 코드를 수정하면 자동으로 테스트 환경에서 실행되고, 문제가 없으면 실제 서버에 배포됩니다.  
환경 변수는 "애플리케이션 실행 시 필요한 비밀번호, URL 등 정보를 안전하게 저장하는 방법"입니다.  
레지스트리는 "컨테이너 이미지를 저장하고 관리하는 저장소"로, Docker 이미지를 공유하는 역할을 합니다.

### 트러블슈팅 흐름도  
[이미지 보기](https://docs.example.com/image1.png)

### 🔍 시나리오 설명
GitHub Actions 파이프라인이 예상치 못한 오류로 중단됨  
예: DB 비밀번호가 설정되지 않으면 파이프라인은 중단됩니다.

### 🔬 원인 분석
환경 변수 누락 또는 설정 파일 오류로 인한 파이프라인 실행 중단  
예: `DB_PASSWORD` 변수가 설정되지 않으면 데이터베이스 연결이 실패합니다.

### 🔎 원인 확인 방법
1. GitHub Actions 워크플로우 로그 확인:  
   - GitHub 워크플로우 로그를 확인하기 위해 다음 단계를 수행하세요.  
     - 워크플로우 실행 내역을 클릭하여 로그를 확인합니다.  
2. 환경 변수 존재 여부 확인:  
   - `echo $DB_PASSWORD` 명령어를 실행해 변수가 설정되었는지 확인합니다.  
3. 설정 파일 문법 검사:  
   - `yml-lint .github/workflows/<workflow-name>.yml` 명령어로 파일 문법을 점검합니다.  
4. 컨테이너 이미지 빌드 로그 확인:  
   - 컨테이너 로그를 확인하려면 Docker UI에서 해당 컨테이너를 선택하고 로그를 클릭하세요.

### 🔧 수정 방법
1. 필요한 환경 변수 설정:  
   - `export DB_PASSWORD=your_password` 명령어로 변수를 설정합니다.  
2. 워크플로크 파일 수정 후 재저장:  
   - 파일을 수정한 후 `git add` 명령어로 변경사항을 저장합니다.  
3. 파이프라인 재실행:  
   - GitHub 워크플로우 실행을 다시 시작해 파이프라인을 재시도합니다.  
4. Docker 이미지 재빌드:  
   - Docker UI에서 이미지를 다시 빌드하거나 `docker build` 명령어를 사용합니다.

### ✔️ 정상 확인 방법
1. 파이프라인 완료 상태 확인:  
   - GitHub 워크플로우 목록에서 실행 완료 상태를 확인합니다.  
2. 빌드된 이미지 검증:  
   - Docker UI에서 이미지 목록을 확인해 빌드된 이미지가 있는지 확인합니다.  
3. 최종 빌드 아트ifacts 존재 여부 확인:  
   - `target/` 폴더에 생성된 파일이 있는지 확인합니다.

---

## 🔍 시나리오 2: 컨테이너 레지스트리 연결 실패

### 💬 개념 설명
레지스트리는 "컨테이너 이미지를 저장하고 관리하는 저장소"입니다.  
예: Docker Hub는 대표적인 레지스트리로, 개발자가 만든 Docker 이미지를 공유하는 장소입니다.

### 트러블슈팅 흐름도  
[이미지 보기](https://docs.example.com/image1.png)

### 🔍 시나리오 설명
Docker 이미지 푸시 시 'denied: unauthorized' 오류 발생  
예: 사용자가 Docker Hub에 이미지 업로드 시 인증이 실패하는 경우.

### 🔬 원인 분석
레지스트리 인증 정보 누락 또는 잘못된 토큰 사용  
예: 토큰이 만료되었거나, 잘못된 사용자 이름/패스워드를 입력한 경우.

### 🔎 원인 확인 방법
1. Docker 로그 확인:  
   - 컨테이너 로그를 확인하려면 Docker UI에서 해당 컨테이너를 선택하고 로그를 클릭하세요.  
2. 인증 정보 존재 여부 확인:  
   - `~/.docker/config.json` 파일을 열어 인증 정보가 저장되었는지 확인합니다.  
3. 레지스트리 토큰 유효성 검사:  
   - `curl -u <username>:<token> <registry-url>/v2/` 명령어로 토큰이 유효한지 확인합니다.  
4. 레지스트리 네트워크 연결 확인:  
   - Docker UI에서 레지스트리 연결 상태를 확인합니다.

### 🔧 수정 방법
1. 신규 토큰 생성 및 설정:  
   - `docker login --username <username> --password-stdin` 명령어로 인증 정보를 설정합니다.  
2. config.json 파일 수정:  
   - `nano ~/.docker/config.json` 명령어로 파일을 열고 인증 정보를 수정합니다.  
3. 레지스트리 인증 정보 재등록:  
   - `docker logout && docker login` 명령어로 인증 정보를 재등록합니다.  
4. 이미지 푸시 재시도:  
   - `docker push <repository>:<tag>` 명령어로 이미지를 다시 업로드합니다.

### ✔️ 정상 확인 방법
1. 레지스트리 인증 성공 여부 확인:  
   - `curl -u <username>:<token> <registry-url>/v2/` 명령어로 인증이 성공했는지 확인합니다.  
2. 이미지 목록 확인:  
   - Docker UI에서 이미지 목록을 확인해 빌드된 이미지가 있는지 확인합니다.  
3. 레지스트리에 이미지 존재 여부 확인:  
   - `curl -u <username>:<token> <registry-url>/v2/<repository>/tags/list` 명령어로 레지스트리에 이미지가 등록되었는지 확인합니다.

---

## 사전 지식 요구사항
이 강의는 다음 사전 지식이 필요합니다:  
1. Docker 설치 및 기본 사용법  
2. GitHub Actions 기초 지식  
3. 터미널 또는 CLI 사용 경험  
4. 기본적인 Linux 명령어 이해 (예: `ls`, `cd`, `mkdir`)  

## 참고 자료
- [Docker 공식 문서](https://docs.docker.com/)  
- [GitHub Actions 가이드](https://docs.github.com/en/actions)  
- [CI/CD 개념 정리](https://devops.com/ci-cd/)



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 1 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 1 | 🎯 DevOps 6개월 교육과정</p>
</div>
