"""Quiz 생성 에이전트"""
import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from src.vectorstore import VectorStoreManager
from .models import Quiz


class QuizAgent:
    """Quiz 생성 에이전트"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.7,
            format="json"
        )
        self.vectorstore = VectorStoreManager()
        
        # Import config values
        from src.config import MIN_QUIZ_QUESTIONS, MIN_QUIZ_QUESTIONS_MULTI_SERVICE
        self.min_questions = MIN_QUIZ_QUESTIONS
        self.min_questions_multi = MIN_QUIZ_QUESTIONS_MULTI_SERVICE
    
    def _validate_quiz(self, data: dict, min_questions: int) -> Quiz:
        """Validate and fix quiz data structure"""
        
        # DEBUG: Log what we received
        import logging
        logger = logging.getLogger("QuizAgent")
        logger.info(f"🔍 DEBUG: Received data type: {type(data)}")
        logger.info(f"🔍 DEBUG: Data keys: {list(data.keys()) if isinstance(data, dict) else 'NOT A DICT'}")
        
        # Validate questions field exists
        if "questions" not in data:
            raise ValueError("Missing required field: questions")
        
        logger.info(f"🔍 DEBUG: Questions type: {type(data['questions'])}")
        logger.info(f"🔍 DEBUG: Questions length: {len(data['questions']) if isinstance(data['questions'], (list, dict)) else 'N/A'}")
        
        # Validate and fix questions structure
        if isinstance(data["questions"], dict):
            logger.warning("⚠️  Questions is a dict, converting to list...")
            questions_list = []
            for key, value in data["questions"].items():
                if isinstance(value, dict) and "question" in value:
                    questions_list.append(value)
                    logger.info(f"  ✓ Added question from key '{key}'")
                elif isinstance(value, str):
                    logger.warning(f"  ✗ Skipped string value for key '{key}'")
                    continue
                else:
                    logger.warning(f"  ✗ Skipped invalid value for key '{key}': {type(value)}")
            data["questions"] = questions_list
            logger.info(f"  → Converted to list with {len(questions_list)} questions")
        
        if not isinstance(data["questions"], list):
            raise ValueError(f"questions must be a list, got {type(data['questions'])}")
        
        if len(data["questions"]) > 0:
            logger.info(f"🔍 DEBUG: First question sample: {data['questions'][0]}")
        
        # Validate each question has required fields
        valid_questions = []
        invalid_questions = []
        required_question_fields = ["question", "choices", "answer", "explanation"]
        
        for i, q in enumerate(data["questions"], 1):
            if not isinstance(q, dict):
                invalid_questions.append(f"Question {i}: Not a dict, got {type(q)}")
                continue
                
            missing_fields = [f for f in required_question_fields if f not in q]
            if missing_fields:
                invalid_questions.append(f"Question {i}: Missing fields {missing_fields}")
                continue
            
            # Validate choices count
            choices = q.get("choices", [])
            if not isinstance(choices, list):
                invalid_questions.append(f"Question {i}: choices is not a list, got {type(choices)}")
                continue
                
            if len(choices) != 4:
                invalid_questions.append(f"Question {i}: Must have exactly 4 choices, got {len(choices)}")
                continue
            
            # Validate answer is one of A, B, C, D
            answer = q.get("answer", "").strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                invalid_questions.append(f"Question {i}: Answer must be A, B, C, or D, got '{answer}'")
                continue
            
            # Validate explanation length
            explanation = q.get("explanation", "")
            if len(explanation) < 50:
                invalid_questions.append(f"Question {i}: Explanation too short ({len(explanation)} chars, need 50+)")
                continue
                
            valid_questions.append(q)
        
        # Log validation results
        logger.info(f"✅ Valid questions: {len(valid_questions)}")
        if invalid_questions:
            logger.warning(f"⚠️  Invalid questions found:")
            for inv in invalid_questions:
                logger.warning(f"   - {inv}")
        
        data["questions"] = valid_questions
        
        # Validate minimum count
        if len(data["questions"]) < min_questions:
            raise ValueError(f"Only {len(data['questions'])} valid questions generated, need at least {min_questions}")
        
        if len(data["questions"]) == 0:
            raise ValueError("No valid questions generated")
        
        return Quiz(**data)
    
    def generate(self, service_name: str, rag_context: str, is_multi_service: bool = False) -> Quiz:
        """퀴즈 섹션 생성 with retry logic
        
        Args:
            service_name: 서비스 이름
            rag_context: RAG 컨텍스트
            is_multi_service: 멀티 서비스 여부 (True면 더 많은 질문 생성)
        """
        
        # Determine minimum questions based on service count
        min_questions = self.min_questions_multi if is_multi_service else self.min_questions
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"""당신은 DevOps 평가 전문가입니다.
주어진 서비스에 대한 퀴즈를 생성하세요.

