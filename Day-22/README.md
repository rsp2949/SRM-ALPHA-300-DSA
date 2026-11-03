
# Day 22 — Classic Binary Search

**Programming Language:** Python

### 1. Binary Search — LeetCode 704
- **Technique:** Iterative Binary Search
- **Approach:** Use low and high pointers to calculate the middle index. Compare the middle element with the target and eliminate half of the search space in each iteration.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Empty array or target not found.

### 2. Search Insert Position — LeetCode 35
- **Technique:** Modified Binary Search
- **Approach:** Search for the target using binary search. If it is not present, return the low pointer as the correct insertion index.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Target smaller than the first element or greater than the last element.

### 3. First Bad Version — LeetCode 278
- **Technique:** Binary Search on Versions
- **Approach:** Search through versions using low and high pointers. If the middle version is bad, search the left half; otherwise, search the right half to find the first bad version.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** First version is bad or all versions are good.

### Learning Outcomes
- Understood the fundamentals of Binary Search.
- Practiced manual midpoint calculation.
- Learned to reduce the search space by half.
- Applied binary search to insertion position problems.
- Used binary search to identify the first bad version.
- Practiced efficient searching with logarithmic time complexity.

### Restrictions Followed
- Avoided `bisect`, `bisect_left`, and `bisect_right`.
- Used manual low, high, and mid pointers.
- Calculated midpoint using `low + (high - low) // 2`.
- Used iterative implementation.
- Implemented all searching logic from scratch.
