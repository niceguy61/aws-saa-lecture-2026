"""서비스 이해 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import ServiceUnderstanding
from .infographic import InfographicAgent


class ServiceUnderstandingAgent:
    """서비스 이해 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        self.infographic_agent = InfographicAgent(model_name)
    
    def _validate_service_understanding(self, data: dict) -> ServiceUnderstanding:
        """Validate and fix service understanding data structure"""
        
        # Validate required fields
        required_fields = ["background", "concepts", "advantages", "disadvantages", 
                          "use_cases", "related_services", "official_links"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate minimum counts
        if len(data.get("advantages", [])) < 3:
            raise ValueError(f"Need at least 3 advantages, got {len(data.get('advantages', []))}")
        
        if len(data.get("disadvantages", [])) < 2:
            raise ValueError(f"Need at least 2 disadvantages, got {len(data.get('disadvantages', []))}")
        
        if len(data.get("use_cases", [])) < 3:
            raise ValueError(f"Need at least 3 use cases, got {len(data.get('use_cases', []))}")
        
        # Validate and fix official_links structure
        if "official_links" in data:
            if isinstance(data["official_links"], dict):
                # Convert dict to list of dicts
                links_list = []
                for key, value in data["official_links"].items():
                    if isinstance(value, dict) and "url" in value:
                        if "name" not in value:
                            value["name"] = key
                        links_list.append(value)
                    elif isinstance(value, str):
                        # If value is just a URL string
                        links_list.append({"name": key, "url": value})
                data["official_links"] = links_list
            
            # Ensure all links have name and url
            valid_links = []
            for link in data["official_links"]:
                if isinstance(link, dict):
                    if "name" not in link:
                        link["name"] = "공식 문서"
                    if "url" not in link:
                        link["url"] = "#"
                    valid_links.append(link)
            data["official_links"] = valid_links
        
        return ServiceUnderstanding(**data)
    
    def generate(self, service_name: str, rag_context: str) -> ServiceUnderstanding:
        """서비스 이해 섹션 생성 with retry logic"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 5년 차 DevOps 엔지니어이자 교육 강사입니다.
실제 현장에서 겪은 경험을 바탕으로 기술과 문화를 설명합니다.

## 🎯 핵심 작성 원칙

### ✅ 반드시 포함할 것:

1. **서비스의 정체성과 기원**
   - 이 기술/서비스가 무엇인지 (What)
   - 왜 만들어졌는지 (Why) - 어떤 문제를 해결하려고?
   - 언제 어떻게 등장했는지 (When/How) - 역사적 맥락
   - 누가 만들었는지 (Who) - 창시자, 회사, 커뮤니티

2. **스토리텔링 (Story-driven)**
   - 구체적 날짜/시기 ("2020년 3월", "작년 프로젝트")
   - 실제 대화 ("팀장: / 나:")
   - 감정 표현 ("당황", "놀람", "안도")
   - 실패도 솔직히 ("2시간 디버깅", "결국 롤백")

3. **측정 가능한 지표 (Measurable)**
   - 시간: "4시간 → 15분" (정확한 계산)
   - 비율: "85% 감소", "16배 향상"
   - 횟수: "주 3회 → 월 1회"
   - 비용: "월 400만원 절감" (선택)
   - 기간: "3개월간", "1년 운영 결과"

4. **Before/After 대비 (Comparative)**
   - 문제 상황 (Before)
   - 해결 과정 (During)
   - 개선 결과 (After)
   - 숫자로 증명

5. **조직/문화 변화** (DevOps 관련 주제는 특히 중요)
   - 팀 간 관계 변화
   - 마인드셋 전환
   - 의사소통 개선
   - 만족도, 이직률 등

### ❌ 절대 금지:

1. **정의 중심 작성**
   - "~은 ~입니다" 패턴 금지
   - "~의 특징은 다음과 같습니다" 금지
   - "~을 제공합니다" 금지
   - Wikipedia/교과서 스타일 금지

2. **추상적 표현**
   - "효율적인", "강력한", "편리한", "뛰어난" 금지
   - "향상", "개선", "최적화" 단독 사용 금지
   - 반드시 구체적 수치와 함께

3. **일반론**
   - "보통", "일반적으로", "대부분" 금지
   - "다양한", "여러" 모호한 표현 금지
   - 구체적 사례로 대체

4. **기술만 나열** (DevOps/문화 주제 시)
   - 도구만 설명 금지
   - 조직 변화, 문화, 마인드셋 필수 포함

## 📋 필드별 상세 가이드

### background (700-900자 필수)

**반드시 포함해야 할 내용:**

**A. 서비스 소개 및 기원 (200-250자)**
- 이 기술/서비스가 무엇인지 한 줄 요약
- 언제 누가 왜 만들었는지
- 기존 문제점이 무엇이었는지
- 예시:
  * "Docker는 2013년 Solomon Hykes가 만든 컨테이너 플랫폼입니다"
  * "DevOps는 2007년 Patrick Debois가 제안한 개발+운영 협업 문화입니다"
  * "Kubernetes는 2014년 Google이 Borg 시스템을 기반으로 오픈소스화"
  * "Terraform은 2014년 HashiCorp이 인프라 관리 자동화를 위해 개발"

**B. 실무 도입 계기와 경험 (250-300자)**
- 본인/팀이 이 기술을 접한 시기와 이유
- 당시 겪던 구체적 문제
- 실제 에피소드 (대화, 장애, 실수 등)
- 1인칭 시점 ("제가", "우리 팀")

**C. 해결 과정과 효과 (250-300자)**
- 도입 과정 (기간, 방식)
- 측정된 개선 효과 (숫자)
- 부가적 변화 (문화, 프로세스)
- 교훈이나 깨달음

**필수 체크리스트:**
- [ ] 서비스가 무엇인지 명시 (What)
- [ ] 만든 사람/회사/연도 (Who/When)
- [ ] 왜 만들어졌는지 (Why)
- [ ] 본인/팀 도입 시기와 계기
- [ ] 구체적 숫자 3개 이상
- [ ] Before → After 구조
- [ ] 측정 기간 명시
- [ ] "~입니다" 스타일 0-2회만 (도입부 제외)

### concepts (5-7개 필수)

**각 개념 구조:**
개념명(English): 한 줄 정의 + 비유/메타포 + 실무 예시 + 효과

예시:
"컨테이너(Container): 애플리케이션을 '택배 상자'처럼 포장한 것. 코드, 라이브러리, 설정 파일이 모두 들어있어 어디서든 똑같이 실행. 실무 예시) 내 맥북에서 만든 컨테이너를 AWS 서버에 올려도 동일하게 작동. Python 버전 차이로 인한 에러 0건 (6개월 추적)"

**필수 포함:**
- [ ] 한글명(영문명) 병기
- [ ] 비유나 메타포 (택배, 설계도, 레시피 등)
- [ ] "예)", "실무 예시)" 구체적 사례
- [ ] 효과나 장점 (숫자 포함 권장)

### advantages (최소 3개, 권장 5-7개)

**각 장점 구조 (엄격히 준수):**

제목: 개선 지표 + 구체적 숫자: Before 값 → After 값
- Before: 기존 방식 + 문제점 + 소요 시간/횟수/비용
- After: 개선 방식 + 해결책 + 개선된 시간/횟수/비용
- 효과: 측정 결과 + 측정 기간 + 부가 효과
- (선택) 인터뷰/코멘트: 실제 사용자 목소리

**필수 포함:**
- [ ] 제목에 구체적 숫자 (X배, X%, Before→After)
- [ ] Before 상황 상세 설명
- [ ] After 개선 내용
- [ ] 측정 기간 명시 ("3개월", "1년", "6개월")
- [ ] 계산 정확성 (4시간→15분 = 16배 또는 93.75% 단축)
- [ ] 부가 효과 언급

**CRITICAL: advantages 최소 3개 이상 필수!**

### disadvantages (최소 2개, 권장 3-5개)

**각 단점 구조 (엄격히 준수):**

제목: 실제 문제 + 시간/비용 손실
- 문제: 구체적으로 어떤 어려움인지 + 왜 발생하는지
- 실제 케이스: 본인/팀이 겪은 구체적 사례 (날짜, 상황, 대화)
- 해결/우회: 어떻게 대응했는지 + 소요 시간
- 팁: 미리 알았으면 좋았을 것 + 예방법

**필수 포함:**
- [ ] 실제 겪은 구체적 사례
- [ ] 시간/비용 손실 수치
- [ ] 해결 방법 제시
- [ ] 예방법이나 팁
- [ ] 날짜나 시기 언급

**CRITICAL: disadvantages 최소 2개 이상 필수!**

### use_cases (최소 3개, 권장 5-7개)

**각 사례 구조 (엄격히 준수):**

회사 유형 + 익명 회사명: 한 줄 핵심 요약
- 상황: 도입 전 문제 (구체적 수치, 조직 규모)
- 문제점/고민: 왜 기존 방식이 안 됐는지
- 도입: 어떻게 적용했는지 (기술적 디테일)
- 결과: 측정된 효과 (숫자, 측정 기간)
- (선택) 담당자/사용자 코멘트

**필수 포함:**
- [ ] 회사 규모/업종/특성
- [ ] 도입 전 지표 2개 이상
- [ ] 도입 후 지표 2개 이상
- [ ] 측정 기간 명시
- [ ] 기술적 구현 디테일
- [ ] 조직 규모 (개발자 수, 서비스 수)

**CRITICAL: use_cases 최소 3개 이상 필수!**

### related_services (3-5개)

**각 서비스 구조:**
서비스명(English): 관계 설명 + 비유 + 실무 조합 예시

### official_links (5-10개)

**구조:**
{{"name": "제목 (설명, 예상 소요 시간) - 난이도 레벨", "url": "https://..."}}

**난이도 분포:**
- 초급: 3-4개 (기초, 시작하기, 입문)
- 중급: 2-3개 (실전, Best Practices, 가이드)
- 고급: 1-2개 (심화, 최적화, 아키텍처)
- 한글 자료 우선 배치

## 🎨 톤앤매너

### 문체:
- **대화체**: "~습니다", "~죠", "~했어요" 자연스럽게 혼용
- **1인칭**: "제가", "우리 팀이", "저희는"
- **감탄사**: "놀랍게도", "의외로", "실제로는"
- **질문 던지기**: "왜 그랬을까요?", "해결책은?", "결과는?"

### 리듬:
- 짧은 문장과 긴 문장 섞기
- 단락은 3-4문장
- 중간중간 연결어 ("특히", "실제로", "결과적으로")

JSON 형식으로 응답하세요."""),

