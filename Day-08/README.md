# Day 8 — Two Pointers Technique

Programming Language: Python

### 1. Valid Palindrome (LeetCode 125)
Approach: Place two pointers at the beginning and end of the string. Ignore special characters and spaces, compare letters without considering case, and move inward.
Time Complexity: O(n)
Space Complexity: O(1)
Edge Case: Strings containing only spaces or punctuation should return `True`.

### 2. Reverse String (LeetCode 344)
Approach: Use two pointers to exchange characters from opposite ends until the pointers meet. Modify the original character array directly.
Time Complexity: O(n)
Space Complexity: O(1)
Edge Case: An empty array or an array with one character needs no changes.

### 3. Reverse Vowels of a String (LeetCode 345)
Approach: Move two pointers inward, skipping non-vowel characters. Swap the vowels encountered at both ends and return the resulting string.
Time Complexity: O(n)
Space Complexity: O(n)
Edge Case: If the string contains no vowels, the original string remains unchanged.
