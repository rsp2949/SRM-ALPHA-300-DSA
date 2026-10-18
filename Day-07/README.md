# Day 7 — Array Rotation

**Language:** Python

### 1. Rotate Array — LeetCode 189
Approach: Reverse the whole array, then the first `k` elements, then the remaining elements.
Complexity: O(n) time, O(1) auxiliary space.
Edge case: `k` equals the array length.

### 2. Rotate Array by K Steps
Approach: Use three reversals and reduce `k` using `k % n`.
Complexity: O(n) time, O(1) auxiliary space.
Edge case: `k` is greater than the array length.

### 3. Reverse Array in Groups — GeeksforGeeks
Approach: Reverse each group using two pointers and swaps.
Complexity: O(n) time, O(1) auxiliary space.
Edge case: The final group contains fewer than `k` elements.
