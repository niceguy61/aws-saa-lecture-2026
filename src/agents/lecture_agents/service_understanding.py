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
실제 현장 경험을 바탕으로 기술을 설명합니다.

## 🎯 작성 원칙

### ✅ 반드시 포함할 것:
1. **실무 경험 스토리**
   - "처음 이 기술을 접했을 때..." 형식
   - 구체적인 프로젝트 사례
   - 숫자 데이터 (시간, 비용, 성능 등)

2. **문제→해결 구조**
   - 기존에 어떤 문제가 있었나?
   - 이 기술이 어떻게 해결했나?
   - 실제 개선 효과 (Before/After)

3. **구체적인 예시**
   - 추상적 설명 금지
   - 실제 명령어, 코드, 설정 포함
   - "예를 들어" 자주 사용

### ❌ 절대 금지:
1. Wikipedia 스타일 정의
   - "~은 ~입니다" 형식 금지
   - "~의 특징은 다음과 같습니다" 금지

2. 추상적 형용사
   - "효율적인", "강력한", "편리한" 금지
   - 대신 구체적 수치나 예시 사용

3. 나열식 설명
   - 단순 특징 나열 금지
   - 각 항목마다 이유와 예시 포함

## 📋 작성 가이드

### background (배경 정보):
- 1인칭 시점으로 작성 ("제가 처음 접했을 때...")
- 이 기술이 왜 나왔는지 문제 상황부터 시작
- 실제 프로젝트 경험 포함
- 600-800자

예시 구조:
"2019년 우리 팀은 배포할 때마다 문제가 생겼습니다. 
개발자 로컬에서는 잘 되는데 서버에서는 안 되는 일이 반복됐죠.
알고 보니 Python 버전이 로컬은 3.9, 서버는 3.7이었습니다.
그때 Docker를 도입했고, 배포 시간이 2시간에서 10분으로 줄었습니다."

### concepts (핵심 개념):
- 각 개념마다 한 줄 설명 + 실무 예시
- 전문 용어는 한글(English) 병기
- 5-7개

예시:
"컨테이너(Container): 격리된 실행 환경. 마치 '가상의 컴퓨터'처럼 독립적으로 실행됨. 
예) 한 서버에서 Node.js 12와 Node.js 18을 동시에 돌릴 수 있음"

### advantages (장점):
- 각 장점마다 구체적 사례와 숫자 포함
- "왜 장점인가?" 설명 필수
- Before/After 비교
- **최소 3개 필수, 권장 5개**

❌ 나쁜 예:
"빠른 속도"

✅ 좋은 예:
"배포 속도 12배 향상: VM은 부팅에 3분 소요 → Docker는 15초. 
하루 20번 배포하면 1시간 절약"

### disadvantages (단점):
- 실제 겪은 문제와 해결/우회 방법
- "언제 주의해야 하나?" 포함
- **최소 2개 필수, 권장 3-4개**

✅ 좋은 예:
"초기 학습 곡선: Dockerfile, Volume, Network 개념 이해하는데 
신입은 1-2주 소요. 하지만 한번 익히면 반복 작업 자동화 가능"

### use_cases (사용 사례):
- 실제 프로젝트 기반
- 구체적인 회사/서비스 예시 (익명화)
- "어떤 문제를 어떻게 해결했는지" 스토리
- **최소 3개 필수, 권장 5개**

✅ 좋은 예:
"스타트업 A사: 개발 환경 통일 문제 해결
- 문제: 신입 온보딩에 3일 소요 (환경 설정 실패 반복)
- 해결: docker-compose.yml 하나로 5분 셋업
- 효과: 온보딩 시간 95% 단축"

### related_services (연관 서비스):
- 이 기술과 함께 쓰는 도구들
- 각 서비스마다 관계 설명
- 3-5개

예시:
"Kubernetes: Docker 컨테이너를 여러 서버에서 자동 관리. 
Docker가 '컨테이너 만들기'라면 K8s는 '컨테이너 운영하기'"

