# DSA Patterns & Insights

## 🔄 Common Patterns

### 1. Two Pointers
- **When to use**: Array/string problems requiring O(1) space or when you need to find pairs/triplets
- **Examples**:
  - Two Sum (sorted array)
  - Container With Most Water
  - Remove Duplicates from Sorted Array
- **Tip**: One pointer at start, one at end; move inward based on condition

### 2. Sliding Window
- **When to use**: Subarray/substring problems with fixed/variable window size
- **Examples**:
  - Maximum Sum Subarray of Size K
  - Longest Substring with K Distinct Characters
  - Minimum Window Substring
- **Tip**: Use hash map to track characters in window

### 3. Hash Map/Dictionary
- **When to use**: Need O(1) lookups or need to count frequencies
- **Examples**:
  - Two Sum
  - Group Anagrams
  - Subarray Sum Equals K
- **Tip**: Can often reduce O(n²) to O(n)

### 4. Binary Search
- **When to use**: Sorted arrays, finding min/max of something
- **Examples**:
  - Search in Rotated Sorted Array
  - Find Minimum in Rotated Sorted Array
  - Median of Two Sorted Arrays
- **Tip**: Always check edge cases (empty array, single element, etc.)

### 5. Prefix/Suffix Products
- **When to use**: When you need to calculate products of all elements except self in O(n) time
- **Examples**:
  - Product of Array Except Self
- **Tip**: Calculate prefix products in one pass, then calculate suffix products in reverse and multiply with prefix

### 6. Kadane's Algorithm
- **When to use**: Finding maximum subarray sum in O(n) time
- **Examples**:
  - Maximum Subarray
  - Best Time to Buy and Sell Stock
- **Tip**: Keep track of current maximum and global maximum, reset current maximum if it becomes negative

### 7. Rotated Array Patterns

### 8. Two Pointers for Container Problems
- **When to use**: Problems involving finding maximum area or volume between two points
- **Examples**:
  - Container With Most Water
  - Trapping Rain Water
- **Tip**: Start with widest possible container and move the pointer at the shorter line inward

### 9. Rotated Array Patterns
- **When to use**: When dealing with sorted arrays that have been rotated
- **Key Insights**:
  - At least one half of the array (left or right of mid) will always be sorted
  - The minimum element is at the pivot point where rotation occurs
  - For search, first determine which half is sorted, then check if target is in that range
- **Examples**:
  - Find Minimum in Rotated Sorted Array
  - Search in Rotated Sorted Array
- **Complexity**: O(log n) time, O(1) space
- **Edge Cases**:
  - Array not rotated (fully sorted)
  - Single element array
  - Array with duplicate elements (requires additional handling)

### 8. 3Sum and k-Sum Problems
- **When to use**: Finding unique triplets (or k elements) that sum to a target
- **Key Insights**:
  - Sort the array first to enable two-pointer technique
  - Skip duplicates to avoid duplicate triplets
  - For each element, use two pointers to find pairs that sum to the complement
- **Time Complexity**: O(n²) for 3Sum, O(n^(k-1)) for k-Sum
- **Example**: 3Sum, 4Sum, 3Sum Closest

### 9. Maximum Product Subarray (DP)
- **When to use**: Finding contiguous subarray with maximum product, especially with negative numbers and zeros
- **Examples**:
  - Maximum Product Subarray
- **Tip**: Track both max and min products at each step since a negative number can make a min product the max when multiplied by another negative

### 10. Best Time to Buy and Sell Stock (Greedy)
- **When to use**: Finding maximum profit from buying and selling a stock once
- **Examples**:
  - Best Time to Buy and Sell Stock
- **Tip**: Track the minimum price seen so far and calculate potential profit at each step

### 11. Trapping Rain Water (Two Pointers)
- **When to use**: Calculating trapped water between bars of different heights
- **Key Insights**:
  - The amount of water that can be trapped at any bar is determined by the minimum of the maximum heights to its left and right, minus the height of the current bar
  - Using two pointers (left and right) and tracking left_max and right_max allows O(n) time and O(1) space solution
  - Move the pointer pointing to the shorter bar inward, as the water level is constrained by the shorter side

### 12. Longest Consecutive Sequence (Hash Set)
- **When to use**: Finding the length of the longest consecutive elements sequence
- **Key Insights**:
  - Convert the array to a set for O(1) lookups
  - Only start counting sequences from numbers that are the start of a sequence (i.e., num-1 is not in the set)
  - For each start of a sequence, count how many consecutive numbers follow it
  - This approach ensures O(n) time complexity as each number is processed at most twice

### 13. Dynamic Programming
- **When to use**: Problems with optimal substructure and overlapping subproblems, or when a problem can be broken down into simpler subproblems
- **Examples**:
  - Fibonacci
  - Longest Increasing Subsequence
  - 0/1 Knapsack
- **Tip**: Start with recursive solution, then memoize, then tabulate

## 📝 Problem-Solving Approach

1. **Understand the Problem**
   - Ask clarifying questions
   - Write sample inputs/outputs
   - Check edge cases

2. **Brute Force First**
   - Write a working solution, then optimize
   - Helps identify patterns

3. **Optimize**
   - Look for repeated work
   - Can you use extra space to reduce time?
   - Sort the input?
   - Use a data structure for faster lookups?

4. **Walk Through**
   - Manually walk through your solution with test cases
   - Check edge cases

5. **Implement**
   - Write clean, readable code
   - Use meaningful variable names
   - Add comments for complex logic

## 🔍 Common Pitfalls

- Off-by-one errors in loops
- Not handling empty/single-element inputs
- Infinite loops in recursion
- Integer overflow (in some languages)
- Modifying array while iterating over it

## 📚 Resources
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview)
