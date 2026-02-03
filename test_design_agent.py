"""
Design Agent 테스트 스크립트

강의 디자인 Agent의 기능을 테스트합니다:
1. details 태그 제거 (퀴즈 제외)
2. 이모지 추가
3. 마크다운 형식 개선
"""

from src.agents.lecture_agents.design import DesignAgent


def test_remove_details_tags():
    """details 태그 제거 테스트"""
    print("\n" + "="*80)
    print("🧪 Test 1: Remove details tags")
    print("="*80)
    
    agent = DesignAgent()
    
    # 테스트 콘텐츠
    content = """
## 1. 배경 정보

<details>
<summary>배경 정보 보기</summary>

Docker는 컨테이너 기술입니다.

</details>

## 2. 핵심 개념

<details>
<summary>핵심 개념 보기</summary>

- 컨테이너
- 이미지
- 레지스트리

</details>
"""
    
    result = agent.remove_details_tags(content)
    
    print("\n원본:")
    print(content)
    print("\n결과:")
    print(result)
    
    # 검증
    assert "<details>" not in result
    assert "<summary>" not in result
    assert "Docker는 컨테이너 기술입니다." in result
    assert "- 컨테이너" in result
    
    print("\n✅ Test 1 passed: details 태그가 제거되었습니다")


def test_add_emojis():
    """이모지 추가 테스트"""
    print("\n" + "="*80)
    print("🧪 Test 2: Add emojis to headings")
    print("="*80)
    
    agent = DesignAgent()
    
    content = """
## 1. 배경 정보

Docker는 컨테이너 기술입니다.

## 2. 핵심 개념

- 컨테이너
- 이미지

## 3. 장단점

**장점**:
- 빠른 배포

**단점**:
- 학습 곡선

### 시나리오 1: 포트 충돌

문제 상황입니다.

### 원인 분석

원인을 분석합니다.

### 수정 방법

수정 방법입니다.
"""
    
    result = agent.add_emojis_to_headings(content)
    
    print("\n원본:")
    print(content)
    print("\n결과:")
    print(result)
    
    # 검증
    assert "📚" in result  # 배경 정보
    assert "🔑" in result  # 핵심 개념
    assert "⚖️" in result  # 장단점
    assert "🔍" in result  # 시나리오
    assert "🔬" in result  # 원인 분석
    assert "🔧" in result  # 수정 방법
    
    print("\n✅ Test 2 passed: 이모지가 추가되었습니다")


def test_design_section():
    """섹션 디자인 개선 테스트"""
    print("\n" + "="*80)
    print("🧪 Test 3: Design section improvement")
    print("="*80)
    
    agent = DesignAgent()
    
    content = """
# 서비스 이해

## 1. 배경 정보

<details>
<summary>배경 정보 보기</summary>

Docker는 컨테이너 기술입니다.

</details>

## 2. 핵심 개념

<details>
<summary>핵심 개념 보기</summary>

- 컨테이너
- 이미지

</details>

## 3. 장단점

<details>
<summary>장단점 보기</summary>

**장점**:
- 빠른 배포

**단점**:
- 학습 곡선

</details>
"""
    
    # 퀴즈가 아닌 섹션 (details 태그 제거)
    result = agent.design_section(content, "service_understanding", is_quiz=False)
    
    print("\n원본:")
    print(content)
    print("\n결과:")
    print(result)
    
    # 검증
    assert "<details>" not in result
    assert "<summary>" not in result
    assert "📚" in result  # 배경 정보 이모지
    assert "🔑" in result  # 핵심 개념 이모지
    assert "⚖️" in result  # 장단점 이모지
    assert "Docker는 컨테이너 기술입니다." in result
    
    print("\n✅ Test 3 passed: 섹션 디자인이 개선되었습니다")


def test_quiz_keeps_details():
    """퀴즈는 details 태그 유지 테스트"""
    print("\n" + "="*80)
    print("🧪 Test 4: Quiz keeps details tags")
    print("="*80)
    
    agent = DesignAgent()
    
    content = """
# 퀴즈

## 질문 1

<details>
<summary>정답 보기</summary>

**답**: A

**설명**: 정답은 A입니다.

</details>

## 질문 2

<details>
<summary>정답 보기</summary>

**답**: B

**설명**: 정답은 B입니다.

</details>
"""
    
    # 퀴즈 섹션 (details 태그 유지)
    result = agent.design_section(content, "quiz", is_quiz=True)
    
    print("\n원본:")
    print(content)
    print("\n결과:")
    print(result)
    
    # 검증
    assert "<details>" in result
    assert "<summary>" in result
    assert "정답 보기" in result
    assert "❓" in result  # 질문 이모지
    
    print("\n✅ Test 4 passed: 퀴즈는 details 태그를 유지합니다")


def test_design_lecture():
    """전체 강의 디자인 테스트"""
    print("\n" + "="*80)
    print("🧪 Test 5: Design entire lecture")
    print("="*80)
    
    agent = DesignAgent()
    
    lecture_files = {
        "service_understanding.md": """
## 1. 배경 정보

<details>
<summary>배경 정보 보기</summary>

Docker는 컨테이너 기술입니다.

</details>
""",
        "deep_dive.md": """
### 시나리오 1: 포트 충돌

<details>
<summary>문제 상황 보기</summary>

포트가 충돌합니다.

</details>

### 원인 분석

<details>
<summary>원인 분석 보기</summary>

5000 포트가 사용 중입니다.

</details>
""",
        "quiz.md": """
## 질문 1

<details>
<summary>정답 보기</summary>

**답**: A

</details>
"""
    }
    
    result = agent.design_lecture(lecture_files)
    
    print("\n결과:")
    for filename, content in result.items():
        print(f"\n--- {filename} ---")
        print(content[:200] + "...")
    
    # 검증
    assert "<details>" not in result["service_understanding.md"]
    assert "<details>" not in result["deep_dive.md"]
    assert "<details>" in result["quiz.md"]  # 퀴즈는 유지
    
    assert "📚" in result["service_understanding.md"]
    assert "🔍" in result["deep_dive.md"]
    assert "❓" in result["quiz.md"]
    
    print("\n✅ Test 5 passed: 전체 강의 디자인이 개선되었습니다")


def main():
    """모든 테스트 실행"""
    print("\n" + "="*80)
    print("🎨 Design Agent Tests")
    print("="*80)
    
    try:
        test_remove_details_tags()
        test_add_emojis()
        test_design_section()
        test_quiz_keeps_details()
        test_design_lecture()
        
        print("\n" + "="*80)
        print("✅ All tests passed!")
        print("="*80)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        raise
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise


if __name__ == "__main__":
    main()
