# Hands-on Lab - Step 7

## Step 7: 실시간 동기화 테스트

**목표**: 코드 변경 시 자동 재빌드 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
echo "console.log('Test');" >> src/index.js
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
브라우저에서 'Test' 로그 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f <container-id> | grep 'Test'
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 재빌드 실패 → docker-compose build --no-cache로 재빌드
- 문제: 파일 동기화 안됨 → 바인드 마운트 경로 재확인

</details>

---

## 실습 완료

Docker 개발 환경을 성공적으로 구성했습니다. 포트 매핑, 바인드 마운트, 실시간 코드 동기화 기능을 활용해 애플리케이션을 실행하고 AWS Secret Manager와 연동하는 방법을 익혔습니다. 이 실습을 통해 컨테이너화된 개발 환경의 기초를 다졌습니다.

**다음 단계**:
- Docker Compose로 복잡한 환경 구성
- CI/CD 파이프라인 설정
- AWS Secrets Manager 실습 가이드: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

