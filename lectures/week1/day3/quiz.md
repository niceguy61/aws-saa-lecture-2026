# 퀴즈 (Quiz)

## 질문 1

**Dockerfile에서 `--mount type=bind,src=.,target=/app` 옵션의 주요 목적은 무엇인가요?**

A) 호스트 파일 시스템을 컨테이너에 마운트하여 실시간 수정 가능하게 함
B) 컨테이너 내부에서 포트 포워딩을 설정함
C) 이미지의 기본 설정을 변경함
D) 빌드 컨텍스트를 압축하여 저장함

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: bind mount는 호스트의 현재 디렉토리를 컨테이너의 /app 디렉토리에 마운트하여, 호스트에서 파일을 수정할 때 컨테이너 내부에서도 즉시 반영되도록 합니다. 이는 개발 시 실시간 업데이트를 위한 주요 기능입니다.

</details>

---

## 질문 2

**Docker Compose의 watch 모드에서 `sync`와 `sync+restart`의 주요 차이점은 무엇인가요?**

A) sync는 파일 변경 시 컨테이너 재시작을 유발하고, sync+restart는 파일 변경 시 이미지 재빌드를 유발함
B) sync는 파일 변경 시 이미지 재빌드를 유발하고, sync+restart는 파일 변경 시 컨테이너 재시작을 유발함
C) sync는 파일 변경 시 컨테이너를 중지하고, sync+restart는 파일 변경 시 로그를 기록함
D) sync는 파일 변경 시 네트워크를 재설정하고, sync+restart는 파일 변경 시 CPU 사용량을 조절함

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: sync는 파일 변경 시 컨테이너를 재시작하지 않고 즉시 파일을 동기화하는 반면, sync+restart는 파일 변경 시 Docker Compose가 이미지를 재빌드하고 컨테이너를 다시 생성합니다. 이는 종속성 변경 시 전체 재빌드가 필요한 경우에 유용합니다.

</details>

---

## 질문 3

**Dockerfile에서 파일 소유권을 명확히 설정하기 위한 옵션은 무엇인가요?**

A) `COPY --chown`
B) `USER`
C) `WORKDIR`
D) `VOLUME`

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: COPY --chown 옵션은 파일을 복사할 때 특정 사용자에게 소유권을 부여합니다. 예를 들어, `COPY --chown=app:app package.json .`은 app 사용자가 파일을 소유하도록 설정합니다. 이는 컨테이너 내부에서 파일 수정 권한을 보장합니다.

</details>

---

## 질문 4

**Docker bind mount에서 `Z` 옵션의 주요 기능은 무엇인가요?**

A) 호스트와 컨테이너 간 파일 시스템을 암호화함
B) SELinux 라벨을 공유하여 여러 컨테이너가 동일한 마운트를 사용할 수 있도록 함
C) 마운트된 파일 시스템을 읽기 전용으로 설정함
D) 호스트 파일 시스템을 컨테이너에 실시간으로 동기화함

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: Z 옵션은 SELinux 라벨을 공유하여 여러 컨테이너가 동일한 bind mount를 사용할 수 있도록 합니다. 이는 SELinux 정책에 따라 마운트된 파일 시스템의 접근 권한을 제어하는 데 사용됩니다.

</details>

---

