# Day 9 — In-Place Array Modification

Language: Python

### 1. Move Zeroes — LeetCode 283
Method: Traverse the array and move each non-zero element forward using a write pointer. The relative order of non-zero elements is preserved.
Time Complexity: O(n)
Space Complexity: O(1)
Special Case: The array contains no non-zero elements.

### 2. Remove Duplicates from Sorted Array — LeetCode 26
Method: Scan the sorted array and store each new distinct value at the next available write position.
Time Complexity: O(n)
Space Complexity: O(1)
Special Case: All array elements are identical.

### 3. Remove Element — LeetCode 27
Method: Examine every element and overwrite the next position with each value that differs from the target. Return the count of retained elements.
Time Complexity: O(n)
Space Complexity: O(1)
Special Case: The target value does not appear in the array.

