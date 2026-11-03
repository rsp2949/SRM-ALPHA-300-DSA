
# Day 25 — Binary Search Variants (Peak + Mountain)

**Programming Language:** Python

### 1. Find Peak Element — LeetCode 162

- **Technique:** Binary Search on Slope
- **Approach:** Compare the middle element with its next element. If the slope is rising, search the right half; otherwise, search the left half to locate a peak.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Peak is at the first or last index.

### 2. Peak Index in a Mountain Array — LeetCode 852

- **Technique:** Binary Search on Mountain Slope
- **Approach:** Identify the increasing and decreasing portions by comparing adjacent elements. Adjust the search range until the maximum element's index is found.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Peak is located near either end of the mountain array.

### 3. Find in Mountain Array — LeetCode 1095

- **Technique:** Three-Stage Binary Search
- **Approach:** First find the mountain peak using slope comparison. Then perform ascending binary search on the left side and descending binary search on the right side to locate the target's smallest index.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Target is absent or appears on both sides of the peak.

### Learning Outcomes

- Understood peak element identification using binary search.
- Learned to identify increasing and decreasing slopes.
- Practiced finding the peak index in a mountain array.
- Applied binary search on both ascending and descending portions.
- Used the MountainArray API to search efficiently.
- Improved understanding of logarithmic-time searching.

### Restrictions Followed

- Avoided `bisect`, `bisect_left`, and `bisect_right`.
- Used manual midpoint calculation.
- Implemented slope-based binary search.
- Avoided linear searching.
- Implemented all searching logic from scratch.
