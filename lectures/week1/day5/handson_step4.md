# Hands-on Lab - Step 4

## Step 4: 컨테이너 간 통신 테스트

**목표**: 다른 컨테이너와의 네트워크 통신 시도

**명령어**:
<details>
<summary>명령어 보기</summary>

```bash
docker run -d --name db --network my_custom_network --env MYSQL_ROOT_PASSWORD=secret mysql:5.7 # DB 컨테이너 실행
docker exec -it db mysql -u root -psecret -e "SHOW DATABASES;" # DB 연결 테스트
```

</details>

**예상 출력**:
<details>
<summary>예상 출력 보기</summary>

```
mysql> SHOW DATABASES; 결과 출력
```

</details>

**확인 방법**:
<details>
<summary>확인 방법 보기</summary>

```bash
docker network inspect my_custom_network
```

</details>

**문제 해결**:
<details>
<summary>문제 해결 보기</summary>

- 문제: 네트워크 분리 → 컨테이너에 --network 옵션 추가
- 문제: 연결 실패 → 포트 확인: docker port db

</details>

