# Setup Guide

## 1. ChromaDB 확인 ✓

ChromaDB가 정상적으로 실행 중입니다!

```bash
docker ps | findstr chromadb
```

## 2. OpenAI API Key 설정 (필수)

`.env` 파일을 생성하고 OpenAI API 키를 설정해야 합니다:

```bash
# .env.example을 복사
copy .env.example .env

# .env 파일을 열어서 API 키 입력
notepad .env
```

`.env` 파일 내용:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-4o
CHROMA_HOST=localhost
CHROMA_PORT=8000
```

## 3. 데이터 수집 실행

### 커리큘럼 데이터 수집
```bash
python src/data_ingestion.py
```

### 공식 문서 크롤링 (선택)
```bash
# 전체 서비스 크롤링 (10-20분 소요)
python src/ingest_official_docs.py --service all

# 개별 서비스 크롤링
python src/ingest_official_docs.py --service docker
python src/ingest_official_docs.py --service kubernetes
python src/ingest_official_docs.py --service terraform
python src/ingest_official_docs.py --service istio
python src/ingest_official_docs.py --service argocd
python src/ingest_official_docs.py --service aws
```

## 4. 데이터 확인

```bash
python scripts/verify_persistence.py
```

## 5. 시스템 실행

```bash
# 대화형 모드
python main.py

# 단일 질문
python main.py "What topics are covered in Week 1?"
```

## 문제 해결

### ChromaDB 연결 실패
```bash
docker-compose down
docker-compose up -d
Start-Sleep -Seconds 5
python test_chromadb.py
```

### 데이터 초기화
```bash
docker-compose down -v
docker-compose up -d
python src/data_ingestion.py
```

### 포트 충돌 (8000번 포트)
```bash
# 다른 포트 사용
# docker-compose.yml에서 "8001:8000"으로 변경
# .env에서 CHROMA_PORT=8001로 변경
```
