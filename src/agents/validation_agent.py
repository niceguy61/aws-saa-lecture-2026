"""강의 검증 Agent - 생성된 강의 자료의 품질을 검증"""
import re
from typing import Dict, List, Tuple
from pathlib import Path
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


class ValidationIssue(BaseModel):
    """검증 이슈"""
    severity: str = Field(description="critical, warning, info")
    category: str = Field(description="mermaid, content, structure, format")
    message: str = Field(description="이슈 설명")
    location: str = Field(description="파일명 또는 섹션")
    suggestion: str = Field(description="수정 제안")


class ValidationResult(BaseModel):
    """검증 결과"""
    is_valid: bool = Field(description="전체 검증 통과 여부")
    issues: List[ValidationIssue] = Field(description="발견된 이슈 목록")
    score: float = Field(description="품질 점수 (0-100)")
    summary: str = Field(description="검증 요약")


class LectureValidationAgent:
    """강의 검증 Agent"""
    
    def __init__(self, model_name: str = "qwen3:8b"):
        self.llm = ChatOllama(
            model=model_name,
            temperature=0.3,  # 검증은 일관성이 중요
            format="json"
        )
        
        # Import minimum requirements from config
        from src.config import (
            MIN_QUIZ_QUESTIONS,
            MIN_LAB_STEPS,
            MIN_ADVANTAGES,
            MIN_DISADVANTAGES,
            MIN_USE_CASES,
            MIN_TROUBLESHOOTING_SCENARIOS
        )
        
        # 검증 기준
        self.min_advantages = MIN_ADVANTAGES
        self.min_disadvantages = MIN_DISADVANTAGES
        self.min_use_cases = MIN_USE_CASES
        self.min_scenarios = MIN_TROUBLESHOOTING_SCENARIOS
        self.min_lab_steps = MIN_LAB_STEPS
        self.min_quiz_questions = MIN_QUIZ_QUESTIONS
        self.min_content_length = 1000  # 각 섹션 최소 글자 수
    
    def auto_fix_mermaid_backticks(self, lecture_dir: Path) -> int:
        """잘못된 Mermaid 백틱 자동 수정"""
        fixed_count = 0
        md_files = list(lecture_dir.glob("*.md"))
        
        print(f"🔧 Auto-fixing Mermaid backticks in {len(md_files)} files...")
        
        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                original_content = content
                
                # Fix opening backticks: any number of backticks (1-5+) + mermaid -> ```mermaid
                # `mermaid, ``mermaid, ````mermaid, `````mermaid -> ```mermaid
                content = re.sub(r'`{1,2}mermaid\s', r'```mermaid\n', content)
                content = re.sub(r'`{4,}mermaid\s', r'```mermaid\n', content)
                
                # Fix closing backticks: any number of backticks (1-2, 4-5+) -> ```
                # Match backticks at end of line or before newline
                content = re.sub(r'\n`{1,2}(?=\s*\n)', r'\n```', content)
                content = re.sub(r'\n`{4,}(?=\s*\n)', r'\n```', content)
                content = re.sub(r'\n`{1,2}\s*$', r'\n```', content, flags=re.MULTILINE)
                content = re.sub(r'\n`{4,}\s*$', r'\n```', content, flags=re.MULTILINE)
                
                if content != original_content:
                    md_file.write_text(content, encoding='utf-8')
                    fixed_count += 1
                    print(f"  ✓ Fixed: {md_file.name}")
            
            except Exception as e:
                print(f"  ⚠️ Failed to auto-fix {md_file.name}: {e}")
        
        if fixed_count > 0:
            print(f"✓ Auto-fixed {fixed_count} file(s)\n")
        else:
            print(f"✓ No fixes needed\n")
        
        return fixed_count
    
    def validate_lecture(
        self, 
        week: int, 
        day: int, 
        lecture_dir: Path
    ) -> ValidationResult:
        """전체 강의 검증"""
        
        print(f"\n{'='*80}")
        print(f"🔍 Validating Lecture: Week {week}, Day {day}")
        print(f"{'='*80}\n")
        
        # 0. Mermaid 백틱 자동 수정 (검증 전)
        print("🔧 Auto-fixing common issues...")
        fixed_count = self.auto_fix_mermaid_backticks(lecture_dir)
        
        issues = []
        
        # 1. 파일 존재 확인
        print("📁 Checking file existence...")
        file_issues = self._check_files_exist(lecture_dir)
        issues.extend(file_issues)
        
        # 2. Service Understanding 검증
        print("🎓 Validating Service Understanding...")
        su_path = lecture_dir / "service_understanding.md"
        if su_path.exists():
            su_issues = self._validate_service_understanding(su_path)
            issues.extend(su_issues)
        
        # 3. Deep Dive 검증
        print("🔍 Validating Deep Dive...")
        dd_path = lecture_dir / "deep_dive.md"
        if dd_path.exists():
            dd_issues = self._validate_deep_dive(dd_path)
            issues.extend(dd_issues)
        
        # 4. Hands-on Lab 검증
        print("🛠️ Validating Hands-on Lab...")
        lab_issues = self._validate_hands_on_lab(lecture_dir)
        issues.extend(lab_issues)
        
        # 5. Quiz 검증
        print("📝 Validating Quiz...")
        quiz_path = lecture_dir / "quiz.md"
        if quiz_path.exists():
            quiz_issues = self._validate_quiz(quiz_path)
            issues.extend(quiz_issues)
        
        # 6. Mermaid 다이어그램 검증
        print("📊 Validating Mermaid diagrams...")
        mermaid_issues = self._validate_all_mermaid(lecture_dir)
        issues.extend(mermaid_issues)
        
        # 점수 계산
        score = self._calculate_score(issues)
        
        # Critical 이슈가 있으면 실패
        critical_issues = [i for i in issues if i.severity == "critical"]
        is_valid = len(critical_issues) == 0 and score >= 70
        
        # 요약 생성
        summary = self._generate_summary(issues, score, is_valid)
        
        result = ValidationResult(
            is_valid=is_valid,
            issues=issues,
            score=score,
            summary=summary
        )
        
        self._print_validation_result(result)
        
        return result
    
    def _check_files_exist(self, lecture_dir: Path) -> List[ValidationIssue]:
        """필수 파일 존재 확인"""
        issues = []
        
        required_files = [
            "service_understanding.md",
            "deep_dive.md",
            "quiz.md"
        ]
        
        for filename in required_files:
            if not (lecture_dir / filename).exists():
                issues.append(ValidationIssue(
                    severity="critical",
                    category="structure",
                    message=f"필수 파일 누락: {filename}",
                    location=str(lecture_dir),
                    suggestion=f"{filename} 파일을 생성하세요"
                ))
        
        # Hands-on Lab 단계 확인 (최소 7개)
        lab_steps = list(lecture_dir.glob("handson_step*.md"))
        if len(lab_steps) < 7:
            issues.append(ValidationIssue(
                severity="critical",
                category="structure",
                message=f"실습 단계 부족: {len(lab_steps)}개 (최소 7개 필요)",
                location=str(lecture_dir),
                suggestion="최소 7개의 실습 단계를 생성하세요"
            ))
        
        return issues
    
    def _validate_service_understanding(self, file_path: Path) -> List[ValidationIssue]:
        """Service Understanding 섹션 검증"""
        issues = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # 최소 길이 확인
            if len(content) < self.min_content_length:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="content",
                    message=f"내용이 너무 짧습니다: {len(content)}자 (최소 {self.min_content_length}자)",
                    location="service_understanding.md",
                    suggestion="더 상세한 설명을 추가하세요"
                ))
            
            # 필수 섹션 확인
            required_sections = [
                "배경 정보",
                "핵심 개념",
                "장단점",
                "자주 사용되는 사례",
                "연관 서비스",
                "공식 문서 링크",
                "인포그래픽"
            ]
            
            for section in required_sections:
                if section not in content:
                    issues.append(ValidationIssue(
                        severity="critical",
                        category="structure",
                        message=f"필수 섹션 누락: {section}",
                        location="service_understanding.md",
                        suggestion=f"'{section}' 섹션을 추가하세요"
                    ))
            
            # 장점 개수 확인 (최소 3개)
            advantages_section = self._extract_section(content, "장점")
            if advantages_section:
                advantages_count = len(re.findall(r'^[-*]\s+', advantages_section, re.MULTILINE))
                if advantages_count < self.min_advantages:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="content",
                        message=f"장점이 부족합니다: {advantages_count}개 (최소 {self.min_advantages}개)",
                        location="service_understanding.md - 장점",
                        suggestion=f"최소 {self.min_advantages}개의 장점을 작성하세요"
                    ))
            
            # 단점 개수 확인 (최소 2개)
            disadvantages_section = self._extract_section(content, "단점")
            if disadvantages_section:
                disadvantages_count = len(re.findall(r'^[-*]\s+', disadvantages_section, re.MULTILINE))
                if disadvantages_count < self.min_disadvantages:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="content",
                        message=f"단점이 부족합니다: {disadvantages_count}개 (최소 {self.min_disadvantages}개)",
                        location="service_understanding.md - 단점",
                        suggestion=f"최소 {self.min_disadvantages}개의 단점을 작성하세요"
                    ))
            
            # 사용 사례 개수 확인 (최소 3개)
            use_cases_section = self._extract_section(content, "자주 사용되는 사례")
            if use_cases_section:
                use_cases_count = len(re.findall(r'^[-*]\s+', use_cases_section, re.MULTILINE))
                if use_cases_count < self.min_use_cases:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="content",
                        message=f"사용 사례가 부족합니다: {use_cases_count}개 (최소 {self.min_use_cases}개)",
                        location="service_understanding.md - 사용 사례",
                        suggestion=f"최소 {self.min_use_cases}개의 실제 사용 사례를 작성하세요"
                    ))
            
            # 공식 문서 링크 확인
            if "https://" not in content and "http://" not in content:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="content",
                    message="공식 문서 링크가 없습니다",
                    location="service_understanding.md - 공식 문서 링크",
                    suggestion="공식 문서 링크를 추가하세요"
                ))
        
        except Exception as e:
            issues.append(ValidationIssue(
                severity="critical",
                category="format",
                message=f"파일 읽기 오류: {str(e)}",
                location="service_understanding.md",
                suggestion="파일 인코딩 및 형식을 확인하세요"
            ))
        
        return issues
    
    def _validate_deep_dive(self, file_path: Path) -> List[ValidationIssue]:
        """Deep Dive 섹션 검증"""
        issues = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # 최소 길이 확인
            if len(content) < self.min_content_length:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="content",
                    message=f"내용이 너무 짧습니다: {len(content)}자",
                    location="deep_dive.md",
                    suggestion="더 상세한 트러블슈팅 시나리오를 추가하세요"
                ))
            
            # 시나리오 개수 확인 (최소 2개)
            scenario_count = len(re.findall(r'##\s+시나리오\s+\d+', content))
            if scenario_count < self.min_scenarios:
                issues.append(ValidationIssue(
                    severity="critical",
                    category="content",
                    message=f"시나리오가 부족합니다: {scenario_count}개 (최소 {self.min_scenarios}개)",
                    location="deep_dive.md",
                    suggestion=f"최소 {self.min_scenarios}개의 트러블슈팅 시나리오를 작성하세요"
                ))
            
            # 각 시나리오의 필수 섹션 확인
            required_subsections = [
                "시나리오 설명",
                "원인 분석",
                "원인 확인 방법",
                "수정 방법",
                "정상 확인 방법"
            ]
            
            for subsection in required_subsections:
                if subsection not in content:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="structure",
                        message=f"시나리오 필수 섹션 누락: {subsection}",
                        location="deep_dive.md",
                        suggestion=f"모든 시나리오에 '{subsection}' 섹션을 추가하세요"
                    ))
            
            # 코드 블록 확인 (진단/수정 명령어)
            code_blocks = len(re.findall(r'```[\s\S]*?```', content))
            if code_blocks < 2:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="content",
                    message=f"코드 예제가 부족합니다: {code_blocks}개",
                    location="deep_dive.md",
                    suggestion="진단 및 수정 명령어를 코드 블록으로 추가하세요"
                ))
        
        except Exception as e:
            issues.append(ValidationIssue(
                severity="critical",
                category="format",
                message=f"파일 읽기 오류: {str(e)}",
                location="deep_dive.md",
                suggestion="파일 인코딩 및 형식을 확인하세요"
            ))
        
        return issues
    
    def _validate_hands_on_lab(self, lecture_dir: Path) -> List[ValidationIssue]:
        """Hands-on Lab 검증"""
        issues = []
        
        lab_steps = sorted(lecture_dir.glob("handson_step*.md"))
        
        if len(lab_steps) < self.min_lab_steps:
            issues.append(ValidationIssue(
                severity="critical",
                category="structure",
                message=f"실습 단계 부족: {len(lab_steps)}개 (최소 {self.min_lab_steps}개)",
                location="hands-on lab",
                suggestion=f"최소 {self.min_lab_steps}개의 실습 단계를 작성하세요"
            ))
        
        # 각 단계 검증
        for step_file in lab_steps:
            try:
                content = step_file.read_text(encoding='utf-8')
                
                # 최소 길이 확인
                if len(content) < 200:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="content",
                        message=f"실습 단계 내용이 너무 짧습니다: {len(content)}자",
                        location=step_file.name,
                        suggestion="더 상세한 설명과 예제를 추가하세요"
                    ))
                
                # 필수 섹션 확인
                required_sections = ["목표", "명령어", "예상 출력", "확인"]
                missing_sections = [s for s in required_sections if s not in content]
                
                if missing_sections:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="structure",
                        message=f"필수 섹션 누락: {', '.join(missing_sections)}",
                        location=step_file.name,
                        suggestion=f"누락된 섹션을 추가하세요: {', '.join(missing_sections)}"
                    ))
                
                # 코드 블록 확인
                if "```" not in content:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="content",
                        message="코드 예제가 없습니다",
                        location=step_file.name,
                        suggestion="실행 가능한 명령어를 코드 블록으로 추가하세요"
                    ))
            
            except Exception as e:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="format",
                    message=f"파일 읽기 오류: {str(e)}",
                    location=step_file.name,
                    suggestion="파일 인코딩을 확인하세요"
                ))
        
        return issues
    
    def _validate_quiz(self, file_path: Path) -> List[ValidationIssue]:
        """Quiz 섹션 검증"""
        issues = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # 질문 개수 확인 (최소 5개)
            question_count = len(re.findall(r'\*\*질문\s+\d+\*\*', content))
            if question_count < self.min_quiz_questions:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="content",
                    message=f"퀴즈 문제가 부족합니다: {question_count}개 (최소 {self.min_quiz_questions}개)",
                    location="quiz.md",
                    suggestion=f"최소 {self.min_quiz_questions}개의 문제를 작성하세요"
                ))
            
            # 각 질문의 구조 확인
            for i in range(1, question_count + 1):
                question_pattern = f"\\*\\*질문\\s+{i}\\*\\*"
                if not re.search(question_pattern, content):
                    continue
                
                # 선택지 확인 (A, B, C, D)
                choices = re.findall(f"{question_pattern}.*?(?=\\*\\*질문|\\*\\*답|$)", content, re.DOTALL)
                if choices:
                    choice_text = choices[0]
                    choice_count = len(re.findall(r'^[A-D]\)', choice_text, re.MULTILINE))
                    if choice_count < 4:
                        issues.append(ValidationIssue(
                            severity="warning",
                            category="content",
                            message=f"질문 {i}: 선택지가 부족합니다 ({choice_count}개)",
                            location="quiz.md",
                            suggestion="4개의 선택지 (A, B, C, D)를 작성하세요"
                        ))
                
                # 답변 및 설명 확인
                if f"**답**: " not in content or f"**설명**: " not in content:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="content",
                        message=f"질문 {i}: 답변 또는 설명이 누락되었습니다",
                        location="quiz.md",
                        suggestion="모든 문제에 답변과 상세 설명을 추가하세요"
                    ))
        
        except Exception as e:
            issues.append(ValidationIssue(
                severity="critical",
                category="format",
                message=f"파일 읽기 오류: {str(e)}",
                location="quiz.md",
                suggestion="파일 인코딩을 확인하세요"
            ))
        
        return issues
    
    def _validate_all_mermaid(self, lecture_dir: Path) -> List[ValidationIssue]:
        """모든 Mermaid 다이어그램 검증"""
        issues = []
        
        md_files = list(lecture_dir.glob("*.md"))
        
        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                mermaid_issues = self._validate_mermaid_syntax(content, md_file.name)
                issues.extend(mermaid_issues)
            except Exception as e:
                issues.append(ValidationIssue(
                    severity="warning",
                    category="format",
                    message=f"파일 읽기 오류: {str(e)}",
                    location=md_file.name,
                    suggestion="파일 인코딩을 확인하세요"
                ))
        
        return issues
    
    def _validate_mermaid_syntax(self, content: str, filename: str) -> List[ValidationIssue]:
        """Mermaid 다이어그램 문법 검증"""
        issues = []
        
        # 잘못된 백틱 패턴 검사 (` 또는 ``)
        invalid_single_backtick = re.findall(r'(?<!`)`mermaid\s', content)
        invalid_double_backtick = re.findall(r'(?<!`)``mermaid\s', content)
        
        if invalid_single_backtick:
            issues.append(ValidationIssue(
                severity="critical",
                category="mermaid",
                message=f"잘못된 Mermaid 코드 블록: 백틱 1개 사용 (`mermaid) - {len(invalid_single_backtick)}개 발견",
                location=filename,
                suggestion="```mermaid (백틱 3개)를 사용하세요"
            ))
        
        if invalid_double_backtick:
            issues.append(ValidationIssue(
                severity="critical",
                category="mermaid",
                message=f"잘못된 Mermaid 코드 블록: 백틱 2개 사용 (``mermaid) - {len(invalid_double_backtick)}개 발견",
                location=filename,
                suggestion="```mermaid (백틱 3개)를 사용하세요"
            ))
        
        # 올바른 Mermaid 블록 추출 (백틱 3개)
        mermaid_blocks = re.findall(r'```mermaid\s*([\s\S]*?)```', content)
        
        # Mermaid 키워드는 있지만 올바른 블록이 없는 경우
        if ('mermaid' in content.lower()) and len(mermaid_blocks) == 0:
            issues.append(ValidationIssue(
                severity="critical",
                category="mermaid",
                message="Mermaid 키워드가 있지만 올바른 코드 블록이 없습니다",
                location=filename,
                suggestion="```mermaid로 시작하고 ```로 끝나는 코드 블록을 사용하세요"
            ))
        
        for i, block in enumerate(mermaid_blocks, 1):
            block = block.strip()
            
            if not block:
                issues.append(ValidationIssue(
                    severity="critical",
                    category="mermaid",
                    message=f"Mermaid 블록 {i}이 비어있습니다",
                    location=f"{filename} - Mermaid #{i}",
                    suggestion="다이어그램 코드를 추가하세요"
                ))
                continue
            
            # 다이어그램 타입 확인
            valid_types = ['graph', 'flowchart', 'sequenceDiagram', 'classDiagram', 
                          'stateDiagram', 'erDiagram', 'gantt', 'pie', 'journey']
            
            has_valid_type = any(block.startswith(t) for t in valid_types)
            if not has_valid_type:
                issues.append(ValidationIssue(
                    severity="critical",
                    category="mermaid",
                    message=f"Mermaid 블록 {i}: 유효하지 않은 다이어그램 타입",
                    location=f"{filename} - Mermaid #{i}",
                    suggestion=f"다음 중 하나로 시작해야 합니다: {', '.join(valid_types)}"
                ))
            
            # 기본 문법 검증
            if block.startswith('graph') or block.startswith('flowchart'):
                # 방향 확인 (TD, LR, TB, RL 등)
                if not re.match(r'(graph|flowchart)\s+(TD|LR|TB|RL|BT)', block):
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="mermaid",
                        message=f"Mermaid 블록 {i}: 그래프 방향이 명시되지 않았습니다",
                        location=f"{filename} - Mermaid #{i}",
                        suggestion="graph TD, graph LR 등으로 방향을 명시하세요"
                    ))
                
                # 노드 정의 확인
                if '-->' not in block and '---' not in block:
                    issues.append(ValidationIssue(
                        severity="warning",
                        category="mermaid",
                        message=f"Mermaid 블록 {i}: 연결선이 없습니다",
                        location=f"{filename} - Mermaid #{i}",
                        suggestion="노드 간 연결을 추가하세요 (-->, ---)"
                    ))
            
            # 괄호 매칭 확인
            open_brackets = block.count('[') + block.count('(') + block.count('{')
            close_brackets = block.count(']') + block.count(')') + block.count('}')
            
            if open_brackets != close_brackets:
                issues.append(ValidationIssue(
                    severity="critical",
                    category="mermaid",
                    message=f"Mermaid 블록 {i}: 괄호가 매칭되지 않습니다",
                    location=f"{filename} - Mermaid #{i}",
                    suggestion="괄호 개수를 확인하세요 (열림: {open_brackets}, 닫힘: {close_brackets})"
                ))
            
            # 최소 길이 확인
            if len(block) < 50:
                issues.append(ValidationIssue(
                    severity="info",
                    category="mermaid",
                    message=f"Mermaid 블록 {i}: 다이어그램이 너무 단순합니다",
                    location=f"{filename} - Mermaid #{i}",
                    suggestion="더 상세한 다이어그램을 작성하세요"
                ))
        
        return issues
    
    def _extract_section(self, content: str, section_name: str) -> str:
        """특정 섹션 추출"""
        pattern = f"###\\s+.*{section_name}.*?\\n(.*?)(?=###|$)"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1) if match else ""
    
    def _calculate_score(self, issues: List[ValidationIssue]) -> float:
        """품질 점수 계산 (0-100)"""
        base_score = 100.0
        
        for issue in issues:
            if issue.severity == "critical":
                base_score -= 15
            elif issue.severity == "warning":
                base_score -= 5
            elif issue.severity == "info":
                base_score -= 1
        
        return max(0.0, min(100.0, base_score))
    
    def _generate_summary(self, issues: List[ValidationIssue], score: float, is_valid: bool) -> str:
        """검증 요약 생성"""
        critical_count = len([i for i in issues if i.severity == "critical"])
        warning_count = len([i for i in issues if i.severity == "warning"])
        info_count = len([i for i in issues if i.severity == "info"])
        
        status = "✅ 통과" if is_valid else "❌ 실패"
        
        summary = f"""
검증 결과: {status}
품질 점수: {score:.1f}/100

발견된 이슈:
- Critical: {critical_count}개
- Warning: {warning_count}개
- Info: {info_count}개

총 {len(issues)}개의 이슈가 발견되었습니다.
"""
        
        if not is_valid:
            summary += "\n⚠️ Critical 이슈를 해결한 후 다시 생성하세요."
        
        return summary.strip()
    
    def _print_validation_result(self, result: ValidationResult):
        """검증 결과 출력"""
        print(f"\n{'='*80}")
        print("📊 Validation Result")
        print(f"{'='*80}\n")
        
        print(result.summary)
        print()
        
        if result.issues:
            print("📋 Detailed Issues:\n")
            
            # Critical 이슈
            critical = [i for i in result.issues if i.severity == "critical"]
            if critical:
                print("🔴 Critical Issues:")
                for issue in critical:
                    print(f"  [{issue.category}] {issue.location}")
                    print(f"    ❌ {issue.message}")
                    print(f"    💡 {issue.suggestion}")
                    print()
            
            # Warning 이슈
            warnings = [i for i in result.issues if i.severity == "warning"]
            if warnings:
                print("🟡 Warnings:")
                for issue in warnings:
                    print(f"  [{issue.category}] {issue.location}")
                    print(f"    ⚠️ {issue.message}")
                    print(f"    💡 {issue.suggestion}")
                    print()
            
            # Info 이슈
            infos = [i for i in result.issues if i.severity == "info"]
            if infos:
                print("ℹ️ Information:")
                for issue in infos:
                    print(f"  [{issue.category}] {issue.location}")
                    print(f"    ℹ️ {issue.message}")
                    print(f"    💡 {issue.suggestion}")
                    print()
        
        print(f"{'='*80}\n")
    
    def generate_feedback_for_regeneration(self, result: ValidationResult) -> str:
        """재생성을 위한 피드백 생성"""
        if result.is_valid:
            return "검증 통과: 재생성 불필요"
        
        feedback_parts = ["다음 이슈를 수정하여 강의를 재생성하세요:\n"]
        
        # Critical 이슈만 포함
        critical_issues = [i for i in result.issues if i.severity == "critical"]
        
        for i, issue in enumerate(critical_issues, 1):
            feedback_parts.append(f"{i}. [{issue.category}] {issue.location}")
            feedback_parts.append(f"   문제: {issue.message}")
            feedback_parts.append(f"   해결: {issue.suggestion}\n")
        
        return "\n".join(feedback_parts)
