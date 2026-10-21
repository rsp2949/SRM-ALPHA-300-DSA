# Day 10 — Array Processing with Two Pointers

Language: Python

### 1. Merge Sorted Array — LeetCode 88
Technique: Backward merging
Approach: Start from the last valid elements of both arrays. Compare them and place the larger value into the last available position of the destination array.
Time Complexity: O(m + n)
Space Complexity: O(1) auxiliary space
Edge Case: The second array is empty, or the first array has no initial elements.

### 2. Squares of a Sorted Array — LeetCode 977
Technique: Opposite-end comparison
Approach: Calculate the squares at both ends, place the larger square into the result array from right to left, and move the corresponding pointer inward.
Time Complexity: O(n)
Space Complexity: O(n)
Edge Case: The array contains both negative and positive numbers.

### 3. Sort Array By Parity — LeetCode 905
Technique: Two-pointer partitioning
Approach: Advance the left pointer over even numbers and the right pointer over odd numbers. Swap misplaced values until the pointers meet.
Time Complexity: O(n)
Space Complexity: O(1) auxiliary space
Edge Case: Every element belongs to the same parity group.
