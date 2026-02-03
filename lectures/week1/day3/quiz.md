# 📘 Week 1 - Day 3

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step7.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 7</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <span style="color: rgba(255,255,255,0.5); padding: 8px 16px;">다음 ➡️</span>
</div>

---

# 퀴즈 (Quiz)

## ❓ 질문 1

**Dockerfile에서 작업 디렉토리를 설정하는 옵션은 무엇인가요?**

A) --mount
B) -w
C) --chown
D) -v

<details>
<summary>정답 및 해설 보기</summary>

**답**: B

**설명**: -w 옵션은 Dockerfile에서 작업 디렉토리를 설정하는 데 사용됩니다. 예를 들어, -w /app은 컨테이너 내에서 명령어를 실행할 디렉토리를 /app으로 지정합니다. 이는 Dockerfile의 WORKDIR 명령어와 유사한 기능을 수행합니다.

</details>

---

## ❓ 질문 2

**Docker Compose에서 실시간으로 파일 변경을 감지하여 호스트와 컨테이너 파일을 동기화하는 기능은 무엇인가요?**

A) watch
B) sync
C) rebuild
D) mount

<details>
<summary>정답 및 해설 보기</summary>

**답**: A

**설명**: watch 기능은 Docker Compose에서 특정 경로의 파일 변경을 감지하여 호스트와 컨테이너 간 파일을 실시간으로 동기화합니다. 이 기능은 개발 중에 소스 코드 변경을 즉시 반영할 때 유용합니다. sync는 단순히 파일을 복사하는 기능으로, 변경 감지 기능은 포함하지 않습니다.

</details>



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 3 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 3 | 🎯 DevOps 6개월 교육과정</p>
</div>
