# DSA Practice Repository

This is a personal DSA practice repo in Python, used to prepare for coding interviews and track progress over time.

🔖 Topics: python, dsa, algorithms, data-structures, leetcode, coding-interview

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TusharQ15/dsa-practice.git
   cd dsa-practice
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🏗️ Repository Structure

```
dsa-practice/
├── arrays/               # Array manipulation problems (7 problems)
│   ├── average_of_array.py
│   ├── max_in_array.py
│   ├── min_in_array.py
│   ├── move_zeros.py
│   ├── reverse_array.py
│   ├── sum_of_array.py
│   └── two_sum.py
├── strings/              # String manipulation problems (2 problems)
│   ├── is_palindrome.py
│   └── reverse_string.py
└── tests/               # Test cases
```

> **Note:** Some topic folders are planned and will be filled over the next 1-2 months.

## 📝 Problem File Format

Each solution follows this consistent structure:

```python
"""
Problem: Two Sum
Source: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach: Use a hash map to store seen numbers and their indices.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All test cases passed!")
```

## 🧪 Testing

Tests are written using pytest. Each problem has a corresponding test file in the `tests/` directory.

Run all tests:
```bash
pytest tests/
```

Run tests for a specific problem:
```bash
pytest tests/test_two_sum.py
```

## 📊 Progress

| Topic | Problems | Key Patterns |
|-------|----------|--------------|
| **Arrays** | 7 | Two Pointers, Sliding Window |
| **Strings** | 2 | Hashing, Sliding Window |

I use these resources for practice and learning:
- [LeetCode](https://leetcode.com/) - For problem sets and practice
- [NeetCode 150](https://neetcode.io/) - For structured problem selection
- [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview) - For learning patterns

## 📝 Notes

Personal notes and insights are maintained in [NOTES.md](NOTES.md).
