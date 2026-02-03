# 📘 Week 2 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step7.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 7</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <span style="color: rgba(255,255,255,0.5); padding: 8px 16px;">다음 ➡️</span>
</div>

---

# 퀴즈 (Quiz)

## ❓ 질문 1

**Dockerfile에서 `--mount type=bind,src=.,target=/app` 명령어의 주요 목적은 무엇인가요?**

A) 컨테이너 내부에서 호스트 파일 시스템을 실시간으로 동기화합니다.
B) 이미지 레이어를 압축하여 저장공간을 절약합니다.
C) Docker Hub에 이미지를 공유합니다.
D) 컨테이너의 네트워크 포트를 호스트에 매핑합니다.

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: bind mount는 호스트의 현재 디렉터리(`src=.`)를 컨테이너의 `/app` 경로에 마운트하여, 개발 중에 파일 변경이 실시간으로 반영되도록 합니다. 이는 개발자 경험 향상을 위한 주요 기능입니다.

</details>

---

## ❓ 질문 2

**Dockerfile에서 `WORKDIR /app` 명령어의 역할은 무엇인가요?**

A) 컨테,이너의 기본 이미지로 사용됩니다.
B) 명령어 실행 시 작업 디렉터리를 `/app`으로 설정합니다.
C) 컨테이너의 포트를 호스트에 매핑합니다.
D) Docker Compose 파일의 서비스 정의를 나타냅니다.

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: `WORKDIR`는 명령어 실행 시 작업 디렉터리를 지정하는 역할을 합니다. 예를 들어 `npm install` 명령어는 `/app` 디렉터리 내에서 실행됩니다.

</details>

---

## ❓ 질문 3

**Dockerfile에서 `COPY --chown` 플래그의 주요 목적은 무엇인가요?**

A) 파일을 압축하여 저장공간을 절약합니다.
B) 파일 소유권을 특정 사용자에게 설정하여 보안을 강화합니다.
C) 이미지 레이어를 최소화합니다.
D) 컨테이너의 네트워크 설정을 변경합니다.

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: `COPY --chown`은 파일을 컨테이너에 복사할 때 소유자를 명시적으로 설정하여, 컨테이너 내부에서 파일 접근 권한을 제어하는 데 사용됩니다. 예: `COPY --chown=app:app package.json .`

</details>

---

## ❓ 질문 4

**Docker Compose에서 `watch` 모드의 `sync+restart` 동작은 어떤 경우에 발생합니까?**

A) `package.json` 변경 시 이미지 재빌드 및 컨테이너 재시작
B) `nginx.conf` 변경 시 실시간 동기화
C) `node_modules` 변경 시 파일 삭제
D) `Dockerfile` 변경 시 컨테이너 종료

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: `sync+restart` 동작은 `package.json`과 같은 의존성 파일 변경 시 이미지 재빌드와 컨테이너 재시작을 트리거합니다. 반면 `sync`는 파일 변경 시 즉시 동기화만 수행합니다.

</details>

---

## ❓ 질문 5

**Docker `--mount` 옵션에서 `:z` 플래그의 주요 기능은 무엇인가요?**

A) 호스트 파일 시스템을 컨테이너에 마운트합니다.
B) 여러 컨테이너가 동일한 바인드 마운트를 공유할 수 있도록 설정합니다.
C) 컨테이너의 포트를 호스트에 매핑합니다.
D) SELinux 라벨을 제거합니다.

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: `:z` 플래그는 SELinux 정책을 통해 여러 컨테이너가 동일한 바인드 마운트를 공유할 수 있도록 허용합니다. 이는 컨테이너 간 파일 공유를 용이하게 만듭니다.

</details>



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 2 - Day 1 학습 완료!</h3>
  <p style="margin: 0; opacity: 0.9;">다음 단계로 계속 진행하세요</p>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;">
  <a href="handson_step7.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">⬅️ 이전<br/><span style="font-size: 12px; opacity: 0.8;">🛠️ Hands-on Lab - Step 7</span></a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;">🏠<br/><span style="font-size: 12px;">목차로</span></a>
  <span style="color: rgba(255,255,255,0.5); padding: 10px 20px;">다음 ➡️</span>
</div>

---

<div style="text-align: center; padding: 10px; color: #666; font-size: 12px;">
  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>
  <p style="margin-top: 5px;">📅 Week 2 Day 1 | 🎯 DevOps 6개월 교육과정</p>
</div>
