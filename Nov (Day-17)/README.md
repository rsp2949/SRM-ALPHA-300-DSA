# Day 17 – String Sliding Window

## Overview

This session focuses on solving string-based problems using the sliding window technique. Character frequencies and positions are maintained throughout the iteration without using built-in frequency counter libraries.

## Problem Summary

| No. | Problem | Technique |
|---|---|---|
| 1 | Longest Substring Without Repeating Characters | Variable Sliding Window |
| 2 | Longest Repeating Character Replacement | Frequency Dictionary |
| 3 | Find All Anagrams in a String | Fixed Sliding Window |

## Implementation Details

### Problem 1 – Longest Substring Without Repeating Characters
- Used a dictionary to store the most recent index of each character.
- Adjusted the left pointer whenever a duplicate appeared within the active window.
- Time Complexity: O(n)
- Space Complexity: O(min(n, k))
- Edge Case: Empty string.

### Problem 2 – Longest Repeating Character Replacement
- Tracked character frequencies while extending the window.
- Reduced the window when the number of required replacements exceeded k.
- Time Complexity: O(n)
- Space Complexity: O(k)
- Edge Case: k = 0 with a string containing different characters.

### Problem 3 – Find All Anagrams in a String
- Created a frequency dictionary for the pattern.
- Maintained a fixed-size window and updated its frequencies incrementally.
- Recorded the starting positions whenever both frequency dictionaries matched.
- Time Complexity: O(n × k) worst case
- Space Complexity: O(k)
- Edge Case: Both strings have different lengths, with the pattern longer than the input string.

## Key Concepts Learned

- Fixed-size and variable-size sliding windows.
- Character frequency management.
- Dictionary updates during traversal.
- Duplicate detection and window adjustment.
- Anagram identification through frequency comparison.

## Learning Outcome

Developed the ability to solve string problems efficiently by maintaining window state and updating character frequencies incrementally rather than repeatedly processing the entire substring.
