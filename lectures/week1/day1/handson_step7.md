# 📘 Week 1 - Day 1

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
  <a href="handson_step6.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">⬅️ 이전: 🛠️ Hands-on Lab - Step 6</a>
  <a href="../README.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;">🏠 목차</a>
  <a href="quiz.md" style="color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;">다음: ❓ 퀴즈 ➡️</a>
</div>

---

# 👉 Hands-on Lab - Step 7

## 👉 Step 7: 로그 모니터링

**목표**: 컨테이너 로그를 실시간으로 확인합니다.

**명령어**:

```bash
docker logs -f webapp-container

```

**예상 출력**:

```

실시간 로그 출력

```

**확인 방법**:

```bash
docker logs webapp-container

```

**문제 해결**:
- 문제: 로그 출력 없음 → docker logs --tail 100 webapp-container로 확인
- 문제: 컨테이너 정지 → docker start webapp-container 실행

---

## 🎉 실습 완료

Docker 컨테이너를 AWS EC2에 성공적으로 배포하고 로그를 확인했습니다. 이 실습을 통해 CI/CD 파이프라인의 기본 흐름을 이해했습니다.

**다음 단계**:
- AWS CodePipeline을 사용한 자동화 배포 구현
- Docker Compose로 다중 컨테이너 배포
- CloudWatch로 로그 모니터링 설정



---

<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;">
  <h3 style="margin: 0 0 10px 0;">🎓 Week 1 - Day 1 학습 완료!</h3>
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
  <p style="margin-top: 5px;">📅 Week 1 Day 1 | 🎯 DevOps 6개월 교육과정</p>
</div>
