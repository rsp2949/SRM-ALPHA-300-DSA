
# Day 8 - Reverse Operations

## 1. Reverse Words in a String
- **Technique:** Word Extraction and Two-Pointer Reversal
- **Approach:** Extract individual words by traversing the string character by character. Store them in a list, reverse their positions using two pointers, and combine them with single spaces.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** A string with leading spaces, trailing spaces, and multiple spaces between words.

## 2. Reverse String II
- **Technique:** Block-Based Reversal
- **Approach:** Process the string in groups of 2k characters. Reverse the first k characters in each group using left and right pointers while leaving the remaining k characters unchanged.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** The final block contains fewer than k characters.

## 3. Reverse Only Letters
- **Technique:** Two-Pointer Selective Reversal
- **Approach:** Use two pointers moving from opposite ends. Skip digits and special characters, then swap only alphabetic characters while preserving all non-letter positions.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** A string contains no English letters.

## Learning Outcomes
- Strengthened understanding of string manipulation.
- Practised reversing words without built-in splitting shortcuts.
- Learned to reverse fixed-size portions of a string.
- Applied two pointers to selective character swapping.
- Used ASCII ranges to distinguish English letters.
- Understood how to preserve characters that should not be modified.

## Restrictions Followed
- No s[::-1].
- No reversed().
- No s.split()[::-1].
- No str.translate().
- No built-in reversal shortcuts.
- Used manual loops and two-pointer swapping.
- Used lists and join() for string construction.
