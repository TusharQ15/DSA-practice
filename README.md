# DSA Practice Repository

📚 A systematic collection of DSA problems solved in Python, organized by topic and pattern for interview preparation.

## 🏗️ Repository Structure

```
dsa-practice/
├── arrays/               # Array manipulation problems
├── strings/             # String manipulation problems
├── linked_list/         # Linked list problems
├── trees/               # Binary trees, BST, etc.
├── graphs/              # Graph algorithms
├── dp/                  # Dynamic programming
├── recursion/           # Recursion and backtracking
├── math/                # Math and number theory
├── search_sort/         # Searching and sorting algorithms
├── misc/                # Miscellaneous problems
├── tests/               # Test cases
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── PROGRESS.md          # Tracking solved problems
└── NOTES.md             # Patterns and insights
```

## 📝 Problem File Format

Each solution file follows this structure:

```python
"""
Problem: Problem Name
Source: URL to problem
Difficulty: Easy/Medium/Hard

Approach: 1-2 line explanation of the approach

Time Complexity: O(...)
Space Complexity: O(...)
"""

def solution(...):
    # Implementation
    pass

# Test cases
if __name__ == "__main__":
    # Basic tests
    assert solution(...) == expected_output
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dsa-practice.git
   cd dsa-practice
   ```

2. **Set up the environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run tests**
   ```bash
   pytest tests/
   ```

## 📚 Topics Covered

| Topic | Problems | Key Patterns |
|-------|----------|--------------|
| **Arrays** | 7 | Two Pointers, Sliding Window |
| **Strings** | 2 | Hashing, Sliding Window |
| **Linked Lists** | 0 | Fast & Slow Pointers |
| **Trees** | 0 | DFS, BFS, Traversals |
| **Graphs** | 0 | BFS, DFS, Dijkstra's |
| **DP** | 0 | Memoization, Tabulation |
| **Search/Sort** | 0 | Binary Search, Quick/Merge Sort |

## 📈 Progress Tracking

- **Total Problems Solved**: 9
- **Weekly Goal**: 5-7 problems
- **Current Focus**: Arrays & Strings

See [PROGRESS.md](PROGRESS.md) for detailed progress and [NOTES.md](NOTES.md) for patterns and insights.

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## 📝 Commit Message Style

- `feat(topic): add new solution` - New problem solution
- `fix(topic): correct solution` - Fix existing solution
- `refactor(topic): improve code` - Code improvements
- `docs: update readme` - Documentation updates

## 🔗 Resources

- [LeetCode](https://leetcode.com/)
- [NeetCode](https://neetcode.io/)
- [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview)
- [AlgoExpert](https://www.algoexpert.io/)
