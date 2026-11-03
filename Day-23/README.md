
# Day 23 — Binary Search on Answer

**Programming Language:** Python

### 1. Sqrt(x) — LeetCode 69
- **Technique:** Binary Search on Answer
- **Approach:** Find the largest integer whose square is less than or equal to the given number. Adjust the search range based on the square of the midpoint.
- **Time Complexity:** O(log x)
- **Auxiliary Space:** O(1)
- **Special Case:** Input is 0 or 1.

### 2. Guess Number Higher or Lower — LeetCode 374
- **Technique:** Binary Search with API
- **Approach:** Compare the middle value with the hidden number using the guess API. Narrow the search range according to whether the guess is higher, lower, or correct.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Hidden number is at either boundary.

### 3. Valid Perfect Square — LeetCode 367
- **Technique:** Binary Search
- **Approach:** Calculate the square of the midpoint and compare it with the given number. Adjust the search range until an exact square is found or no valid candidate remains.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Input is 1 or a non-perfect-square number.

### Learning Outcomes
- Practiced Binary Search on Answer.
- Implemented integer square root manually.
- Applied binary search with an API-based condition.
- Checked perfect squares without built-in square root functions.
- Improved understanding of search-space reduction.
- Practiced logarithmic-time algorithms.

### Restrictions Followed
- Avoided `bisect`, `bisect_left`, and `bisect_right`.
- Avoided `math.isqrt()`.
- Used manual midpoint calculation.
- Built condition checks inside binary search.
- Implemented all searching logic from scratch.