## 🎯 필수 규칙

1. **JSON 구조 (엄격히 준수)**:
   - 최상위 키: "questions" (배열)
   - 각 질문은 객체 {{"question": "...", "choices": [...], "answer": "...", "explanation": "..."}}
   - questions는 반드시 배열(array)이어야 합니다!

2. **질문 개수**: 최소 {min_questions}개 (더 많이 생성 권장)

3. **각 질문 필수 필드**:
   - question: 질문 텍스트 (한글)
   - choices: 정확히 4개의 선택지 배열 ["A) ...", "B) ...", "C) ...", "D) ..."]
   - answer: 정답 (A, B, C, D 중 하나)
   - explanation: 상세한 설명 (한글, 100자 이상)

4. **질문 유형 다양화**:
   - 지식 확인 (개념, 용어)
   - 시나리오 기반 (문제 해결)
   - 명령어/설정 (실무)
   - 비교/분석 (장단점)

CRITICAL WARNING:
- questions를 객체(object)로 만들지 마세요!
- questions는 반드시 배열(array)이어야 합니다!
- 예: {{"questions": [{{}}, {{}}, {{}}]}} ✅
- 예: {{"questions": {{"q1": {{}}, "q2": {{}}}}}} ❌

JSON 형식으로만 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

## 📋 응답 형식 (정확히 따르세요)

