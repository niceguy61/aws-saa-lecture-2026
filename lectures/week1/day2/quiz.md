# 📘 Week 1 - Day 2

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step8.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 8</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <span style="color: rgba(255,255,255,0.5); padding: 8px 16px;">다음 ➡️</span>
</div>

---

---

# 📘 Week 1 - Day 2

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step8.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 8</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <span style="color: rgba(255,255,255,0.5); padding: 8px 16px;">다음 ➡️</span>
</div>

---

# 퀴즈 (Quiz)

## ❓ 질문 1

**Docker 컨테이너에서 포트 매핑을 설정하는 옵션은 무엇인가요?**

A) -p
B) --expose
C) -e
D) --network

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: Docker에서 포트 매핑은 `-p` 옵션을 사용하여 설정합니다. 예를 들어 `docker run -p 8080:80`은 호스트의 8080 포트를 컨테이너의 80 포트로 매핑합니다. 다른 옵션들은 환경 변수 설정, 네트워크 구성 등 다른 기능을 수행합니다.

</details>

---

## ❓ 질문 2

**Docker Compose에서 `--mount type=bind,src=.,target=/app` 옵션의 목적은 무엇인가요?**

A) 호스트 파일 시스템을 컨테이너의 /app 디렉토리에 바인드
B) 컨테이너 내부 파일 시스템을 호스트에 공유
C) Docker 이미지의 기본 디렉토리를 변경
D) 컨테이너의 포트를 호스트에 노출

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  `--mount type=bind` 옵션은 호스트의 현재 디렉토리(`src=.`)를 컨테이너의 `/app` 디렉토리에 바인드하여 파일을 실시간으로 동기화합니다. 이는 개발 중 변경된 소스 파일을 즉시 컨테이너에 반영할 수 있도록 합니다.

</details>

---

## ❓ 질문 3

**Docker Compose의 `watch` 모드에서 `ignore` 규칙이 적용되는 경우는 어떤 상황인가요?**

A) `package.json` 파일이 변경될 때
B) `node_modules` 폴더가 변경될 때
C) `requirements.txt` 파일이 변경될 때
D) `Dockerfile`이 변경될 때

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**:  `ignore` 규칙은 특정 경로의 변경을 무시하도록 설정합니다. 예시에서 `myproject/web/node_modules/`는 `ignore` 대상이지만 `myproject/node_modules/`는 아닌 것으로 보입니다. 이는 `node_modules`는 일반적으로 개발 중 동기화 대상이 아니므로 제외하는 경우입니다.

</details>

---

## ❓ 질문 4

**Docker에서 비밀 정보를 파일과 환경 변수로 동시에 마운트하는 방법은 무엇인가요?**

A) `--mount`와 `--env` 옵션을 함께 사용
B) `--secret`과 `--env` 옵션을 함께 사용
C) `--volume`과 `--env` 옵션을 함께 사용
D) `--bind`와 `--env` 옵션을 함께 사용

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**:  `--mount` 옵션으로 비밀 정보를 파일로 마운트하고, `env` 옵션으로 환경 변수로 전달할 수 있습니다. 예를 들어 `--mount type=secret,id=aws-secret-key,env=AWS_SECRET_ACCESS_KEY`처럼 사용하여 동일한 비밀 정보를 파일과 환경 변수로 동시에 제공할 수 있습니다.

</details>

---

---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 2 학습 완료!</h3>
  <p style="margin: 0; opacity: 0.9;">다음 단계로 계속 진행하세요</p>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;">
  <a href="handson_step8.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">⬅️ 이전<br/><span style="font-size: 12px; opacity: 0.8;">🛠️ Hands-on Lab - Step 8</span></a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;">🏠<br/><span style="font-size: 12px;">목차로</span></a>
  <span style="color: rgba(255,255,255,0.5); padding: 10px 20px;">다음 ➡️</span>
</div>

---

<div style="text-align: center; padding: 10px; color: #666; font-size: 12px;">
  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>
  <p style="margin-top: 5px;">📅 Week 1 Day 2 | 🎯 DevOps 6개월 교육과정</p>
</div>

---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 2 학습 완료!</h3>
  <p style="margin: 0; opacity: 0.9;">다음 단계로 계속 진행하세요</p>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;">
  <a href="handson_step8.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">⬅️ 이전<br/><span style="font-size: 12px; opacity: 0.8;">🛠️ Hands-on Lab - Step 8</span></a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;">🏠<br/><span style="font-size: 12px;">목차로</span></a>
  <span style="color: rgba(255,255,255,0.5); padding: 10px 20px;">다음 ➡️</span>
</div>

---

<div style="text-align: center; padding: 10px; color: #666; font-size: 12px;">
  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>
  <p style="margin-top: 5px;">📅 Week 1 Day 2 | 🎯 DevOps 6개월 교육과정</p>
</div>
