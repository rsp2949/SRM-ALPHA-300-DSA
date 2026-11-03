
# Day 24 — Binary Search Variants (First and Last Occurrence)

**Programming Language:** Python

### 1. Find First and Last Position — LeetCode 34
- **Technique:** Two-Pass Binary Search
- **Approach:** Perform two independent binary searches to identify the first and last positions of the target in a sorted array.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Target is not present or occurs once.

### 2. Count Occurrences — GeeksforGeeks
- **Technique:** First and Last Occurrence Search
- **Approach:** Find the first and last positions of the target and calculate its frequency using their index difference plus one.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Target does not exist in the array.

### 3. Floor and Ceiling in Sorted Array
- **Technique:** Modified Binary Search
- **Approach:** Perform separate binary searches to find the greatest element less than or equal to the target and the smallest element greater than or equal to it.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Target is outside the array's value range.

### Learning Outcomes
- Implemented first and last occurrence searches.
- Practiced searching for duplicate elements.
- Learned to calculate element frequency using binary search.
- Understood floor and ceiling operations.
- Applied modified binary search to different problems.
- Improved searching efficiency using logarithmic time complexity.

### Restrictions Followed
- Avoided `bisect_left` and `bisect_right`.
- Built both binary search variants manually.
- Used manual midpoint calculation.
- Avoided linear searching.
- Implemented all searching logic from scratch.
