# Day 17 — Manual Insertion and Array Sorting

**Programming Language:** Python

### 1. Basic Insertion Sort
- **Technique:** Shifting and insertion
- **Approach:** Maintain a sorted prefix and insert each remaining element into its appropriate position by shifting larger values one place to the right.
- **Time Complexity:** O(n) best case, O(n²) worst case
- **Auxiliary Space:** O(1)
- **Special Case:** An empty array requires no operations.

### 2. Insertion Sort on Nearly-Sorted Array
- **Technique:** Adaptive insertion
- **Approach:** Process the array from left to right and shift only those elements that are larger than the current key. Nearly sorted inputs require fewer shifts.
- **Time Complexity:** O(n) best case, O(n²) worst case
- **Auxiliary Space:** O(1)
- **Special Case:** The array is already in ascending order.

### 3. Sort Colors — LeetCode 75
- **Technique:** Insertion sort with restricted values
- **Approach:** Sort the array in place by repeatedly shifting larger elements and inserting the current value. The allowed values are 0, 1, and 2.
- **Time Complexity:** O(n) best case, O(n²) worst case
- **Auxiliary Space:** O(1)
- **Special Case:** All elements are already in the correct order.

