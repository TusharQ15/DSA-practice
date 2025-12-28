import pytest
from arrays.longest_consecutive_sequence import longest_consecutive

def test_longest_consecutive_basic_examples():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # 1,2,3,4
    assert longest_consecutive([0,3,7,2,5,8,4,6,0,1]) == 9  # 0,1,2,3,4,5,6,7,8

def test_longest_consecutive_empty_and_single():
    assert longest_consecutive([]) == 0
    assert longest_consecutive([5]) == 1

def test_longest_consecutive_already_ordered():
    assert longest_consecutive([1,2,3,4,5]) == 5
    assert longest_consecutive([-2,-1,0,1]) == 4

def test_longest_consecutive_with_duplicates():
    assert longest_consecutive([1,1,1]) == 1
    assert longest_consecutive([2,2,2,2,2]) == 1

def test_longest_consecutive_negative_numbers():
    assert longest_consecutive([-1,1,0,2,-2,3]) == 6  # -2,-1,0,1,2,3
    assert longest_consecutive([-3,-1,-2,0,2,1]) == 6  # -3,-2,-1,0,1,2

def test_longest_consecutive_disconnected_sequences():
    assert longest_consecutive([10,5,6,100,101,7]) == 3  # 5,6,7
    assert longest_consecutive([1,3,5,7,9,11]) == 1  # All separate

def test_longest_consecutive_mixed_cases():
    assert longest_consecutive([1,2,0,1]) == 3  # 0,1,2
    assert longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6]) == 7  # -1,0,1,3,4,5,6,7,8,9
