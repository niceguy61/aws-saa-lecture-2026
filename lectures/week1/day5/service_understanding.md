# 서비스 이해 (Service Understanding)

## 1. 배경 정보

Docker 네트워킹은 컨테이너 간 통신과 호스트(컴퓨터)와의 연결을 관리하는 기능입니다. 예를 들어, 웹 애플리케이션을 개발할 때 서버와 클라이언트가 서로 데이터를 주고받는 방식을 설정하는 것이죠.  
**포트 매핑**은 호스트 컴퓨터의 포트(예: 8080)와 컨테이너의 포트(예: 3000)를 연결해 외부에서 애플리케이션에 접근할 수 있도록 도와요.  
**바인드 마운트**는 호스트 컴퓨터의 파일 폴더를 컨테이너에 연결해 실시간으로 파일을 동기화하는 기능입니다.  
**Docker Compose**는 여러 컨테이너를 하나의 파일로 관리해 복잡한 네트워크 설정을 쉽게 만듭니다.  

### 단계별 설명  
1. **포트 매핑 설정**: 호스트 포트(예: 80)를 컨테이너 포트(예: 8080)로 연결  
   - 예: `ports: - "80:8080"`  
2. **바인드 마운트 구성**: 호스트 파일 폴더를 컨테이너에 연결  
   - 예: `volumes: - ./app:/app`  
3. **작업 디렉토리 설정**: 컨테이너가 실행될 기본 폴더 지정  
4. **Docker Compose 통합**: `docker-compose.yml` 파일로 설정 통합  
5. **Sync+Restart 예제**: 파일 변경 시 자동 재시작 설정  

**참고 이미지**:  
- [포트 매핑 예시](https://docs.docker.com/compose/compose-file/compose-file-v3.md#ports)  
- [바인드 마운트 예시](https://docs.docker.com/engine/tutorials/dockervolumes/images/bind-mount-diagram.png)  

---

## 2. 핵심 개념

- **Docker Networking**: 컨테이너 간 통신과 호스트 연결을 관리하는 기능  
- **포트 매핑**: 호스트 포트와 컨테이너 포트를 연결해 외부 접근 허용  
- **바인드 마운트**: 호스트 파일 폴더를 컨테이너에 연결해 실시간 동기화  
- **Docker Compose**: 여러 컨테이너를 하나의 파일로 관리  
- **실시간 모니터링**: 파일 변경 시 자동으로 컨테이너 재시작  
- **Sync+Restart 패턴**: 파일 변경 → 자동 재시작 → 애플리케이션 재시작  

### 단계별 설명  
1. **포트 매핑**  
   - 호스트(예: 80) → 컨테이너(예: 8080) 연결  
   - 외부 사용자가 `http://localhost`로 애플리케이션 접근 가능  
2. **바인드 마운트**  
   - 호스트 파일 폴더(예: `./app`) → 컨테이너 폴더(`/app`) 연결  
   - 실시간으로 파일 변경 시 컨테이너 자동 업데이트  
3. **Docker Compose**  
   - `docker-compose.yml` 파일로 서비스 설정  
   - 예:  
     ```yaml  
     services:  
       web:  
         image: myapp  
         ports: - "80:8080"  
         volumes: - ./app:/app  
     ```  
4. **실시간 모니터링**  
   - 파일 변경 시 `docker-compose up --build` 명령어 자동 실행  
   - 애플리케이션 재시작으로 변경사항 반영  

**참고 이미지**:  
- [Docker Compose 설정 예시](https://docs.docker.com/compose/compose-file/compose-file-v3.md#volumes)  

---

## 3. 장단점

**장점**:  
- 호스트 파일과 컨테이너 실시간 동기화 가능  
- 외부 접근성 확보 (포트 매핑)  
- 다양한 런타임 환경(예: node:alpine)에서 유연한 개발  

**단점**:  
- SELinux 문제로 호스트 시스템 접근 위험  
- 바인드 마운트 시 파일 권한 오류 시 접근 거부  

---

## 4. 자주 사용되는 사례

1. **Node.js 개발**:  
   - 호스트 `./app` 폴더 → 컨테이너 `/app` 연결  
   - 파일 변경 시 자동 재시작  
   - 예: `docker-compose up --build`  
2. **프록시 서버 설정**:  
   - 설정 파일 동기화 → 재시작으로 설정 적용  
3. **SSH 마운트**:  
   - 비공개 저장소 클론 → `ssh://` URL로 바인드 마운트  

---

## 5. 연관 서비스

- **Docker Compose**: 서비스 관리  
- **Dockerfile**: 이미지 빌드  
- **Secret Management**: 비밀 정보 관리  

---

## 6. 공식 문서 링크

- [Docker Networking 공식 문서](https://docs.docker.com/network/)  
- [Docker Compose 네트워크 설정](https://docs.docker.com/compose/networking/)  
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)