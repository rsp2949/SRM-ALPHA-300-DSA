
# Day 10 - Split, Trim, Rejoin

## 1. Length of Last Word
- **Technique:** Backward String Traversal
- **Approach:** Start scanning from the last character and ignore trailing spaces. Count the characters of the final word until a space or the beginning of the string is reached.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Edge Case:** A string containing multiple trailing spaces.

## 2. Shortest Distance to a Character
- **Technique:** Bidirectional Traversal
- **Approach:** Calculate distances using two passes through the string. The forward pass finds the nearest target character on the left, while the backward pass checks the nearest target character on the right and keeps the smaller distance.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** The target character appears only once in the string.

## 3. Goal Parser Interpretation
- **Technique:** Index-Based Pattern Matching
- **Approach:** Read the command character by character and identify the three valid patterns. Convert each pattern into its corresponding output and combine the collected characters using join().
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** The command contains repeated empty-parenthesis patterns.

## Learning Outcomes
- Improved understanding of whitespace handling.
- Learned to process strings from right to left.
- Practised calculating minimum distances with two traversals.
- Developed index-based pattern recognition.
- Compared manual string processing with built-in split().
- Improved efficient output construction using lists and join().

## Restrictions Followed
- Built a manual loop-based approach for word processing.
- Did not rely exclusively on split().
- Avoided reverse slicing and reversed().
- Used manual indexing and conditional checks.
- Used lists and join() for output construction.
- Avoided external libraries and unnecessary shortcuts.
