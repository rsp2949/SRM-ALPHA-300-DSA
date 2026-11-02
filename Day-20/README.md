
# Day 20 — Counting Sort and Frequency-Based Sorting

**Programming Language:** Python

### 1. Counting Sort — GeeksforGeeks

- **Technique:** Frequency counting
- **Approach:** Create a count array of 26 positions to store the frequency of each lowercase English character. Reconstruct the sorted string using the count array.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Special Case:** Empty string or a string containing repeated characters.

### 2. Sort Colors — LeetCode 75

- **Technique:** Counting Sort
- **Approach:** Count the occurrences of 0, 1, and 2 using a fixed-size count array. Rewrite the original array in ascending order based on their frequencies.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Special Case:** Array containing only one type of element.

### 3. Segregate 0s and 1s — GeeksforGeeks

- **Technique:** Frequency counting and array rearrangement
- **Approach:** Count the number of zeros in the array. Place zeros first and fill the remaining positions with ones.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Special Case:** Array containing all zeros or all ones.

### Learning Outcomes

- Understood the working principle of Counting Sort.
- Practiced building frequency arrays manually.
- Applied counting techniques to strings and integer arrays.
- Learned to rearrange arrays without using built-in sorting functions.
- Improved understanding of linear-time sorting for restricted input ranges.

### Restrictions Followed

- Avoided `.sort()`, `sorted()`, and `collections.Counter`.
- Built all frequency arrays manually.
- Used basic Python lists, loops, and conditions.
- Implemented all sorting and rearrangement logic from scratch.
