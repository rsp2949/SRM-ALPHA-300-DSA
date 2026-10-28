# Day 16 — Manual Sorting and Frequency Counting

**Programming Language:** Python

### 1. Basic Selection Sort
- **Technique:** Minimum selection and swapping
- **Approach:** Find the smallest value in the unsorted section during each pass and move it to its correct position.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Special Case:** An empty or single-element array requires no swaps.

### 2. K Smallest Elements Using Selection Sort
- **Technique:** Partial selection sort
- **Approach:** Execute only `k` passes instead of sorting the entire array. Collect the first `k` elements as the result.
- **Time Complexity:** O(nk)
- **Auxiliary Space:** O(k) for the result.
- **Special Case:** When `k` equals the array length, all elements are returned in ascending order.

### 3. Sort Characters By Frequency — LeetCode 451
- **Technique:** Hashmap counting and selection sort
- **Approach:** Build a frequency dictionary, manually arrange the distinct characters by their counts, and construct the final string using repeated characters.
- **Time Complexity:** O(n + u²)
- **Auxiliary Space:** O(n + u)
- **Special Case:** Characters with equal frequencies can appear in either order.
