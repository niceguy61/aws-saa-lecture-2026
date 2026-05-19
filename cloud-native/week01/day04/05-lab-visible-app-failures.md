# 5교시 - 핸즈온: 눈에 보이는 앱 실패 만들기

## 목표

이 시간의 목표는 시연 앱을 실행한 뒤 일부러 실패 상태를 만들어 보는 것이다. 실패를 두려워하지 않기 위해서는 작은 환경에서 안전하게 실패를 관찰해봐야 한다.

이 세션의 끝에서 우리는 다음을 할 수 있어야 한다.

- 앱을 실행하고 브라우저에서 `/`, `/api/products`, `/health`를 확인한다.
- 없는 경로와 데이터 파일 누락이 어떤 증상을 만드는지 본다.
- 서버 로그와 브라우저 응답을 함께 기록한다.

## 오늘 한 줄 요약

작은 실패를 직접 만들어 보면, 큰 장애를 만났을 때 어디부터 봐야 하는지 감이 생긴다.

## 수업 이미지

![웹앱 실패 증상을 브라우저와 로그로 비교하는 모습](assets/stickman-visible-failure.png)

## 오늘의 흐름

| 시간 | 단계 | 진행 |
|---|---|---|
| 14:00-14:08 | 앱 실행 | 시연 앱을 기본 설정으로 실행한다. |
| 14:08-14:20 | 정상 상태 확인 | `/`, `/api/products`, `/health`를 확인한다. |
| 14:20-14:32 | 404 만들기 | 없는 경로를 요청하고 로그를 본다. |
| 14:32-14:43 | 데이터 파일 실패 | 데이터 파일 경로를 바꿔 API 실패를 만든다. |
| 14:43-14:50 | 기록 | 증상, 로그, 원인 후보를 표로 정리한다. |

## 준비

저장소 루트에서 시작한다.

```bash
cd cloud-native/week01/day04/demo_app
```

서버 실행:

```bash
python3 server.py
```

Windows에서 필요하면:

```powershell
py server.py
```

## 정상 상태 확인

브라우저에서 차례로 연다.

```text
http://localhost:8000
```

```text
http://localhost:8000/api/products
```

```text
http://localhost:8000/health
```

확인할 것:

| 경로 | 기대 |
|---|---|
| `/` | 상품 목록 화면 |
| `/api/products` | JSON 데이터 |
| `/health` | `status`가 `ok` |

서버 터미널에 요청 로그가 찍히는지도 본다.

## 실패 1 - 없는 경로 요청

브라우저에서 아래 주소를 연다.

```text
http://localhost:8000/no-page
```

기대:

- 브라우저에는 404 응답이 보인다.
- 서버 로그에는 `status=404`가 찍힌다.

정리:

| 항목 | 기록 |
|---|---|
| 요청한 경로 | |
| 브라우저 응답 | |
| 서버 로그 | |
| 원인 추정 | |

## 실패 2 - 데이터 파일 경로 바꾸기

서버를 `Ctrl+C`로 멈춘다.

없는 데이터 파일을 가리키도록 실행한다.

여기서 `DATA_FILE=...`은 파일을 새로 만드는 명령이 아니다. 서버에게 “이번에는 이 위치의 데이터 파일을 읽어보라”고 알려주는 설정이다. 일부러 없는 파일 이름을 주기 때문에 실패가 난다.

Linux/macOS/WSL:

```bash
DATA_FILE=data/missing-products.json python3 server.py
```

Windows PowerShell:

```powershell
$env:DATA_FILE="data/missing-products.json"; py server.py
```

브라우저에서 확인한다.

```text
http://localhost:8000/api/products
```

```text
http://localhost:8000/health
```

기대:

- `/api/products`는 데이터 파일을 읽지 못해 실패한다.
- `/health`는 unhealthy 상태를 보여준다.
- 서버 로그에는 데이터 파일을 찾지 못했다는 단서가 남는다.

해석:

| 관찰 | 의미 |
|---|---|
| `/api/products`가 `500` | API가 데이터를 읽다가 실패했다 |
| `/health`가 `unhealthy` | 앱이 켜져 있지만 운영 상태가 좋지 않다 |
| `data file not found` | 데이터 파일 경로나 파일 존재 여부를 봐야 한다 |

이 상황은 “컴퓨터가 고장났다”가 아니라 “앱이 필요한 데이터 파일을 못 찾는다”에 가깝다.

## 실패 3 - 앱 이름 바꾸기

서버를 멈춘 뒤 앱 이름을 바꿔 실행한다.

Linux/macOS/WSL:

```bash
APP_NAME=practice-shop python3 server.py
```

Windows PowerShell:

```powershell
$env:APP_NAME="practice-shop"; py server.py
```

브라우저에서 `/`와 `/health`를 확인한다. 앱 이름은 화면과 health 응답에서 바뀐다.

이 실패는 진짜 장애가 아니라 설정 변경 관찰이다. 같은 코드라도 실행할 때 전달한 설정에 따라 화면과 응답이 바뀔 수 있음을 보기 위한 실습이다.

## 정리 표

| 상황 | 브라우저 증상 | 서버 로그 | 원인 후보 |
|---|---|---|---|
| 정상 | | | |
| 없는 경로 | | | |
| 데이터 파일 누락 | | | |
| 앱 이름 변경 | | | |

## 주의

오늘 실습은 안전한 실패만 만든다. 파일을 삭제하지 않는다. 특히 `rm`, `rm -r`, `rm -rf`로 문제를 해결하려 하지 않는다.

## 다음 교시 연결

다음 시간에는 방금 만든 실패 증상을 조금 더 체계적으로 진단한다. 브라우저, 서버 로그, health check를 어떤 순서로 볼지 정한다.
