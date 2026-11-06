# Day 6 – Palindrome Variants

## 1. Valid Palindrome II
- **Technique:** Two Pointers + One Deletion
- **Approach:** Compare characters from both ends. When a mismatch occurs, check whether skipping the left character or skipping the right character produces a palindrome. Only one deletion is allowed.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Edge Case:** A string that is already a palindrome requires no deletion.

## 2. Longest Palindrome
- **Technique:** Character Frequency Counting
- **Approach:** Build a frequency dictionary manually. Use the largest even portion of every character frequency to construct the palindrome. If any odd frequency exists, one character can occupy the center.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(k), where k is the number of distinct characters.
- **Edge Case:** A string containing only one character.

## 3. Palindrome Permutation
- **Technique:** Frequency Dictionary + Odd Count
- **Approach:** Count the frequency of every character. A palindrome permutation is possible when at most one character has an odd frequency.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(k), where k is the number of distinct characters.
- **Edge Case:** A string with more than one odd-frequency character.

## Learning Outcomes
- Practiced palindrome validation with one allowed deletion.
- Learned to construct palindrome length using character frequencies.
- Understood the relationship between odd and even character frequencies.
- Practiced manual frequency dictionary construction.
- Learned to identify whether a palindrome permutation is possible.

## Restrictions Followed
- No s[::-1] used.
- No reversed() used.
- No collections.Counter used.
- No built-in string reversal used.
- Frequency dictionaries implemented manually.
- Two-pointer traversal implemented manually.
- Only primitive data structures used.
