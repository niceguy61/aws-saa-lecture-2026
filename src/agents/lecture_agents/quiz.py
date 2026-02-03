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
        logger.info(f"🔍 DEBUG: Data keys: {data.keys() if isinstance(data, dict) else 'NOT A DICT'}")
        if "questions" in data:
            logger.info(f"🔍 DEBUG: Questions type: {type(data['questions'])}")
            logger.info(f"🔍 DEBUG: Questions length: {len(data['questions']) if isinstance(data['questions'], (list, dict)) else 'N/A'}")
            if isinstance(data['questions'], list) and len(data['questions']) > 0:
                logger.info(f"🔍 DEBUG: First question sample: {data['questions'][0]}")
        
        # Validate questions field exists
        if "questions" not in data:
            raise ValueError("Missing required field: questions")
        
        # Validate and fix questions structure
        if isinstance(data["questions"], dict):
            questions_list = []
            for key, value in data["questions"].items():
                if isinstance(value, dict) and "question" in value:
                    questions_list.append(value)
                elif isinstance(value, str):
                    continue
            data["questions"] = questions_list
        
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
            raise ValueError(f"Only {len(data['questions'])} questions generated, need at least {min_questions}")
        
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

반드시 다음 규칙을 따르세요:
1. 모든 내용은 한글로 작성
2. 최소 {min_questions}개의 질문 (더 많이 생성 권장)
3. 각 질문은 정확히 4개의 선택지
4. 모든 질문에 상세한 설명 포함
5. 다양한 유형 (지식, 시나리오, 명령어, 비교)

CRITICAL: 
- questions는 반드시 배열(array)이어야 합니다!
- 최소 {min_questions}개 이상 생성하세요!
- 각 질문은 question, choices, answer, explanation 필드 필수!

JSON 형식으로 응답하세요."""),
            ("user", """서비스: {service_name}

RAG 컨텍스트:
{rag_context}

다음 JSON 스키마로 정확히 응답하세요:

{{
  "questions": [
    {{
      "question": "Dockerfile에서 COPY와 ADD 명령어의 차이점은 무엇인가요?",
      "choices": [
        "A) COPY는 로컬 파일만, ADD는 URL도 가능",
        "B) 차이 없음",
        "C) ADD가 더 빠름",
        "D) COPY가 더 안전함"
      ],
      "answer": "A",
      "explanation": "COPY는 로컬 파일 시스템의 파일만 복사할 수 있지만, ADD는 URL에서 파일을 다운로드하거나 tar 파일을 자동으로 압축 해제할 수 있습니다. 하지만 보안상 COPY 사용이 권장됩니다."
    }},
    {{
      "question": "다음 중 Docker 이미지 크기를 줄이는 방법이 아닌 것은?",
      "choices": [
        "A) 멀티 스테이지 빌드 사용",
        "B) Alpine 베이스 이미지 사용",
        "C) 모든 RUN 명령을 하나로 합치기",
        "D) 모든 파일을 한 번에 COPY"
      ],
      "answer": "D",
      "explanation": "모든 파일을 한 번에 COPY하면 불필요한 파일까지 포함되어 이미지 크기가 커집니다. .dockerignore를 사용하여 필요한 파일만 복사해야 합니다."
    }},
    {{
      "question": "컨테이너가 exit code 137로 종료되었습니다. 가장 가능성 높은 원인은?",
      "choices": [
        "A) 애플리케이션 버그",
        "B) 메모리 부족 (OOM)",
        "C) 디스크 공간 부족",
        "D) 네트워크 오류"
      ],
      "answer": "B",
      "explanation": "Exit code 137은 SIGKILL(128+9)을 의미하며, 일반적으로 메모리 부족으로 시스템이 컨테이너를 강제 종료했을 때 발생합니다."
    }}
  ]
}}

위 예시처럼 최소 """ + str(min_questions) + """개 이상의 질문을 배열 형태로 생성하세요.
각 질문은 question, choices(4개), answer, explanation을 모두 포함해야 합니다.""")
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
