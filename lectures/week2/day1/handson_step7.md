# 📘 Week 2 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step6.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 6</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="quiz.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: ❓ 퀴즈 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 7

## 👉 Step 7: 실시간 파일 동기화 설정

**목표**: bind mount을 통한 실시간 파일 동기화 구성

**명령어**:

```bash
docker stop myapp-container && docker rm myapp-container && docker run -d -p 3000:3000 --name myapp-container -v "/$(pwd)/src:/app/src" myapp:latest

```

**예상 출력**:

```

컨테이너 재시작

```

**확인 방법**:

```bash
docker ps

```

**문제 해결**:
- 문제: 마운트 실패 → 'docker run' 명령어 재확인
- 문제: 권한 문제 → 'chmod'로 파일 권한 변경

---

## 🎉 실습 완료

이 실습을 통해 Dockerfile을 작성하여 Node.js 애플리케이션을 배포하고, bind mount를 사용한 실시간 파일 동기화 및 비밀 변수 마운트 기능을 구현했습니다. Docker Compose를 활용한 서비스 실행 및 로그 확인 방법을 익혔습니다.

**다음 단계**:
- CI/CD 파이프라인 설정 (GitHub Actions)
- Docker Compose로 다중 서비스 배포
- AWS Secrets Manager 통한 보안 강화



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 2 - Day 1 학습 완료!</h3>
  <p style="margin: 0; opacity: 0.9;">다음 단계로 계속 진행하세요</p>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;">
  <a href="handson_step6.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">⬅️ 이전<br/><span style="font-size: 12px; opacity: 0.8;">🛠️ Hands-on Lab - Step 6</span></a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;">🏠<br/><span style="font-size: 12px;">목차로</span></a>
  <a href="quiz.md" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;">다음 ➡️<br/><span style="font-size: 12px; opacity: 0.8;">❓ 퀴즈</span></a>
</div>

---

<div style="text-align: center; padding: 10px; color: #666; font-size: 12px;">
  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>
  <p style="margin-top: 5px;">📅 Week 2 Day 1 | 🎯 DevOps 6개월 교육과정</p>
</div>
