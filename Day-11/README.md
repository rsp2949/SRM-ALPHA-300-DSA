# Day 11 — Sliding Window and Array Statistics

**Language:** Python

### 1. Maximum Average Subarray I — LeetCode 643
- **Technique:** Fixed-size sliding window
- **Approach:** Find the sum of the first `k` elements, then update the window sum by removing the previous element and adding the next one. Return the highest window average.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Edge Case:** The window covers the entire array.

### 2. Max Sum Subarray of Size K — GeeksforGeeks
- **Technique:** Running window sum
- **Approach:** Calculate the initial window sum and move through the array one element at a time, tracking the maximum sum.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Edge Case:** All values in the array are identical.

### 3. Mean of Array After Removing Some Elements — LeetCode 1619
- **Technique:** Frequency counting
- **Approach:** Count the occurrences of each value, exclude the lowest and highest 5% of elements, and calculate the mean of the remaining values without using built-in sorting.
- **Time Complexity:** O(n + U), where U is the value range.
- **Space Complexity:** O(U)
- **Edge Case:** All values are equal, so removing the extremes leaves the same mean.

