# Hands-on Lab - Step 7

## Step 7: 일반적인 문제 해결

**목표**: 서버 오류 및 마운트 문제 해결

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker inspect dev-container | grep Mounts
docker exec dev-container ls -l /app
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
마운트 경로 및 파일 목록
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker stats dev-container
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: SELinux 오류 → 해결: docker run -d -v $(pwd):/app:z 명령어로 재실행
- 문제: 네트워크 문제 → 해결: docker network inspect bridge 명령어로 네트워크 상태 확인

</details>

---

## 실습 완료

Docker 이미지 생성 및 실시간 개발 환경이 성공적으로 구성되었습니다. 변경된 코드가 자동으로 컨테이너에 반영되고 로그를 통해 실시간으로 확인할 수 있습니다.

**다음 단계**:
- 프로덕션 환경으로 배포
- CI/CD 파이프라인 설정
- 다른 프레임워크(예: Flask)로 동일한 방식 적용

