# 퀴즈 (Quiz)

## 질문 1

**Docker에서 --mount 옵션의 주요 용도는 무엇인가요?**

A) 컨테이너 내부 파일 시스템을 호스트에 복사합니다
B) 호스트의 특정 디렉터리를 컨테이너에 바인드 마운트합니다
C) 네트워크 포트를 호스트와 컨테이너 간에 매핑합니다
D) 컨테이너의 작업 디렉터리를 설정합니다

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: --mount는 호스트의 파일 시스템을 컨테이너에 바인드 마운트하는 기능입니다. 예를 들어 --mount type=bind,src=.,target=/app는 현재 디렉터리를 컨테이너의 /app 경로에 마운트합니다. 이는 실시간으로 파일 변경을 반영할 수 있는 동적 파일 공유 기능입니다.

</details>

---

## 질문 2

**Docker 컨테이너에서 포트 매핑을 구성할 때 -p 옵션의 올바른 사용법은 무엇인가요?**

A) -p 80:3000 호스트 80포트를 컨테이너 3000포트로 매핑합니다
B) -p 3000:80 호스트 3000포트를 컨테이너 80포트로 매핑합니다
C) -p 80:3000 호스트 3000포트를 컨테이너 80포트로 매핑합니다
D) -p 3000:80 호스트 80포트를 컨테이너 3000포트로 매핑합니다

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: -p 3000:80은 호스트의 3000포트를 컨테이너의 80포트로 매핑합니다. 이는 외부에서 컨테이너의 80포트를 접근할 때 호스트의 3000포트로 전달하는 방식입니다. 예를 들어 Node.js 애플리케이션의 80포트를 호스트의 3000포트로 노출시킬 때 사용합니다.

</details>

---

## 질문 3

**-w 옵션의 주요 기능은 무엇인가요?**

A) 컨테이너의 작업 디렉터리를 설정합니다
B) 호스트 파일 시스템을 컨테이너에 마운트합니다
C) 네트워크 포트를 호스트와 컨테이너 간에 매핑합니다
D) Docker 이미지의 기본 경로를 변경합니다

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: -w 옵션은 컨테이너의 작업 디렉터리를 설정합니다. 예를 들어 -w /app은 커맨드가 실행될 디렉터리를 /app으로 지정합니다. 이는 npm install 또는 npm run dev 명령어가 실행될 경로를 설정하는 데 사용됩니다.

</details>

---

## 질문 4

**Docker Compose에서 bind mount와 volume의 주요 차이점은 무엇인가요?**

A) bind mount는 실시간 파일 동기화를 지원하고, volume은 정적 파일 저장소입니다
B) volume은 실시간 파일 동기화를 지원하고, bind mount는 정적 파일 저장소입니다
C) bind mount는 호스트 디렉터리를 컨테이너에 마운트하고, volume은 컨테이너 내부 디렉터리에 파일을 저장합니다
D) volume은 호스트 디렉터리를 컨테이너에 마운트하고, bind mount는 컨테이너 내부 디렉터리에 파일을 저장합니다

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: bind mount는 호스트 디렉터리를 컨테이너에 마운트하여 실시간 파일 동기화를 지원합니다. 반면 volume은 컨테이너 내부 디렉터리에 파일을 저장하고, 정적 데이터 저장에 적합합니다. 예를 들어, 개발 중인 소스 코드는 bind mount로 동기화하고, 데이터베이스는 volume으로 관리하는 것이 일반적입니다.

</details>

---

## 질문 5

**Docker Compose에서 bind mount의 올바른 구문은 다음 중哪一个인가요?**

A) volumes: - type: bind, source: ./static, target: /opt/app/static
B) volumes: - type: volume, source: ./static, target: /opt/app/static
C) volumes: - type: bind, source: /opt/app/static, target: ./static
D) volumes: - type: volume, source: /opt/app/static, target: ./static

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: bind mount의 구문은 type: bind, source(호스트 디렉터리), target(컨테이너 디렉터리)를 지정해야 합니다. 예시에서 ./static(호스트 디렉터리)를 /opt/app/static(컨테이너 디렉터리)로 마운트하므로 A가 정답입니다. volume은 다른 구문을 사용합니다.

</details>

---

