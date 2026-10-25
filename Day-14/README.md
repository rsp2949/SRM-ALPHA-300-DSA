# Day 14 — Window Constraints and Frequency Tracking

**Programming Language:** Python

### 1. Max Consecutive Ones III — LeetCode 1004
- **Technique:** Sliding window with zero counting
- **Approach:** Expand the window while counting zeros. When the zero count exceeds `k`, move the left pointer until the window becomes valid again.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Edge Case:** The array contains only zeros or only ones.

### 2. Longest Repeating Character Replacement — LeetCode 424
- **Technique:** Sliding window with frequency tracking
- **Approach:** Maintain character frequencies and the highest frequency observed. Calculate the number of replacements needed and shrink the window whenever it exceeds `k`.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) for the fixed uppercase English alphabet.
- **Edge Case:** No replacements are allowed, so only an existing sequence of identical characters can be selected.

### 3. Longest Substring Without Repeating Characters — LeetCode 3
- **Technique:** Sliding window with last-seen indices
- **Approach:** Record each character's latest position. When a repeated character appears within the current window, advance the left pointer beyond its previous occurrence.
- **Time Complexity:** O(n) average
- **Space Complexity:** O(min(n, Σ))
- **Edge Case:** An empty string returns 0.