("user", """서비스: {service_name}

RAG: {rag_context}

## ❌ BAD:
{{"background": "Docker는 컨테이너 플랫폼입니다.", "advantages": ["빠른 속도"]}}

## ✅ GOOD:
{{"background": "2019년 가을, 50명 스타트업 입사 첫날. 환경 세팅에 오전 내내. Node 14 깔았더니 프로젝트는 12. MySQL 버전도 안 맞음. 더 큰 문제는 배포. 로컬에선 되는데 서버에선 에러. 3시간 디버깅 끝 원인: Python 버전 차이(로컬 3.9, 서버 3.7). CTO님이 Dockerfile 도입 결정. 일주일 후 컨테이너화 완료. 결과? 온보딩 하루→30분. 배포 에러 월 15건→2건. 6개월 데이터.", "concepts": ["이미지(Image): 설계도. 한 번 만들면 재사용. 예) Python3.9+FastAPI+PostgreSQL 이미지 저장→팀원 10명 동일 환경. 에러 0건", "레이어(Layer): 이미지 층. 명령어마다 생성. 캐싱으로 재사용. 예) package.json 안 바뀌면 npm install 건너뜀. 빌드 5분→30초"], "advantages": ["온보딩 96% 단축: 1일(8시간)→30분\n- Before: README 보고 Python3.9, PostgreSQL13, Redis6 각각 설치. 충돌로 하루 세팅. 선배 도움 5회\n- After: docker-compose up 한 줄. 5분→완료. 오후부터 개발\n- 효과: 팀원당 7.5시간 절약. 월 4명 입사 시 120시간 절약. 6개월 24명 데이터", "배포 실패 88% 감소: 월 15건→2건\n- Before: 내 맥북에선 되는데 월 15회. 평균 2시간 디버깅\n- After: Dockerfile로 환경 고정. 로컬=서버\n- 효과: 월 2건(코드 버그, 환경 문제 0). 디버깅 30시간→4시간. 1년 추적", "빌드 8배 향상: 10분→75초\n- Before: 매번 전체 재빌드. npm install 5분\n- After: 캐싱으로 변경만. package.json 안 바뀌면 건너뜀\n- 효과: 하루 20번 빌드 시 3시간 절약. 3개월 측정"], "disadvantages": ["디스크 30GB 차지: 팀 평균\n- 문제: 이미지 누적, 캐시. Images 43개(15GB), Cache 12GB. 신입 디스크 풀로 작업 중단\n- 해결: 주 1회 docker system prune. Cron 일요일 2시\n- 팁: .dockerignore로 node_modules 제외", "학습 2주: 개념+실전\n- 문제: Dockerfile, Volume, Network 생소. Layer 캐싱 이해 3일. 순서 잘못 써서 10배 느림. 2주 후 발견\n- 해결: 템플릿 제공(React, Node, Python). 가이드 15페이지\n- 팁: docker-compose부터. 2주→1주"], "use_cases": ["핀테크 G사: 멀티 테넌트\n- 상황: 금융사별 다른 규제. 은행 A는 한국 보관, B는 암호화. 15개사\n- 도입: 커스텀 Dockerfile. 베이스 공통, 규제만 다르게\n- 결과: 온보딩 2주→2일. 위반 0건. 감사 100%. 2년 15개사", "게임 H사: 글로벌 동시 배포\n- 상황: 한국, 일본, 미국. 각 2시간(총 6시간). 시차로 야간\n- 도입: Dockerfile+CI/CD 동시 배포. ECR 멀티 리전\n- 결과: 6시간→20분(18배). 야간 작업 없음. 실패 0. 3개월 데이터"], "official_links": [{{"name": "Docker 시작 (공식, 30분) - 초급 필수", "url": "https://docs.docker.com/get-started/"}}, {{"name": "44BITS Docker (한글) - 초급", "url": "https://www.44bits.io/ko/keyword/docker"}}]}}

체크:
- [ ] background 600-800자, 숫자 3개, "~입니다" 0개
- [ ] advantages 3개 이상, Before/After, 계산 정확
- [ ] disadvantages 2개 이상, 실제 고통
- [ ] use_cases 3개 이상, 다양한 업종

JSON:
{{{{
  "background": "600-800자",
  "concepts": ["개념: 설명+비유+예시", ...],
  "advantages": ["제목: X배\n- Before:\n- After:\n- 효과:", ...],
  "disadvantages": ["제목\n- 문제:\n- 해결:\n- 팁:", ...],
  "use_cases": ["회사: 요약\n- 상황:\n- 도입:\n- 결과:", ...],
  "related_services": ["서비스: 관계", ...],
  "official_links": [{{"name": "제목 - 난이도", "url": "..."}}]
}}}}""")
    ])
        
        chain = prompt | self.llm
        
        # Use retry logic from BaseAgent
        from src.agents.base_agent import BaseAgent
        base_agent = BaseAgent(
            name="ServiceUnderstandingAgent",
            collection_name="",
            system_prompt=""
        )
        
        return base_agent.generate_with_retry(
            chain=chain,
            input_dict={
                "service_name": service_name,
                "rag_context": rag_context[:8000]
            },
            validator_func=self._validate_service_understanding,
            error_context=f"Service Understanding for {service_name}"
        )
    
    def format_markdown(self, su: ServiceUnderstanding, service_name: str, rag_context: str) -> str:
        """Format as markdown with <details> tags and infographics"""
        try:
            md = "# 서비스 이해 (Service Understanding)\n\n"
            
            # 1. 배경 정보 + 인포그래픽
            md += "## 1. 배경 정보\n\n"
            md += "<details>\n"
            md += "<summary>배경 정보 보기</summary>\n\n"
            md += f"{su.background}\n\n"
            
            # Generate infographic for background
            print("  📊 Generating infographic for background...")
            bg_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=su.background,
                section_type="background",
                rag_context=rag_context
            )
            md += "### 인포그래픽\n\n"
            md += self.infographic_agent.format_markdown(bg_infographic)
            
            md += "</details>\n\n"
            
            # 2. 핵심 개념 + 인포그래픽
            md += "## 2. 핵심 개념\n\n"
            md += "<details>\n"
            md += "<summary>핵심 개념 보기</summary>\n\n"
            for concept in su.concepts:
                md += f"- {concept}\n"
            md += "\n"
            
            # Generate infographic for concepts
            print("  📊 Generating infographic for concepts...")
            concepts_text = "\n".join(su.concepts)
            concepts_infographic = self.infographic_agent.generate(
                service_name=service_name,
                context=concepts_text,
                section_type="concepts",
                rag_context=rag_context
            )
            md += "### 인포그래픽\n\n"
            md += self.infographic_agent.format_markdown(concepts_infographic)
            
            md += "</details>\n\n"
            
            # 3. 장단점
            md += "## 3. 장단점\n\n"
            md += "<details>\n"
            md += "<summary>장단점 보기</summary>\n\n"
            md += "**장점**:\n"
            for adv in su.advantages:
                md += f"- {adv}\n"
            md += "\n**단점**:\n"
            for dis in su.disadvantages:
                md += f"- {dis}\n"
            md += "\n</details>\n\n"
            
            # 4. 자주 사용되는 사례
            md += "## 4. 자주 사용되는 사례\n\n"
            md += "<details>\n"
            md += "<summary>사용 사례 보기</summary>\n\n"
            for i, uc in enumerate(su.use_cases, 1):
                md += f"{i}. {uc}\n"
            md += "\n</details>\n\n"
            
            # 5. 연관 서비스
            md += "## 5. 연관 서비스\n\n"
            md += "<details>\n"
            md += "<summary>연관 서비스 보기</summary>\n\n"
            for rs in su.related_services:
                md += f"- {rs}\n"
            md += "\n</details>\n\n"
            
            # 6. 공식 문서 링크
            md += "## 6. 공식 문서 링크\n\n"
            print(f"  🔗 Processing {len(su.official_links)} official links...")
            for i, link in enumerate(su.official_links):
                print(f"    Link {i+1} type: {type(link)}, value: {link}")
                # Handle both dict and object access
                if isinstance(link, dict):
                    link_name = link.get('name', '링크')
                    link_url = link.get('url', '#')
                else:
                    link_name = getattr(link, 'name', '링크')
                    link_url = getattr(link, 'url', '#')
                md += f"- [{link_name}]({link_url})\n"
            md += "\n"
            
            return md
            
        except Exception as e:
            print(f"❌ Error in format_markdown: {e}")
            import traceback
            traceback.print_exc()
            raise
