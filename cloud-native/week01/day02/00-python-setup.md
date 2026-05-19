# Day2 사전 준비 - Python 설치와 확인

## 목표

Day2 실습 앱은 Python 3로 실행한다. Python이 설치되어 있지 않으면 5교시 실습에서 바로 막히므로, 먼저 설치 여부를 확인하고 필요한 경우 설치한다.

## 오늘 한 줄 요약

터미널에서 Python 3 버전이 출력되면 Day2 실습을 시작할 수 있다.

## 1단계 - 먼저 설치 여부 확인

터미널을 열고 아래 명령을 실행한다.

macOS, Linux, WSL:

```bash
python3 --version
```

Windows PowerShell:

```powershell
python --version
py --version
```

아래처럼 `Python 3.x.x`가 보이면 설치되어 있는 것이다.

```text
Python 3.12.0
```

정확한 버전 번호는 달라도 된다. 이 실습은 Python 3.9 이상이면 충분하다.

## 2단계 - Windows 설치

Windows에서는 세 가지 방법 중 하나를 사용한다. 이미 설치되어 있으면 다시 설치하지 않아도 된다.

### 방법 A - Microsoft Store

1. 시작 메뉴에서 `Microsoft Store`를 연다.
2. `Python 3`를 검색한다.
3. 최신 Python 3 버전을 설치한다.
4. PowerShell을 새로 열고 확인한다.

```powershell
python --version
```

### 방법 B - winget

PowerShell에서 아래 명령을 실행한다.

```powershell
winget install Python.Python.3.12
```

설치 후 PowerShell을 새로 열고 확인한다.

```powershell
python --version
py --version
```

### 방법 C - 공식 설치 파일

1. 브라우저에서 `https://www.python.org/downloads/`를 연다.
2. Windows용 Python 3 설치 파일을 받는다.
3. 설치 첫 화면에서 `Add python.exe to PATH`를 체크한다.
4. 설치를 진행한다.
5. PowerShell을 새로 열고 확인한다.

```powershell
python --version
```

주의: `Add python.exe to PATH`를 체크하지 않으면 터미널에서 `python` 명령을 찾지 못할 수 있다.

## 3단계 - macOS 설치

macOS에서는 두 가지 방법 중 하나를 사용한다.

### 방법 A - 공식 설치 파일

1. 브라우저에서 `https://www.python.org/downloads/`를 연다.
2. macOS용 Python 3 설치 파일을 받는다.
3. 설치 후 Terminal을 새로 연다.
4. 아래 명령으로 확인한다.

```bash
python3 --version
```

### 방법 B - Homebrew

Homebrew를 이미 쓰고 있다면 아래 명령을 사용할 수 있다.

```bash
brew install python
```

설치 후 확인한다.

```bash
python3 --version
```

## 4단계 - Ubuntu 또는 WSL 설치

Ubuntu 또는 WSL에서는 아래 명령을 사용한다.

```bash
sudo apt update
sudo apt install -y python3
```

설치 후 확인한다.

```bash
python3 --version
```

## 5단계 - 실습 앱 실행 전 최종 확인

저장소 루트에서 아래 명령을 실행한다.

```bash
cd cloud-native/week01/day02/app
python3 server.py
```

Windows PowerShell에서 `python3`가 안 되면 아래 중 하나를 사용한다.

```powershell
python server.py
py server.py
```

성공하면 아래와 비슷한 출력이 보인다.

```text
starting day2 demo server
listening on http://localhost:8000
```

브라우저에서 아래 주소를 연다.

```text
http://localhost:8000
```

화면이 보이면 준비가 끝난 것이다.

서버를 종료할 때는 서버가 실행 중인 터미널에서 아래 키를 누른다.

```text
Ctrl+C
```

## 자주 막히는 경우

| 증상 | 가능한 원인 | 해결 |
|---|---|---|
| `python` 명령을 찾을 수 없음 | Python 미설치 또는 PATH 미설정 | 설치 후 터미널을 새로 연다 |
| `python3`는 안 되지만 `python`은 됨 | OS별 명령 이름 차이 | 해당 OS에서 되는 명령을 사용한다 |
| Windows에서 설치했는데 계속 안 됨 | PATH 반영 전 터미널을 계속 사용 중 | PowerShell을 완전히 닫고 다시 연다 |
| `server.py`를 찾을 수 없음 | 폴더 위치가 다름 | `pwd`, `ls`, `dir`로 현재 위치를 확인한다 |
| `Address already in use` | 8000번 포트를 이미 사용 중 | 기존 서버를 `Ctrl+C`로 종료하거나 다른 포트로 실행한다 |

## 마무리 체크

아래 세 가지가 되면 Day2 실습을 진행할 수 있다.

- Python 3 버전 확인이 된다.
- `server.py`가 있는 폴더로 이동할 수 있다.
- `http://localhost:8000` 화면을 열 수 있다.
