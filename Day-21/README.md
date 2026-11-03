
# Day 21 — Sorting Consolidation and Dutch National Flag

**Programming Language:** Python

### 1. Sort Colors — LeetCode 75

- **Technique:** Dutch National Flag Algorithm (3-way partition)
- **Approach:** Use three pointers: low, mid, and high. Move zeros to the beginning, keep ones in the middle, and move twos to the end using manual swapping.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Special Case:** Array containing only zeros, ones, or twos.

### 2. Wiggle Sort I — LeetCode 280

- **Technique:** Insertion Sort and adjacent swapping
- **Approach:** First sort the array using manual Insertion Sort. Then swap elements at consecutive odd and even positions to create the required wiggle pattern.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Special Case:** Empty array, single element, or an already sorted array.

### 3. Sort Array by Increasing Frequency — LeetCode 1636

- **Technique:** Frequency counting and Insertion Sort
- **Approach:** Build a frequency dictionary manually. Sort elements by increasing frequency. When frequencies are equal, place the larger element first using manual comparisons and shifting.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(k), where k is the number of distinct elements.
- **Special Case:** All elements have the same frequency or the array contains repeated elements.

### Learning Outcomes

- Implemented the Dutch National Flag algorithm using three pointers.
- Consolidated manual Insertion Sort from previous days.
- Practiced creating wiggle patterns through adjacent swapping.
- Used dictionaries for manual frequency counting.
- Applied custom sorting conditions based on frequency and element values.

### Restrictions Followed

- Avoided `.sort()` and `sorted()`.
- Used manually implemented Insertion Sort.
- Avoided built-in sorting shortcuts.
- Used manual frequency counting and comparisons.
- Implemented all sorting and rearrangement logic from scratch.
