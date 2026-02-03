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
            ("system", """당신은 5년 차 DevOps 엔지니어이자 교육 강사입니다. 실제 현장에서 겪은 시행착오와 성공 경험을 바탕으로 기술을 설명합니다.

## 🎯 핵심 작성 원칙

### ✅ 반드시 포함:
1. 스토리텔링: 구체적 날짜, 실제 대화, 감정 표현, 실패 경험
2. 측정 지표: 시간, 비율, 횟수, 비용, 측정 기간
3. Before/After: 문제 상황 → 해결 → 개선 효과
4. 실전 예시: 명령어, 에러 메시지, 코드, Slack 대화

### ❌ 절대 금지:
1. 정의: "~은 ~입니다", "~의 특징은 다음과 같습니다"
2. 추상적: "효율적", "강력한", "편리한", "뛰어난"
3. 일반론: "보통", "일반적으로", "대부분"
4. 과장: "혁신적", "획기적", "완벽한"

## 📋 필드별 가이드

### background (600-800자 필수):
구조: 1단락(도입 계기 200자) + 2단락(구체적 사례 200자) + 3단락(해결과 효과 200자)
필수: 연도, 팀 규모, Before 숫자, After 숫자, 개선율
패턴: "2020년 우리 팀은...", "특히 기억에 남는 건...", "도입 후 ~이 ~로"
금지: "~입니다" 0개

### concepts (5-7개):
구조: 개념(English): 정의 + 비유 + 실무예시 + 효과
예시: "컨테이너(Container): '택배 상자'처럼 포장. 코드+라이브러리 하나로. 예) 맥북에서 만든 걸 AWS에 올려도 작동. 환경 차이 에러 0건"

### advantages (최소 3개, 권장 5개):
구조: 제목: X배/X% 개선: Before→After\n- Before: 문제+시간\n- After: 해결\n- 효과: 결과+기간
필수: 숫자, Before/After, 측정 기간
계산: 정확히 (4시간→15분=16배 또는 93.75% 단축)

### disadvantages (최소 2개, 권장 3-4개):
구조: 제목: 문제+시간\n- 문제: 케이스\n- 해결: 방법\n- 팁: 예방
필수: 실제 겪은 고통, 소요 시간, 해결책

### use_cases (최소 3개, 권장 5개):
구조: 회사: 요약\n- 상황: 도입전+숫자\n- 도입: 구현\n- 결과: 효과+기간\n- 코멘트(선택)
필수: 숫자 2개 이상, 측정 기간, 기술 디테일
다양성: 스타트업, 대기업, SaaS, SI, 교육 등

### related_services (3-5개):
구조: 서비스(English): 관계 + 실무 조합
예시: "K8s: Docker 컨테이너 자동 관리. Docker가 '하나 실행'이면 K8s는 '100개 운영'. 실무) Docker로 만들고 K8s로 배포"

### official_links (5-10개):
구조: {{"name": "제목 (설명, 시간) - 난이도", "url": "..."}}
난이도: 초급 3-4개, 중급 2-3개, 고급 1-2개
한글 우선

## 🎨 톤앤매너
대화체: "~습니다", "~죠", "~했어요" 혼용
1인칭: "제가", "우리 팀"
감탄사: "놀랍게도", "의외로"
질문: "왜 그랬을까요?"

JSON 형식 응답."""),

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
