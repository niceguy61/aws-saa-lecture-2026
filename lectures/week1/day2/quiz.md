# 퀴즈 (Quiz)

## 질문 1

**Docker 명령어에서 '-w /app' 옵션의 주요 역할은 무엇인가요?**

A) 컨테이너의 포트 매핑 설정
B) 작업 디렉토리 설정
C) 네트워크 설정
D) 데몬 모드 활성화

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  '-w /app'는 컨테이너에서 명령어를 실행할 작업 디렉토리를 설정하는 옵션입니다. 이는 커맨드가 실행될 기준 경로를 지정하여 파일 경로 처리에 영향을 미칩니다.

</details>

---

## 질문 2

**bind mount와 volume mount의 주요 차이점은 무엇인가요?**

A) bind mount는 실시간 동기화를 지원하고 volume mount는 아님
B) bind mount는 호스트 파일을 직접 마운트하고 volume mount는 볼륨 드라이브를 사용함
C) bind mount는 컨테이너 내부 파일만 수정 가능하고 volume mount는 호스트 파일도 수정 가능함
D) bind mount는 Dockerfile에서 정의하고 volume mount는 docker-compose에서만 정의됨

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: bind mount는 호스트 파일을 컨테이너에 직접 마운트하는 반면, volume mount는 Docker Volume이라는 가상 디스크를 사용합니다. bind mount는 실시간 동기화를 지원하지만, volume mount는 별도의 볼륨 드라이브를 필요로 합니다.

</details>

---

## 질문 3

**Docker 명령어로 포트 8080을 호스트 3000으로 매핑하는 올바른 구문은 무엇인가요?**

A) -p 8080:3000
B) --port 3000:8080
C) -expose 8080:3000
D) -publish 3000:8080

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  '-p' 옵션은 호스트 포트:컨테이너 포트 형식으로 포트 매핑을 설정합니다. 예시에서 호스트 3000 포트를 컨테이너 8080 포트로 매핑하려면 '-p 8080:3000'이 올바른 구문입니다.

</details>

---

## 질문 4

**docker-compose.yml에서 'ignore' 필드의 주요 목적은 무엇인가요?**

A) 변경 사항을 무시하여 빌드 속도를 향상시킴
B) 특정 파일 변경 시 재빌드를 방지함
C) 컨테이너 내부 파일 시스템을 보호함
D) 데몬 모드에서 자동 업데이트를 막음

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  'ignore' 필드는 특정 경로의 변경을 무시하여 빌드 과정에서 불필요한 재빌드를 방지합니다. 예를 들어, node_modules 폴더 변경은 무시되지만, package.json 변경은 재빌드를 트리거합니다.

</details>

---

