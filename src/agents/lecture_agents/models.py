"""Pydantic 모델 정의"""
from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class Infographic(BaseModel):
    """인포그래픽"""
    type: str = Field(description="mermaid 또는 svg")
    content: str = Field(description="다이어그램 코드 또는 SVG 코드")
    image_references: Optional[List[str]] = Field(description="참고 이미지 링크", default=None)


class ServiceUnderstanding(BaseModel):
    """서비스 이해 섹션"""
    background: str = Field(description="배경 정보")
    concepts: List[str] = Field(description="핵심 개념 리스트")
    advantages: List[str] = Field(description="장점 (최소 3개)")
    disadvantages: List[str] = Field(description="단점 (최소 2개)")
    use_cases: List[str] = Field(description="자주 사용되는 사례 (최소 3개)")
    related_services: List[str] = Field(description="연관 서비스")
    official_links: List[Dict[str, str]] = Field(description="공식 문서 링크")


class TroubleshootingScenario(BaseModel):
    """트러블슈팅 시나리오"""
    title: str
    description: str
    root_cause: str
    diagnosis_steps: List[str]
    resolution_steps: List[str]
    verification_steps: List[str]


class DeepDive(BaseModel):
    """Deep Dive 섹션"""
    scenarios: List[TroubleshootingScenario] = Field(description="최소 2개의 시나리오")


class HandsOnStep(BaseModel):
    """실습 단계"""
    step_number: int
    title: str
    objective: str
    commands: Optional[str] = None
    expected_output: Optional[str] = None
    verification: Optional[str] = None
    troubleshooting: Optional[List[str]] = None


class HandsOnLab(BaseModel):
    """실습 섹션"""
    title: str
    purpose: str
    learning_objectives: List[str]
    estimated_time: str
    difficulty: str
    prerequisites: List[str]
    setup_instructions: List[str]
    steps: List[HandsOnStep] = Field(description="최소 7개의 단계")
    completion_summary: str
    next_steps: Optional[List[str]] = None


class QuizQuestion(BaseModel):
    """퀴즈 질문"""
    question: str
    choices: List[str] = Field(description="4개의 선택지")
    answer: str
    explanation: str


class Quiz(BaseModel):
    """퀴즈 섹션"""
    questions: List[QuizQuestion] = Field(description="최소 5개의 질문")
