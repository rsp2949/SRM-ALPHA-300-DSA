# Day 1 – Length, Concatenation and Basic String Operations

## 1. Length of Last Word
- **Technique:** Reverse Traversal and Character Counting
- **Approach:** Traverse the string from the end. Skip trailing spaces and count characters until another space or the beginning of the string.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Edge Case:** String contains trailing spaces or multiple spaces between words.

## 2. Longest Common Prefix
- **Technique:** Character-by-Character Comparison
- **Approach:** Use the first string as the reference. Compare each character with the corresponding position in every other string. Store matching characters in a list and join once.
- **Time Complexity:** O(n × m)
- **Auxiliary Space:** O(m)
- **Edge Case:** One string is empty or there is no common prefix.

## 3. Count and Say
- **Technique:** String Traversal and Run-Length Counting
- **Approach:** Start with "1". Count consecutive identical characters in the current term and append the count followed by the character using a list. Join to generate the next term.
- **Time Complexity:** Proportional to the total length of generated terms.
- **Auxiliary Space:** O(L), where L is the maximum generated term length.
- **Edge Case:** n = 1, which must return "1".

## Learning Outcomes
- Practiced string traversal from both directions.
- Learned character-by-character comparison.
- Understood consecutive character counting.
- Practiced building strings using lists and join().
- Learned how to generate strings iteratively.

## Restrictions Followed
- No collections.Counter.
- No reversed().
- No string slicing reversal.
- No unnecessary library imports.
- Dynamic strings built using lists and join().
- Only primitive data structures used.
