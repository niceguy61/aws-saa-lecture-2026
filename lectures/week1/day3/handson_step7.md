# 📘 Week 1 - Day 3

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step6.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 6</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="quiz.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: ❓ 퀴즈 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 7

## 👉 Step 7: 애플리케이션 테스트

**목표**: 서버 실행 확인 및 종료

**명령어**:

```bash
curl http://localhost:3000 && docker stop myapp-container

```

**예상 출력**:

```

HTTP 200 응답

```

**확인 방법**:

```bash
curl http://localhost:3000

```

**문제 해결**:
- 문제: 연결 거부
  해결: 포트 확인 (docker port myapp-container) 및 방화벽 설정 확인

---

## 🎉 실습 완료

Docker 이미지를 통한 개발 환경 구성 및 실시간 파일 동기화 기능을 완료했습니다. 개발 서버 실행 시 nodemon을 사용해 실시간 업데이트가 가능하며, bind mount를 통해 호스트와 컨테이너 간 파일 동기화를 구현했습니다.

**다음 단계**:
- AWS Secret Mount 사용 실습
- Docker Compose로 다중 서비스 관리
- Docker BuildKit의 advanced features 활용



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 3 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 3 | 🎯 DevOps 6개월 교육과정</p>
</div>