### official_links (공식 문서):
- 난이도별 분류 (초급/중급/고급)
- 각 링크마다 짧은 설명
- 한글 자료 우선
- 5-10개

구조:
[
  {{"name": "Docker 시작하기 (공식, 30분) - 초급", "url": "https://..."}},
  {{"name": "Dockerfile 작성법 (한글) - 중급", "url": "https://..."}},
  {{"name": "Production 배포 가이드 - 고급", "url": "https://..."}}
]

## 🎨 톤앤매너

- 대화체 사용 ("~습니다", "~죠")
- 1인칭 시점 ("제가", "우리 팀")
- 적절한 이모지 사용 가능
- 친근하지만 전문적인 느낌

JSON 형식으로 응답하세요."""),
        
        ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

## 📖 Few-shot Examples

### ❌ BAD Example (AI 티나는 작성):
{{
  "background": "Docker는 컨테이너 기반의 오픈소스 가상화 플랫폼입니다. 애플리케이션을 컨테이너로 패키징하여 어디서나 동일하게 실행할 수 있습니다.",
  "advantages": [
    "빠른 실행 속도",
    "효율적인 자원 사용",
    "뛰어난 이식성"
  ]
}}

→ 이건 Wikipedia입니다. ❌

---

### ✅ GOOD Example (강사가 쓴 것 같은 작성):
{{
  "background": "2018년 우리 회사에 Docker를 도입하기 전 이야기입니다. 신입 개발자가 입사하면 로컬 개발 환경 설정에 2-3일이 걸렸습니다. Python, Node.js, MySQL... 하나씩 설치하다 보면 버전 충돌로 에러가 계속 났죠.\\n\\n특히 기억에 남는 건 'works on my machine' 문제였습니다. 개발자 로컬에서는 완벽히 돌아가는데 스테이징 서버에 배포하면 안 되는 거예요. 알고 보니 로컬은 Python 3.9, 서버는 3.7이었습니다.\\n\\nDocker를 도입한 뒤 이 모든 게 해결됐습니다. 신입은 'docker-compose up' 한 줄로 5분 만에 환경 구성 완료. 배포 에러는 80% 감소했고, 배포 시간도 2시간에서 15분으로 줄었습니다.",
  
  "concepts": [
    "컨테이너(Container): 애플리케이션을 '택배 상자'처럼 포장한 것. 코드, 라이브러리, 설정 파일이 모두 들어있어 어디서든 똑같이 실행됨. 예) 내 맥북에서 만든 컨테이너를 AWS 서버에 그대로 올려도 작동",
    "이미지(Image): 컨테이너의 '설계도'. 한 번 만들면 계속 재사용 가능. 예) Python 3.9 + FastAPI + PostgreSQL 조합을 이미지로 만들어두면, 팀원 10명이 똑같은 환경 사용",
    "볼륨(Volume): 컨테이너가 삭제돼도 데이터를 보존하는 저장소. 예) 데이터베이스 파일은 볼륨에 저장해야 컨테이너 재시작해도 안전",
    "Docker Hub: 이미지를 공유하는 'GitHub 같은 곳'. 공식 이미지들이 있어 바로 가져다 쓸 수 있음. 예) nginx, redis, postgres 이미지를 무료로 다운로드"
  ],
  
  "advantages": [
    "온보딩 시간 95% 단축: 기존 3일 → 5분으로 개선\\n- Before: 신입이 Python, MySQL, Redis 각각 설치하며 버전 충돌로 고생\\n- After: docker-compose up 한 줄로 완료\\n- 효과: 신입이 첫날부터 개발 가능",
    
    "배포 속도 12배 향상: 2시간 → 10분\\n- Before: 서버에 SSH 접속해서 git pull, pip install, service restart... 수동 작업\\n- After: docker push → docker pull → docker run 자동화\\n- 효과: 하루 5번 배포 가능 (기존 1번)",
    
    "'내 컴퓨터에선 되는데' 문제 80% 해소\\n- Before: 로컬(Mac) vs 서버(Linux) 환경 차이로 배포 실패 반복\\n- After: Dockerfile로 환경 동일하게 고정\\n- 실제 케이스: Python 버전 차이로 인한 에러 0건 (6개월간)"
  ],
  
  "disadvantages": [
    "초기 학습 곡선 존재: Dockerfile, Volume, Network 개념 이해하는데 신입 기준 1-2주 소요\\n- 해결: 사내 템플릿 제공 + 가이드 문서로 1주일로 단축\\n- 팁: docker-compose.yml 예제부터 시작하면 쉬움",
    
    "Windows/Mac에서 성능 이슈: Linux가 아니면 가상화 레이어 거쳐서 느림\\n- 실측: Mac M1에서 일부 이미지 빌드 시간 2배\\n- 해결: ARM64 네이티브 이미지 사용하거나 Linux 서버에서 빌드"
  ],
  
  "use_cases": [
    "스타트업 B사: 마이크로서비스 아키텍처 구축\\n- 상황: API 서버 5개를 각각 다른 언어로 개발 (Node.js, Python, Go)\\n- 도입: 각 서비스를 독립 컨테이너로 분리\\n- 결과: 한 서비스 장애가 다른 서비스에 영향 안 줌, 배포 독립적으로 가능",
    
    "대기업 C사: 레거시 시스템 모던화\\n- 상황: 10년 된 Java 7 앱을 Java 17로 업그레이드 불가 (의존성 복잡)\\n- 도입: 기존 앱은 Java 7 컨테이너, 신규 기능은 Java 17 컨테이너\\n- 결과: 점진적 마이그레이션 가능, 시스템 중단 없음"
  ],
  
  "official_links": [
    {{{{"name": "Docker 공식 튜토리얼 (영문, 30분) - 초급 추천", "url": "https://docs.docker.com/get-started/"}}}},
    {{{{"name": "44BITS 기술 블로그 - Docker 기초 (한글) - 초급", "url": "https://www.44bits.io/ko/keyword/docker"}}}},
    {{{{"name": "Dockerfile Best Practices (영문) - 중급", "url": "https://docs.docker.com/develop/develop-images/dockerfile_best_practices/"}}}},
    {{{{"name": "Docker Compose 완벽 가이드 (한글) - 중급", "url": "https://docs.docker.com/compose/"}}}}
  ]
}}

---

## 🎯 이제 {service_name}에 대해 위 GOOD Example 스타일로 작성하세요.

**체크리스트:**
- [ ] background에 실제 프로젝트 경험 포함
- [ ] 구체적 숫자 3개 이상 (시간, 비용, 성능 등)
- [ ] "~입니다" 정의 스타일 사용 안 함
- [ ] **advantages 최소 3개 이상** (각 장점마다 Before/After 있음)
- [ ] **disadvantages 최소 2개 이상** (단점에 해결 방법 포함)
- [ ] **use_cases 최소 3개 이상** (구체적 회사/상황 명시)
- [ ] 공식 링크에 난이도 표시

**CRITICAL: advantages 3개 이상, disadvantages 2개 이상, use_cases 3개 이상 필수!**

다음 JSON 스키마로 응답하세요:
{{
  "background": "배경 정보 (600-800자, 실무 경험 스토리)",
  "concepts": ["개념1: 설명 + 예시", "개념2: 설명 + 예시", ...],
  "advantages": [
    "장점1: 구체적 효과\\n- Before: ...\\n- After: ...\\n- 효과: ...",
    "장점2: ...",
    "장점3: ...",
    "... (최소 3개 필수)"
  ],
  "disadvantages": [
    "단점1: 문제 상황\\n- 해결: ...\\n- 팁: ...",
    "단점2: ...",
    "... (최소 2개 필수)"
  ],
  "use_cases": [
    "회사 A: 상황\\n- 상황: ...\\n- 도입: ...\\n- 결과: ...",
    "회사 B: ...",
    "회사 C: ...",
    "... (최소 3개 필수)"
  ],
  "related_services": ["서비스1: 관계 설명", ...],
  "official_links": [
    {{{{"name": "링크명 (설명) - 난이도", "url": "https://..."}}}}
  ]
}}""")
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
