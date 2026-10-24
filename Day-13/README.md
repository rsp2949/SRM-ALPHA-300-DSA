# Day 13 — Hashmap-Based Sliding Window

**Programming Language:** Python

### 1. Contains Duplicate II — LeetCode 219
- **Technique:** Hashmap with index tracking
- **Approach:** Record each number's latest position. When a duplicate is encountered, calculate the distance between the indices and check whether it is within `k`.
- **Time Complexity:** O(n) average
- **Space Complexity:** O(n)
- **Edge Case:** The same value appears multiple times, but no pair of occurrences is within the allowed distance.

### 2. Find All Anagrams in a String — LeetCode 438
- **Technique:** Fixed-size sliding window with frequency counting
- **Approach:** Count the pattern's characters and maintain the frequency of characters in a window of equal length. Add the starting index whenever the frequencies match.
- **Time Complexity:** O(n + m) average for a bounded character set
- **Space Complexity:** O(m + Σ)
- **Edge Case:** The pattern is longer than the source string.

### 3. Permutation in String — LeetCode 567
- **Technique:** Fixed-size sliding window and hashmap
- **Approach:** Track character frequencies in the target and current window. Move the window across the source string and return `True` when the frequency counts match.
- **Time Complexity:** O(n + m) average for a bounded character set
- **Space Complexity:** O(m + Σ)
- **Edge Case:** The source string is shorter than the target string.

### Learning Outcome
Practiced tracking repeated elements with index maps and using frequency dictionaries to identify anagrams and permutations efficiently.
