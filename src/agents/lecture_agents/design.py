"""
강의 디자인 Agent

생성된 강의 콘텐츠의 가독성을 개선하고 이모지를 추가하며,
퀴즈를 제외한 섹션에서 details 태그를 제거하고,
페이지 네비게이션을 추가합니다.
"""

import re
from typing import Dict, List, Optional
from pathlib import Path


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
    
    def create_navigation(
        self, 
        current_file: str, 
        all_files: List[str],
        week: int,
        day: int
    ) -> tuple[str, str]:
        """
        페이지 네비게이션 생성
        
        Args:
            current_file: 현재 파일명
            all_files: 모든 파일 목록 (정렬된 순서)
            week: 주차
            day: 일차
        
        Returns:
            (상단 네비게이션, 하단 네비게이션) 튜플
        """
        # 파일 순서 정의
        file_order = {
            'service_understanding': (1, '📚 서비스 이해'),
            'deep_dive': (2, '🔍 Deep Dive'),
            'handson': (3, '🛠️ Hands-on Lab'),
            'quiz': (4, '❓ 퀴즈')
        }
        
        # 현재 파일의 타입과 순서 찾기
        current_type = None
        current_order = 0
        for file_type, (order, _) in file_order.items():
            if file_type in current_file.lower():
                current_type = file_type
                current_order = order
                break
        
        # Hands-on Lab의 경우 step 번호 추출
        current_step = None
        if 'handson' in current_file.lower():
            match = re.search(r'step(\d+)', current_file.lower())
            if match:
                current_step = int(match.group(1))
        
        # 이전/다음 파일 찾기
        prev_file = None
        prev_title = None
        next_file = None
        next_title = None
        
        sorted_files = sorted(all_files, key=lambda f: self._get_file_sort_key(f))
        current_idx = sorted_files.index(current_file) if current_file in sorted_files else -1
        
        if current_idx > 0:
            prev_file = sorted_files[current_idx - 1]
            prev_title = self._get_file_title(prev_file)
        
        if current_idx >= 0 and current_idx < len(sorted_files) - 1:
            next_file = sorted_files[current_idx + 1]
            next_title = self._get_file_title(next_file)
        
        # 상단 네비게이션 생성
        top_nav = self._create_top_navigation(week, day, prev_file, prev_title, next_file, next_title)
        
        # 하단 네비게이션 생성
        bottom_nav = self._create_bottom_navigation(week, day, prev_file, prev_title, next_file, next_title)
        
        return top_nav, bottom_nav
    
    def _get_file_sort_key(self, filename: str) -> tuple:
        """파일 정렬 키 생성"""
        # service_understanding -> (1, 0)
        # deep_dive -> (2, 0)
        # handson_step1 -> (3, 1)
        # handson_step2 -> (3, 2)
        # quiz -> (4, 0)
        
        if 'service_understanding' in filename.lower():
            return (1, 0)
        elif 'deep_dive' in filename.lower():
            return (2, 0)
        elif 'handson' in filename.lower():
            match = re.search(r'step(\d+)', filename.lower())
            step_num = int(match.group(1)) if match else 0
            return (3, step_num)
        elif 'quiz' in filename.lower():
            return (4, 0)
        else:
            return (99, 0)
    
    def _get_file_title(self, filename: str) -> str:
        """파일명에서 제목 추출"""
        if 'service_understanding' in filename.lower():
            return '📚 서비스 이해'
        elif 'deep_dive' in filename.lower():
            return '🔍 Deep Dive'
        elif 'handson' in filename.lower():
            match = re.search(r'step(\d+)', filename.lower())
            if match:
                return f'🛠️ Hands-on Lab - Step {match.group(1)}'
            return '🛠️ Hands-on Lab'
        elif 'quiz' in filename.lower():
            return '❓ 퀴즈'
        else:
            return filename
    
    def _create_top_navigation(
        self, 
        week: int, 
        day: int, 
        prev_file: Optional[str], 
        prev_title: Optional[str],
        next_file: Optional[str],
        next_title: Optional[str]
    ) -> str:
        """상단 네비게이션 생성"""
        nav = "---\n\n"
        nav += f"# 📘 Week {week} - Day {day}\n\n"
        
        # 네비게이션 버튼
        nav += "<div style=\"display: flex; justify-content: space-between; align-items: center; padding: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;\">\n"
        
        # 이전 버튼
        if prev_file:
            nav += f"  <a href=\"{prev_file}\" style=\"color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;\">⬅️ 이전: {prev_title}</a>\n"
        else:
            nav += "  <span style=\"color: rgba(255,255,255,0.5); padding: 8px 16px;\">⬅️ 이전</span>\n"
        
        # 홈 버튼
        nav += "  <a href=\"../README.md\" style=\"color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold;\">🏠 목차</a>\n"
        
        # 다음 버튼
        if next_file:
            nav += f"  <a href=\"{next_file}\" style=\"color: white; text-decoration: none; padding: 8px 16px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold;\">다음: {next_title} ➡️</a>\n"
        else:
            nav += "  <span style=\"color: rgba(255,255,255,0.5); padding: 8px 16px;\">다음 ➡️</span>\n"
        
        nav += "</div>\n\n"
        nav += "---\n\n"
        
        return nav
    
    def _create_bottom_navigation(
        self, 
        week: int, 
        day: int, 
        prev_file: Optional[str], 
        prev_title: Optional[str],
        next_file: Optional[str],
        next_title: Optional[str]
    ) -> str:
        """하단 네비게이션 생성"""
        nav = "\n\n---\n\n"
        
        # 진행 상황 표시
        nav += "<div style=\"text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white; margin: 20px 0;\">\n"
        nav += f"  <h3 style=\"margin: 0 0 10px 0;\">🎓 Week {week} - Day {day} 학습 완료!</h3>\n"
        nav += "  <p style=\"margin: 0; opacity: 0.9;\">다음 단계로 계속 진행하세요</p>\n"
        nav += "</div>\n\n"
        
        # 네비게이션 버튼 (하단)
        nav += "<div style=\"display: flex; justify-content: space-between; align-items: center; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px;\">\n"
        
        # 이전 버튼
        if prev_file:
            nav += f"  <a href=\"{prev_file}\" style=\"color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;\">⬅️ 이전<br/><span style=\"font-size: 12px; opacity: 0.8;\">{prev_title}</span></a>\n"
        else:
            nav += "  <span style=\"color: rgba(255,255,255,0.5); padding: 10px 20px;\">⬅️ 이전</span>\n"
        
        # 홈 버튼
        nav += "  <a href=\"../README.md\" style=\"color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.3); border-radius: 5px; font-weight: bold; font-size: 14px;\">🏠<br/><span style=\"font-size: 12px;\">목차로</span></a>\n"
        
        # 다음 버튼
        if next_file:
            nav += f"  <a href=\"{next_file}\" style=\"color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 5px; font-weight: bold; font-size: 14px;\">다음 ➡️<br/><span style=\"font-size: 12px; opacity: 0.8;\">{next_title}</span></a>\n"
        else:
            nav += "  <span style=\"color: rgba(255,255,255,0.5); padding: 10px 20px;\">다음 ➡️</span>\n"
        
        nav += "</div>\n\n"
        nav += "---\n\n"
        nav += "<div style=\"text-align: center; padding: 10px; color: #666; font-size: 12px;\">\n"
        nav += "  <p>💡 <strong>Tip:</strong> 실습 중 문제가 발생하면 공식 문서를 참고하세요</p>\n"
        nav += f"  <p style=\"margin-top: 5px;\">📅 Week {week} Day {day} | 🎯 DevOps 6개월 교육과정</p>\n"
        nav += "</div>\n"
        
        return nav
    
    def add_navigation_to_content(
        self, 
        content: str, 
        current_file: str,
        all_files: List[str],
        week: int,
        day: int
    ) -> str:
        """콘텐츠에 네비게이션 추가"""
        top_nav, bottom_nav = self.create_navigation(current_file, all_files, week, day)
        
        # 상단 네비게이션 추가
        content = top_nav + content
        
        # 하단 네비게이션 추가
        content = content + bottom_nav
        
        return content
    
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
    
    def design_lecture(
        self, 
        lecture_files: Dict[str, str],
        week: int = 1,
        day: int = 1
    ) -> Dict[str, str]:
        """
        전체 강의 파일 디자인 개선
        
        Args:
            lecture_files: 파일명 -> 콘텐츠 매핑
            week: 주차
            day: 일차
        
        Returns:
            개선된 파일명 -> 콘텐츠 매핑
        """
        improved_files = {}
        all_filenames = list(lecture_files.keys())
        
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
            
            # 네비게이션 추가
            improved_content = self.add_navigation_to_content(
                improved_content,
                filename,
                all_filenames,
                week,
                day
            )
            
            improved_files[filename] = improved_content
        
        return improved_files
