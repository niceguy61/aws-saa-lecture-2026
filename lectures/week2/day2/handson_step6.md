# Hands-on Lab - Step 6

## Step 6: Docker Registry 연동 테스트

**목표**: Docker Registry 서비스와의 통신 확인

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
# 로컬 Docker Registry 서버 실행
docker run -d -p 5000:5000 --name registry registry:2
# 이미지 푸시
docker tag my-node-app localhost:5000/my-node-app
docker push localhost:5000/my-node-app
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
Push to registry: 100%
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker images | grep my-node-app
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 이미지 푸시 실패
해결: 'docker login' 명령어로 로그인 상태 확인

</details>

