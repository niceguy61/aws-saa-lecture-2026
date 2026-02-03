# Ollama 로컬 LLM 설정 가이드

## 1. Ollama 설치

### Windows
```powershell
# Ollama 다운로드 및 설치
# https://ollama.ai/download 에서 Windows 버전 다운로드
```

### 설치 확인
```powershell
ollama --version
```

## 2. 필요한 모델 다운로드

### Qwen2.5:7b (메인 LLM)
```powershell
ollama pull qwen2.5:7b
```

### Nomic Embed Text (임베딩)
```powershell
ollama pull nomic-embed-text
```

### 모델 확인
```powershell
ollama list
```

## 3. Ollama 서버 실행

Ollama는 설치 시 자동으로 백그라운드에서 실행됩니다.

### 수동 실행 (필요시)
```powershell
ollama serve
```

### 서버 확인
```powershell
curl http://localhost:11434
```

## 4. 환경 변수 설정

`.env` 파일 생성:
```bash
copy .env.example .env
```

`.env` 파일 내용:
```env
# LLM Provider
LLM_PROVIDER=ollama

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:7b

# Embedding Configuration
EMBEDDING_PROVIDER=ollama
OLLAMA_EMBEDDING_MODEL=nomic-embed-text

# ChromaDB Configuration
CHROMA_HOST=localhost
CHROMA_PORT=8000
```

## 5. 모델 테스트

### Qwen2.5 테스트
```powershell
ollama run qwen2.5:7b "Explain Docker in one sentence"
```

### Nomic Embed 테스트
```powershell
ollama run nomic-embed-text "test embedding"
```

## 6. 시스템 실행

### ChromaDB 시작
```powershell
docker-compose up -d
```

### 데이터 수집
```powershell
python src/data_ingestion.py
```

### 공식 문서 크롤링 (선택)
```powershell
python src/ingest_official_docs.py --service docker
```

### 시스템 실행
```powershell
python main.py
```

## 모델 추천

### 메인 LLM 옵션
- **qwen2.5:7b** (권장) - 7B 파라미터, 빠르고 정확
- **qwen2.5:14b** - 더 높은 품질, 더 많은 메모리 필요
- **llama3.1:8b** - Meta의 Llama 3.1
- **mistral:7b** - Mistral AI 모델

### 임베딩 모델 옵션
- **nomic-embed-text** (권장) - 768차원, 빠르고 정확
- **mxbai-embed-large** - 1024차원, 더 높은 품질
- **all-minilm** - 384차원, 가장 빠름

## 성능 최적화

### GPU 사용 (NVIDIA)
Ollama는 자동으로 GPU를 감지하고 사용합니다.

### CPU 전용
```env
OLLAMA_NUM_GPU=0
```

### 메모리 제한
```env
OLLAMA_MAX_LOADED_MODELS=1
```

## 문제 해결

### Ollama 서버 연결 실패
```powershell
# 서비스 재시작
Stop-Service Ollama
Start-Service Ollama

# 또는 수동 실행
ollama serve
```

### 모델 다운로드 느림
```powershell
# 다른 미러 사용
$env:OLLAMA_MIRROR="https://ollama.ai"
ollama pull qwen2.5:7b
```

### 메모리 부족
- 더 작은 모델 사용 (qwen2.5:3b)
- 다른 프로그램 종료
- 시스템 메모리 확인

## 비교: OpenAI vs Ollama

| 항목 | OpenAI | Ollama |
|------|--------|--------|
| 비용 | 유료 (API 호출당) | 무료 (로컬) |
| 속도 | 빠름 (API) | 중간 (로컬 하드웨어 의존) |
| 품질 | 매우 높음 | 높음 |
| 프라이버시 | 클라우드 | 완전 로컬 |
| 인터넷 | 필수 | 불필요 |
| 설정 | 간단 (API 키) | 중간 (모델 다운로드) |

## 권장 시스템 사양

### 최소 사양 (qwen2.5:7b)
- RAM: 8GB
- 디스크: 10GB
- CPU: 4코어

### 권장 사양
- RAM: 16GB
- 디스크: 20GB
- CPU: 8코어
- GPU: NVIDIA (선택)

### 최적 사양 (qwen2.5:14b)
- RAM: 32GB
- 디스크: 30GB
- CPU: 16코어
- GPU: NVIDIA RTX 3060 이상
