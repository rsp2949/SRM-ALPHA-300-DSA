# Day 12 — Dynamic Sliding Window

**Language:** Python

### 1. Minimum Size Subarray Sum — LeetCode 209
- **Technique:** Shrinking window
- **Approach:** Add elements from the right while maintaining the current sum. Once the target is reached, record the shortest length and remove elements from the left to find a smaller valid window.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Edge Case:** The target cannot be reached by any contiguous subarray.

### 2. Longest Subarray with Sum K — GeeksforGeeks
- **Technique:** Variable-size window
- **Approach:** Maintain a running sum while expanding the window. Reduce the sum from the left whenever it exceeds `k`, then update the longest length when the sum matches `k`.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Edge Case:** No contiguous subarray has the required sum.
- **Note:** This method assumes non-negative array elements. For arrays containing negative values, a prefix-sum and hashmap technique is more appropriate.

### 3. Fruit Into Baskets — LeetCode 904
- **Technique:** Sliding window with frequency counting
- **Approach:** Track fruit frequencies in the current window. If more than two fruit types are present, remove elements from the left until the window becomes valid again.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) auxiliary space, as the valid window holds at most two distinct fruit types.
