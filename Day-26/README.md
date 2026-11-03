
# Day 26 — Binary Search on Rotated Array

**Programming Language:** Python

### 1. Search in Rotated Sorted Array — LeetCode 33

- **Technique:** Modified Binary Search
- **Approach:** Identify which half of the rotated array is sorted. Check whether the target belongs to that half and eliminate the other half accordingly.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Target is absent or the array is rotated at different pivot positions.

### 2. Find Minimum in Rotated Sorted Array — LeetCode 153

- **Technique:** Binary Search on Minimum Element
- **Approach:** Compare the middle element with the last element. If the middle element is greater, search the right half; otherwise, search the left half including the middle position.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Array is not rotated or contains only one element.

### 3. Find the Rotation Count — GeeksforGeeks

- **Technique:** Binary Search on Minimum Index
- **Approach:** Find the index of the minimum element using binary search. The index of the minimum element represents the number of rotations performed on the originally sorted array.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Array is not rotated or contains only one element.

### Learning Outcomes

- Understood binary search on rotated sorted arrays.
- Practiced identifying the sorted half of an array.
- Learned to search for elements in rotated arrays.
- Implemented minimum element identification using binary search.
- Learned to calculate rotation count using the minimum element's index.
- Improved understanding of modified binary search techniques.

### Restrictions Followed

- Avoided `bisect`, `bisect_left`, and `bisect_right`.
- Used manual midpoint calculation.
- Identified sorted and unsorted halves through comparisons.
- Avoided linear searching.
- Implemented all searching logic from scratch.
