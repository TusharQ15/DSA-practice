import pytest
from strings.generate_parentheses import generate_parentheses


def test_generate_parentheses_basic():
    """Test basic cases"""
    result1 = generate_parentheses(1)
    assert result1 == ["()"]
    
    result2 = generate_parentheses(2)
    assert set(result2) == {"(())", "()()"}
    assert len(result2) == 2
    
    result3 = generate_parentheses(3)
    expected3 = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert set(result3) == expected3
    assert len(result3) == 5


def test_generate_parentheses_edge_cases():
    """Test edge cases"""
    # n = 0 should return empty list
    assert generate_parentheses(0) == []
    
    # Test that results are in lexicographic order (due to backtracking)
    result2 = generate_parentheses(2)
    assert result2 == ["(())", "()()"]


def test_generate_parentheses_medium():
    """Test medium size cases"""
    result4 = generate_parentheses(4)
    expected4 = {
        "(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
        "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
        "()(()())", "()(())()", "()()(())", "()()()()"
    }
    assert set(result4) == expected4
    assert len(result4) == 14


def test_generate_parentheses_consistency():
    """Test that all generated strings are valid"""
    for n in range(1, 6):
        result = generate_parentheses(n)
        for s in result:
            # Check length
            assert len(s) == 2 * n
            # Check validity
            assert is_valid_parentheses_string(s)


def test_generate_parentheses_count():
    """Test that the number of results matches Catalan numbers"""
    # Catalan numbers: 1, 2, 5, 14, 42, 132...
    catalan = [1, 2, 5, 14, 42, 132]
    
    for i, expected_count in enumerate(catalan, start=1):
        result = generate_parentheses(i)
        assert len(result) == expected_count


def is_valid_parentheses_string(s: str) -> bool:
    """Helper function to validate parentheses string"""
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def test_generate_parentheses_uniqueness():
    """Test that all generated strings are unique"""
    for n in range(1, 6):
        result = generate_parentheses(n)
        assert len(result) == len(set(result))  # No duplicates
