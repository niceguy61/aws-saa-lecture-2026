# 📘 Week 1 - Day 5

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step6.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 6</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="quiz.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: ❓ 퀴즈 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 7

## 👉 Step 7: 애플리케이션 테스트

**목표**: 포트 접근 및 동작 확인

**명령어**:

```bash
curl http://localhost:3000

```

**예상 출력**:

```

HTTP 응답 코드 200

```

**확인 방법**:

```bash
curl -I http://localhost:3000

```

**문제 해결**:
- 문제: 접근 거부 → 포트 확인: docker port <container-id>

---

## 🎉 실습 완료

Docker 네트워킹을 통해 바인드 마운트와 포트 매핑을 설정하여 개발 환경을 구성했습니다. 실시간 코드 변경이 가능하며, 개발 서버 상태를 확인하고 테스트하는 방법을 익혔습니다.

**다음 단계**:
- Docker Compose로 네트워크 구성
- Secrets Manager로 보안 설정 심화
- Docker 네트워크 정책 구성 가이드: https://docs.docker.com/network/



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 5 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 5 | 🎯 DevOps 6개월 교육과정</p>
</div>