```json
{{
  "questions": [
    {{
      "question": "Docker 컨테이너와 가상 머신의 가장 큰 차이점은 무엇인가요?",
      "choices": [
        "A) 컨테이너는 OS 커널을 공유하지만, VM은 각자 OS를 가짐",
        "B) 컨테이너가 VM보다 항상 느림",
        "C) VM은 격리가 안 되지만 컨테이너는 완전 격리",
        "D) 차이가 없음"
      ],
      "answer": "A",
      "explanation": "Docker 컨테이너는 호스트 OS의 커널을 공유하여 가볍고 빠르게 시작됩니다. 반면 가상 머신은 각각 독립적인 OS를 실행하므로 더 무겁지만 완전한 격리를 제공합니다. 컨테이너는 프로세스 수준 격리, VM은 하드웨어 수준 격리입니다."
    }},
    {{
      "question": "Dockerfile에서 COPY와 ADD 명령어의 차이점은 무엇인가요?",
      "choices": [
        "A) COPY는 로컬 파일만, ADD는 URL과 tar 자동 압축 해제 가능",
        "B) 차이 없음, 동일한 기능",
        "C) ADD가 더 빠르고 효율적",
        "D) COPY만 보안 검사를 수행"
      ],
      "answer": "A",
      "explanation": "COPY는 로컬 파일 시스템의 파일만 복사할 수 있습니다. ADD는 URL에서 파일을 다운로드하거나 tar 파일을 자동으로 압축 해제할 수 있습니다. 하지만 예측 가능성과 보안을 위해 COPY 사용이 권장됩니다. ADD는 특별한 경우에만 사용하세요."
    }},
    {{
      "question": "다음 중 Docker 이미지 크기를 줄이는 방법이 아닌 것은?",
      "choices": [
        "A) 멀티 스테이지 빌드 사용",
        "B) Alpine 베이스 이미지 사용",
        "C) 모든 RUN 명령을 하나로 합치기",
        "D) 모든 파일을 한 번에 COPY하기"
      ],
      "answer": "D",
      "explanation": "모든 파일을 한 번에 COPY하면 불필요한 파일(node_modules, .git, 테스트 파일 등)까지 포함되어 이미지 크기가 커집니다. .dockerignore 파일을 사용하여 필요한 파일만 선택적으로 복사해야 합니다. 멀티 스테이지 빌드, Alpine 이미지, RUN 명령 최적화는 모두 크기 감소에 효과적입니다."
    }},
    {{
      "question": "프로덕션 환경에서 컨테이너가 exit code 137로 종료되었습니다. 가장 가능성 높은 원인은?",
      "choices": [
        "A) 애플리케이션 코드 버그",
        "B) 메모리 부족 (OOM Killer)",
        "C) 디스크 공간 부족",
        "D) 네트워크 연결 끊김"
      ],
      "answer": "B",
      "explanation": "Exit code 137은 SIGKILL(128+9)을 의미하며, 일반적으로 컨테이너가 메모리 제한을 초과하여 OOM(Out Of Memory) Killer에 의해 강제 종료되었을 때 발생합니다. docker run --memory 옵션으로 메모리 제한을 확인하고, docker stats로 실제 사용량을 모니터링하여 적절히 조정해야 합니다."
    }},
    {{
      "question": "Docker Compose에서 depends_on 옵션의 한계점은 무엇인가요?",
      "choices": [
        "A) 서비스 시작 순서만 보장하고, 준비 상태는 보장하지 않음",
        "B) 모든 서비스가 완전히 준비될 때까지 대기함",
        "C) 네트워크 연결을 자동으로 확인함",
        "D) 데이터베이스 초기화를 자동으로 수행함"
      ],
      "answer": "A",
      "explanation": "depends_on은 컨테이너 시작 순서만 제어하며, 서비스가 실제로 준비되었는지(예: 데이터베이스가 연결을 받을 수 있는지)는 확인하지 않습니다. 프로덕션에서는 healthcheck와 restart 정책을 함께 사용하거나, 애플리케이션 코드에서 재시도 로직을 구현해야 합니다."
    }}
  ]
}}
```

## ✅ 체크리스트

- [ ] questions는 배열(array) 형태
- [ ] 최소 """ + str(min_questions) + """개 질문 생성
- [ ] 각 질문에 question, choices, answer, explanation 모두 포함
- [ ] choices는 정확히 4개 (A, B, C, D)
- [ ] explanation은 100자 이상 상세 설명
- [ ] 다양한 유형 (개념, 시나리오, 명령어, 비교)

위 형식을 정확히 따라 JSON으로만 응답하세요.""")
        ])
        
        chain = prompt | self.llm
        
        # Use retry logic from BaseAgent
        from src.agents.base_agent import BaseAgent
        base_agent = BaseAgent(
            name="QuizAgent",
            collection_name="",
            system_prompt=""
        )
        
        # Create validator with min_questions closure
        def validator(data):
            return self._validate_quiz(data, min_questions)
        
        return base_agent.generate_with_retry(
            chain=chain,
            input_dict={
                "service_name": service_name,
                "rag_context": rag_context[:8000]
            },
            validator_func=validator,
            error_context=f"Quiz for {service_name}"
        )
    
    def format_markdown(self, quiz: Quiz) -> str:
        """Format as markdown with <details> tags"""
        md = "# 퀴즈 (Quiz)\n\n"
        
        for i, q in enumerate(quiz.questions, 1):
            md += f"## 질문 {i}\n\n"
            md += f"**{q.question}**\n\n"
            
            for choice in q.choices:
                md += f"{choice}\n"
            md += "\n"
            
            md += "<details>\n"
            md += "<summary>정답 및 해설 보기</summary>\n\n"
            md += f"**답**: {q.answer}\n\n"
            md += f"**설명**: {q.explanation}\n\n"
            md += "</details>\n\n"
            md += "---\n\n"
        
        return md
