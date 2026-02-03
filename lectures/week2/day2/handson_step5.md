# Hands-on Lab - Step 5

## Step 5: 코드 수정 및 동기화 테스트

**목표**: 실시간 코드 동기화 기능 검증

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# src/index.js 파일 수정 후 저장
# 예시: console.log('Hello from Docker!'); 추가
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
콘솔에 'Hello from Docker!' 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker logs -f <container-id>
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 코드 변경 후 재빌드되지 않음
해결: 'docker-compose up --build' 명령어로 강제 재빌드

</details>

