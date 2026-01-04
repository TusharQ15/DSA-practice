import pytest
from strings.valid_parentheses import is_valid_parentheses


def test_valid_parentheses_typical():
    """Test typical valid cases"""
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("(())") == True
    assert is_valid_parentheses("([{}])") == True
    assert is_valid_parentheses("{[()]}") == True
    assert is_valid_parentheses("([]{})") == True


def test_valid_parentheses_invalid():
    """Test invalid cases"""
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("]") == False
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses("({[") == False
    assert is_valid_parentheses("){") == False
    assert is_valid_parentheses("([)") == False


def test_valid_parentheses_edge_cases():
    """Test edge cases"""
    assert is_valid_parentheses("") == True
    assert is_valid_parentheses("(((((") == False
    assert is_valid_parentheses(")))))") == False
    assert is_valid_parentheses("()(") == False
    assert is_valid_parentheses("())") == False


def test_valid_parentheses_nested():
    """Test deeply nested cases"""
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("({[({})]})") == True
    assert is_valid_parentheses("({[({})]})") == True
    assert is_valid_parentheses("({[({})]})") == True


def test_valid_parentheses_single_type():
    """Test single bracket type cases"""
    assert is_valid_parentheses("()()()") == True
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("(()())") == True
    assert is_valid_parentheses("())(") == False
    assert is_valid_parentheses("((())") == False
