import pytest
from strings.group_anagrams import group_anagrams


def test_typical_mixed_anagram_groups():
    """Test typical case with mixed anagram groups."""
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_strs)
    
    # Sort each group and the result for consistent comparison
    sorted_result = [sorted(group) for group in result]
    sorted_result.sort()
    
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    sorted_expected = [sorted(group) for group in expected]
    sorted_expected.sort()
    
    assert sorted_result == sorted_expected


def test_all_strings_identical():
    """Test case where all strings are identical."""
    input_strs = ["aaa", "aaa", "aaa"]
    result = group_anagrams(input_strs)
    
    assert len(result) == 1
    assert sorted(result[0]) == ["aaa", "aaa", "aaa"]


def test_no_anagrams_all_unique():
    """Test case where no anagrams exist (all unique)."""
    input_strs = ["abc", "def", "ghi"]
    result = group_anagrams(input_strs)
    
    # Each string should be in its own group
    assert len(result) == 3
    
    # Check that all original strings are present
    all_strings = []
    for group in result:
        all_strings.extend(group)
    assert sorted(all_strings) == ["abc", "def", "ghi"]


def test_empty_list_input():
    """Test case with empty list input."""
    input_strs = []
    result = group_anagrams(input_strs)
    assert result == []


def test_single_element_list():
    """Test case with single element list."""
    input_strs = ["hello"]
    result = group_anagrams(input_strs)
    assert result == [["hello"]]


def test_complex_anagrams():
    """Test case with more complex anagrams."""
    input_strs = ["", "a", "b", "ab", "ba", "abc", "bac", "cab"]
    result = group_anagrams(input_strs)
    
    # Sort each group and the result for consistent comparison
    sorted_result = [sorted(group) for group in result]
    sorted_result.sort()
    
    expected = [[""], ["a"], ["b"], ["ab", "ba"], ["abc", "bac", "cab"]]
    sorted_expected = [sorted(group) for group in expected]
    sorted_expected.sort()
    
    assert sorted_result == sorted_expected


def test_case_sensitive_anagrams():
    """Test case sensitivity in anagrams."""
    input_strs = ["a", "A", "b", "B"]
    result = group_anagrams(input_strs)
    
    # Sort each group and the result for consistent comparison
    sorted_result = [sorted(group) for group in result]
    sorted_result.sort()
    
    expected = [["A"], ["B"], ["a"], ["b"]]
    sorted_expected = [sorted(group) for group in expected]
    sorted_expected.sort()
    
    assert sorted_result == sorted_expected


def test_unicode_characters():
    """Test case with Unicode characters."""
    input_strs = ["ñá", "áñ", "hello", "olleh"]
    result = group_anagrams(input_strs)
    
    # Sort each group and the result for consistent comparison
    sorted_result = [sorted(group) for group in result]
    sorted_result.sort()
    
    expected = [["áñ", "ñá"], ["hello", "olleh"]]
    sorted_expected = [sorted(group) for group in expected]
    sorted_expected.sort()
    
    assert sorted_result == sorted_expected
