
# Day 9 - Reverse by Chunks / Per-Word

## 1. Reverse Words in a String III
- **Technique:** Segment-Based String Reversal
- **Approach:** Convert the sentence into a character list and traverse it to detect word boundaries. Reverse each word independently using left and right pointers without changing the positions of spaces.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** A sentence contains a single word or words of different lengths.

## 2. Reverse Prefix of Word
- **Technique:** First Occurrence Search and Prefix Reversal
- **Approach:** Search for the first occurrence of the specified character. Use two pointers to reverse the prefix ending at that position while keeping the remaining characters unchanged.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** The specified character is absent from the input word.

## 3. Reverse Vowels of a String
- **Technique:** Two-Pointer Character Swapping
- **Approach:** Traverse the string from both ends and identify vowels. Skip consonants and special characters, then swap the vowels until both pointers meet.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** The input contains no vowels or contains only one vowel.

## Learning Outcomes
- Improved understanding of character-level string manipulation.
- Learned to reverse multiple word segments independently.
- Practised locating a character and reversing a prefix.
- Applied two-pointer techniques for selective reversal.
- Understood how to preserve non-target characters.
- Strengthened boundary detection and manual traversal skills.

## Restrictions Followed
- No reverse slicing such as [::-1].
- No reversed().
- No list comprehension with reverse slicing.
- Used manual character-by-character processing.
- Applied two-pointer swapping wherever required.
- Used lists and join() for constructing output strings.
- Avoided external libraries and prohibited shortcuts.
