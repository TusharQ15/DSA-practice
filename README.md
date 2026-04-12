# DSA Practice Repository

NeetCode/Blind 75 style DSA practice in Python with tests.

🔖 Topics: python, dsa, algorithms, data-structures, leetcode, coding-interview, neetcode, blind-75

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

## Repository Structure

```
dsa-practice/
├── arrays/               # Array manipulation problems
├── strings/              # String manipulation problems
└── tests/                # Test cases for all problems
```

## Current Focus

**30-Day DSA Challenge (Dec 2025 – Jan 2026)**  
Focused on mastering core data structures and algorithms through structured practice. Following a NeetCode/Blind 75 style curriculum with an emphasis on arrays, strings, binary search, and pattern-based problem-solving.

See [PROGRESS.md](PROGRESS.md) for detailed progress tracking and problem solutions.

> **Note:** More topics and problems will be added over time.

## Problem File Format

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
    pass
```

For a complete example, see [arrays/two_sum.py](arrays/two_sum.py).

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
| **Arrays** | 9 | Two Pointers, Sliding Window, Binary Search |
| **Strings** | 2 | Two Pointers, Hashing |

I use these resources for practice and learning:
- [LeetCode](https://leetcode.com/) - For problem sets and practice
- [NeetCode 150](https://neetcode.io/) - For structured problem selection
- [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview) - For learning patterns

## 📝 Notes

Personal notes and insights are maintained in [NOTES.md](NOTES.md).
