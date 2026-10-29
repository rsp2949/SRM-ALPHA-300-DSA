# Day 18 — Recursive Merge Sort

**Date:** October 18, 2026  
**Category:** Sorting Algorithms  
**Language:** Python

## Problem 1: Merge Sort
Implemented Merge Sort using recursion and the divide-and-conquer approach. The array is divided into smaller halves, recursively sorted, and merged into a sorted array.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Edge Case:** An empty array or an array containing one element.

## Problem 2: Merge Two Sorted Arrays
Merged two sorted arrays into a single sorted array using two pointers. Remaining elements are appended after one array is exhausted.

- **Time Complexity:** O(n + m)
- **Space Complexity:** O(n + m)
- **Edge Case:** Both arrays are empty or one array is empty.

## Problem 3: Count Inversions in an Array
Modified Merge Sort to count inversions while merging. Whenever an element from the right half is smaller than an element in the left half, the remaining elements in the left half contribute to the inversion count.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Edge Case:** A sorted array has zero inversions, and duplicate elements do not count as inversions.

## Key Concepts Learned
- Divide-and-conquer strategy
- Recursive splitting and merging
- Two-pointer technique
- Counting inversions efficiently during merging

## Restrictions
- No `sorted()`
- No `.sort()`
- No `heapq.merge()`
- Implemented splitting, merging, and inversion counting manually.

## Conclusion
Practiced recursive Merge Sort and learned how its merging process can be extended to solve array problems efficiently.
