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
    
    def generate(self, service_name: str, rag_context: str) -> ServiceUnderstanding:
        """서비스 이해 섹션 생성"""
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 DevOps 교육 전문가입니다.
주어진 서비스에 대한 서비스 이해 섹션을 생성하세요.

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 기술 용어는 한글(English) 형식으로 첫 사용 시 표기
3. 장점 최소 3개, 단점 최소 2개
4. 사용 사례 최소 3개
5. Mermaid 다이어그램 포함
6. 공식 문서 링크 포함

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 응답하세요:
{{
  "background": "배경 정보 (한글)",
  "concepts": ["개념1", "개념2", ...],
  "advantages": ["장점1", "장점2", "장점3", ...],
  "disadvantages": ["단점1", "단점2", ...],
  "use_cases": ["사례1", "사례2", "사례3", ...],
  "related_services": ["서비스1", "서비스2", ...],
  "official_links": [
    {{"name": "링크명", "url": "https://..."}}
  ]
}}""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "rag_context": rag_context[:8000]
        })
        
        try:
            data = json.loads(response.content)
            
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
        except Exception as e:
            print(f"❌ Service Understanding generation error: {e}")
            print(f"Response content: {response.content[:500]}")
            raise
    
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
