"""인포그래픽 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import Infographic


class InfographicAgent:
    """인포그래픽 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
    
    def generate(
        self, 
        service_name: str, 
        context: str, 
        section_type: str,
        rag_context: str
    ) -> Infographic:
        """인포그래픽 생성
        
        Args:
            service_name: 서비스 이름
            context: 섹션 내용 (배경정보, 핵심개념 등)
            section_type: 섹션 타입 (background, concepts, troubleshooting, hands_on)
            rag_context: ChromaDB에서 가져온 문서 (이미지 링크 포함)
        """
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """당신은 기술 문서 시각화 전문가입니다.
주어진 내용을 Mermaid 다이어그램으로 시각화하세요.

## 📊 다이어그램 타입 선택 가이드

### 1. Timeline (시간 흐름) - background에 최적
**언제 사용:** 역사, 발전 과정, 버전 변화
```mermaid
timeline
    title Docker 발전 역사
    2013 : Docker 0.1 출시
         : dotCloud 사내 프로젝트
    2014 : Docker 1.0 GA
         : Docker Hub 런칭
    2015 : 기업 도입 폭발
         : Kubernetes 등장
```

### 2. Graph TD/LR (관계도) - concepts에 최적
**언제 사용:** 시스템 구조, 컴포넌트 관계
```mermaid
graph TD
    Client[클라이언트] -->|HTTP 요청| LB[로드밸런서]
    LB -->|분산| Server1[서버 1]
    LB -->|분산| Server2[서버 2]
    Server1 --> DB[(데이터베이스)]
    Server2 --> DB
    
    classDef primary fill:#667eea,color:#fff,stroke:#764ba2
    classDef storage fill:#ffd43b,color:#000,stroke:#f59f00
    Client:::primary
    LB:::primary
    DB:::storage
```

**노드 모양:**
- `[텍스트]` 사각형
- `(텍스트)` 둥근 사각형
- `([텍스트])` 스타디움형
- `[(텍스트)]` 원통형 (DB)
- `{{{{텍스트}}}}` 육각형
- `{{텍스트}}` 마름모

### 3. Flowchart (흐름도) - troubleshooting, hands_on에 최적
**언제 사용:** 프로세스, 의사결정, 알고리즘
```mermaid
flowchart TD
    Start([시작]) --> CheckPort{{포트 사용<br/>가능?}}
    CheckPort -->|Yes| RunContainer[실행]
    CheckPort -->|No| FindProcess[프로세스 확인]
    FindProcess --> Decision{{중요한<br/>프로세스?}}
    Decision -->|Yes| UseOtherPort[다른 포트]
    Decision -->|No| KillProcess[종료]
    KillProcess --> RunContainer
    
    style Start fill:#51cf66,color:#fff
    style CheckPort fill:#ffd43b,color:#000
```

### 4. Mindmap (마인드맵) - concepts 대안
**언제 사용:** 개념 분류, 기능 계층
```mermaid
mindmap
  root((Docker<br/>플랫폼))
    컨테이너
      격리 환경
      경량화
    이미지
      Layer 구조
      Registry
    네트워킹
      Bridge
      Host
```

### 5. Sequence Diagram (시퀀스) - API 흐름
**언제 사용:** 시스템 간 통신, 상호작용
```mermaid
sequenceDiagram
    actor User as 사용자
    participant App as 앱
    participant API as API 서버
    
    User->>App: 로그인 요청
    App->>API: POST /api/login
    API-->>App: 200 OK
    App-->>User: 로그인 성공
```

## 🎨 스타일링

### 색상 팔레트:
```
Primary (주요):     fill:#667eea,color:#fff,stroke:#764ba2
Success (성공):     fill:#51cf66,color:#fff,stroke:#37b24d
Warning (경고):     fill:#ffd43b,color:#000,stroke:#f59f00
Error (에러):       fill:#ff6b6b,color:#fff,stroke:#f03e3e
Storage (저장소):   fill:#868e96,color:#fff,stroke:#495057
```

## ⚠️ CRITICAL 규칙

### 예약어 금지 (노드 ID):
❌ 사용 금지: `start`, `end`, `default`, `class`, `style`, `graph`, `subgraph`, `click`, `call`, `classDef`

✅ 대신 사용:
- `Start`, `End`, `Begin`, `Finish`
- `Step1`, `Step2`, `Step3`
- `Check`, `Decision`, `Action`
- `Process1`, `Process2`

### 문법 규칙:
1. **괄호 균형**: `[`, `]`, `(`, `)`, `{{`, `}}` 개수 일치
2. **줄바꿈**: 노드 내 `<br/>` 사용
3. **화살표 일관성**: `-->` 또는 `->>` (공백 주의)
4. **한글 사용**: 모든 레이블은 한글
5. **간결함**: 노드 5-15개 권장

## 📋 섹션별 추천

| 섹션 | 1순위 | 2순위 | 3순위 |
|------|-------|-------|-------|
| background | timeline | flowchart | graph |
| concepts | graph | mindmap | - |
| troubleshooting | flowchart | sequence | graph |
| hands_on | flowchart | graph | sequence |

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}
섹션 타입: {section_type}

섹션 내용:
{context}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 응답:
{{
  "type": "mermaid",
  "content": "```mermaid\\ngraph TD\\n  Client[클라이언트] --> Server[서버]\\n  style Client fill:#667eea,color:#fff\\n```",
  "image_references": []
}}

**체크리스트:**
- [ ] 섹션 타입에 맞는 다이어그램 선택
- [ ] 노드 ID는 대문자 시작 (Start, Step1...)
- [ ] 한글 레이블
- [ ] 스타일 적용 (primary, success...)
- [ ] 5-15개 노드
- [ ] caption 작성

**금지:** start, end, class, style 등 예약어""")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "service_name": service_name,
            "section_type": section_type,
            "context": context[:2000],
            "rag_context": rag_context[:4000]
        })
        
        try:
            data = json.loads(response.content)
            
            # Fix Mermaid reserved keywords
            if data.get("type") == "mermaid" and "content" in data:
                data["content"] = self._fix_mermaid_reserved_keywords(data["content"])
            
            return Infographic(**data)
        except Exception as e:
            print(f"❌ Infographic generation error: {e}")
            print(f"Response content: {response.content[:500]}")
            # Return default infographic on error
            return Infographic(
                type="mermaid",
                content="```mermaid\ngraph LR\n  Start[시작] --> Progress[진행중]\n  Progress --> End[완료]\n```",
                image_references=None
            )
    
    def _fix_mermaid_reserved_keywords(self, content: str) -> str:
        """
        Fix Mermaid reserved keywords with better validation
        
        Mermaid reserved keywords that cause parsing errors:
        - start, end, default, class, style, graph, subgraph, click, call
        """
        import re
        
        # 1. Extract all node IDs from the diagram
        node_pattern = r'(\w+)[\[\(\{]'
        nodes = re.findall(node_pattern, content)
        
        # 2. Mermaid reserved keywords
        reserved = {
            'start', 'end', 'default', 'class', 'style', 
            'graph', 'subgraph', 'click', 'call', 'classDef'
        }
        
        # 3. Create replacement mapping
        replacements = {}
        for node in set(nodes):
            if node.lower() in reserved:
                # Capitalize or add prefix
                new_node = node.capitalize() if node.islower() else f"Node_{node}"
                replacements[node] = new_node
                print(f"  🔧 Replacing reserved keyword: {node} → {new_node}")
        
        # 4. Apply replacements (whole word only)
        for old, new in replacements.items():
            # Replace in node definitions
            content = re.sub(
                rf'\b{old}\b(?=[\[\(\{{])',
                new,
                content
            )
            # Replace in connections
            content = re.sub(
                rf'(?<=-->)\s*\b{old}\b',
                f' {new}',
                content
            )
            # Replace in references
            content = re.sub(
                rf'(?<=\s)\b{old}\b(?=\s)',
                new,
                content
            )
        
        # 5. Validate Mermaid syntax (basic)
        if not self._validate_mermaid_syntax(content):
            print("  ⚠️ Mermaid syntax validation failed, using fallback")
            return self._get_fallback_diagram()
        
        return content
    
    def _validate_mermaid_syntax(self, content: str) -> bool:
        """Basic Mermaid syntax validation"""
        try:
            # Remove code fence markers if present
            content_clean = content.replace('```mermaid', '').replace('```', '').strip()
            
            # Check for basic structure - must have at least one diagram type
            diagram_types = ['graph', 'flowchart', 'sequenceDiagram', 'timeline', 'mindmap']
            has_diagram_type = any(dtype in content_clean.lower() for dtype in diagram_types)
            if not has_diagram_type:
                print("  ⚠️ No diagram type found")
                return False
            
            # Check for balanced brackets (but allow some flexibility)
            bracket_pairs = [
                ('[', ']'),
                ('(', ')'),
                ('{', '}')
            ]
            
            for open_b, close_b in bracket_pairs:
                open_count = content_clean.count(open_b)
                close_count = content_clean.count(close_b)
                # Allow small imbalance (might be in strings or comments)
                if abs(open_count - close_count) > 2:
                    print(f"  ⚠️ Bracket imbalance: {open_b}{close_b} ({open_count} vs {close_count})")
                    return False
            
            # Check for connections (arrows) - but not required for all diagram types
            has_connections = any(arrow in content_clean for arrow in ['-->', '---', '->>', '->>'])
            
            # Timeline and mindmap don't need arrows
            if 'timeline' not in content_clean.lower() and 'mindmap' not in content_clean.lower():
                if not has_connections:
                    print("  ⚠️ No connections found")
                    return False
            
            # Check minimum content length
            if len(content_clean) < 20:
                print("  ⚠️ Content too short")
                return False
            
            return True
        except Exception as e:
            print(f"  ⚠️ Validation error: {e}")
            return False
    
    def _get_fallback_diagram(self) -> str:
        """Fallback diagram when generation fails"""
        return """```mermaid
graph LR
    A[시작] --> B[진행]
    B --> C[완료]
    
    style A fill:#e1f5ff
    style B fill:#fff3e0
    style C fill:#e8f5e9
```"""
    
    def format_markdown(self, infographic: Infographic) -> str:
        """Format infographic as markdown"""
        md = ""
        
        # Add diagram
        if infographic.type == "mermaid":
            md += f"{infographic.content}\n\n"
        elif infographic.type == "svg":
            md += f"{infographic.content}\n\n"
        
        # Add image references if available
        if infographic.image_references:
            md += "**참고 이미지**:\n"
            for img_url in infographic.image_references:
                md += f"- [이미지 보기]({img_url})\n"
            md += "\n"
        
        return md
