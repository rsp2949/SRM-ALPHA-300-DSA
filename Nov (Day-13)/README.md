
# Day 13 - Isomorphism (Bijective Dictionary Pattern)

## 1. Isomorphic Strings
- **Technique:** Bidirectional Character Mapping
- **Approach:** Maintain two dictionaries to record character relationships between both strings. Traverse the strings and verify that every source character maps consistently to one target character and that no target character is assigned to multiple source characters.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1) for a fixed character set.
- **Edge Case:** Two different characters in the first string attempt to map to the same character in the second string.

## 2. Word Pattern
- **Technique:** Bijective Word Mapping
- **Approach:** Extract the words from the sentence and compare them with the pattern characters at corresponding positions. Use two dictionaries to maintain consistent mappings between pattern characters and complete words.
- **Time Complexity:** O(n + m), where n is the pattern length and m is the sentence length.
- **Auxiliary Space:** O(n) for storing words and mappings.
- **Edge Case:** The pattern contains four characters but the sentence contains only three words.

## 3. Find and Replace Pattern
- **Technique:** Reusable Two-Dictionary Pattern Matching
- **Approach:** Examine every candidate word independently. Create fresh forward and reverse dictionaries for each word, validate every character mapping, and collect only the words that satisfy the given pattern.
- **Time Complexity:** O(W × L), where W is the number of words and L is the maximum word length.
- **Auxiliary Space:** O(L) for temporary dictionaries.
- **Edge Case:** A candidate word has a different repetition structure from the pattern.

## Learning Outcomes
- Understood bijective relationships between characters.
- Learned to maintain forward and reverse mappings.
- Practised mapping individual characters to complete words.
- Applied dictionary-based validation to multiple candidate strings.
- Identified conflicts caused by repeated characters.
- Improved manual traversal and dictionary lookup techniques.

## Restrictions Followed
- Did not use zip().
- Did not use zip() with set() for mapping validation.
- Implemented two dictionaries explicitly.
- Checked both forward and reverse mappings.
- Used manual index-based traversal.
- Created fresh dictionaries for each candidate word.
- Avoided Counter and external libraries.

## Key Takeaways
- A one-to-one mapping must work in both directions.
- Equal lengths are necessary before comparing character mappings.
- Repeated characters must always preserve their original mapping.
- Each candidate word must be checked independently.
