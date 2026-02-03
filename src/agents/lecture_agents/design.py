"""
강의 디자인 Agent

생성된 강의 콘텐츠의 가독성을 개선하고 이모지를 추가하며,
퀴즈를 제외한 섹션에서 details 태그를 제거합니다.
"""

import re
from typing import Dict, List


class DesignAgent:
    """강의 디자인 개선 Agent"""
    
    def __init__(self):
        # 섹션별 이모지 매핑
        self.section_emojis = {
            "배경 정보": "📚",
            "핵심 개념": "🔑",
            "장단점": "⚖️",
            "장점": "✅",
            "단점": "⚠️",
            "자주 사용되는 사례": "💡",
            "사용 사례": "💡",
            "연관 서비스": "🔗",
            "공식 문서": "📖",
            "시나리오": "🔍",
            "원인 분석": "🔬",
            "원인 확인": "🔎",
            "진단": "🔎",
            "수정 방법": "🔧",
            "해결": "🔧",
            "정상 확인": "✔️",
            "검증": "✔️",
            "실습 개요": "🎯",
            "사전 요구사항": "📋",
            "환경 설정": "⚙️",
            "Step": "👉",
            "실습 완료": "🎉",
            "추가 자료": "📚",
            "질문": "❓",
            "답": "✅",
            "설명": "💬",
        }
    
    def remove_details_tags(self, content: str) -> str:
        """details 태그 제거 (퀴즈 제외)"""
        # details 태그와 그 내용을 추출하여 내용만 남김
        pattern = r'<details>\s*<summary>(.*?)</summary>\s*(.*?)</details>'
        
        def replace_details(match):
            summary = match.group(1).strip()
            inner_content = match.group(2).strip()
            # summary는 제거하고 내용만 반환
            return inner_content
        
        # re.DOTALL을 사용하여 여러 줄에 걸친 패턴 매칭
        result = re.sub(pattern, replace_details, content, flags=re.DOTALL)
        return result
    
    def add_emojis_to_headings(self, content: str) -> str:
        """제목에 이모지 추가"""
        lines = content.split('\n')
        result_lines = []
        
        for line in lines:
            # 제목 라인 확인 (##, ###, #### 등)
            if line.strip().startswith('#'):
                # 이미 이모지가 있는지 확인
                has_emoji = any(char in line for char in '📚🔑⚖️✅⚠️💡🔗📖🔍🔬🔎🔧✔️🎯📋⚙️👉🎉❓💬')
                
                if not has_emoji:
                    # 제목에서 키워드 찾기
                    for keyword, emoji in self.section_emojis.items():
                        if keyword in line:
                            # 제목 레벨 추출
                            heading_level = len(line) - len(line.lstrip('#'))
                            heading_marks = '#' * heading_level
                            title = line.lstrip('#').strip()
                            
                            # 이모지 추가
                            line = f"{heading_marks} {emoji} {title}"
                            break
                
                result_lines.append(line)
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    def improve_formatting(self, content: str) -> str:
        """마크다운 형식 개선"""
        # 연속된 빈 줄을 2개로 제한
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        # 목록 항목 앞에 적절한 공백 추가
        content = re.sub(r'^(\s*)-\s+', r'\1- ', content, flags=re.MULTILINE)
        
        # 코드 블록 전후에 빈 줄 추가
        content = re.sub(r'([^\n])\n```', r'\1\n\n```', content)
        content = re.sub(r'```\n([^\n])', r'```\n\n\1', content)
        
        return content
    
    def design_section(self, content: str, section_type: str, is_quiz: bool = False) -> str:
        """
        섹션 디자인 개선
        
        Args:
            content: 원본 콘텐츠
            section_type: 섹션 타입 (service_understanding, deep_dive, hands_on, quiz)
            is_quiz: 퀴즈 섹션 여부
        
        Returns:
            개선된 콘텐츠
        """
        # 1. 퀴즈가 아닌 경우 details 태그 제거
        if not is_quiz:
            content = self.remove_details_tags(content)
        
        # 2. 제목에 이모지 추가
        content = self.add_emojis_to_headings(content)
        
        # 3. 마크다운 형식 개선
        content = self.improve_formatting(content)
        
        return content
    
    def design_lecture(self, lecture_files: Dict[str, str]) -> Dict[str, str]:
        """
        전체 강의 파일 디자인 개선
        
        Args:
            lecture_files: 파일명 -> 콘텐츠 매핑
        
        Returns:
            개선된 파일명 -> 콘텐츠 매핑
        """
        improved_files = {}
        
        for filename, content in lecture_files.items():
            print(f"🎨 디자인 개선 중: {filename}")
            
            # 파일 타입 판단
            is_quiz = 'quiz' in filename.lower()
            
            if 'service_understanding' in filename:
                section_type = 'service_understanding'
            elif 'deep_dive' in filename:
                section_type = 'deep_dive'
            elif 'handson' in filename or 'hands_on' in filename:
                section_type = 'hands_on'
            elif 'quiz' in filename:
                section_type = 'quiz'
            else:
                section_type = 'unknown'
            
            # 디자인 개선
            improved_content = self.design_section(content, section_type, is_quiz)
            improved_files[filename] = improved_content
        
        return improved_files
