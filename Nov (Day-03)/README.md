# Day 3 – Character Frequency Counting

## 1. Valid Anagram
- **Technique:** Frequency Dictionary
- **Approach:** Build a frequency dictionary for the first string. Traverse the second string and decrease the corresponding character counts. If a character is missing or has no remaining count, return False.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(k), where k is the number of distinct characters.
- **Edge Case:** Both strings have equal lengths but different character frequencies.

## 2. Group Anagrams
- **Technique:** Hash Map + Frequency Signature
- **Approach:** Build a 26-position frequency array for every word. Convert it into a tuple and use it as a dictionary key to group words with identical character frequencies.
- **Time Complexity:** O(n × k), where n is the number of words and k is the maximum word length.
- **Auxiliary Space:** O(n × 26) for frequency signatures and groups, excluding output.
- **Edge Case:** Empty strings or words containing repeated characters.

## 3. First Unique Character in a String
- **Technique:** Frequency Dictionary + Linear Traversal
- **Approach:** Count every character using a dictionary. Traverse the string again and return the index of the first character with frequency 1.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(k), where k is the number of distinct characters.
- **Edge Case:** All characters repeat, so return -1.

## Learning Outcomes
- Learned to construct frequency dictionaries manually.
- Practiced counting and comparing character frequencies.
- Understood anagram grouping using frequency signatures.
- Learned to find the first unique character.
- Practiced using tuples as dictionary keys.

## Restrictions Followed
- No collections.Counter used.
- No Counter.most_common() used.
- Frequency dictionaries built manually.
- No built-in sorting used.
- No unnecessary library imports.
- Only primitive data structures used.
