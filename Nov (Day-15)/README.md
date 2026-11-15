
# Day 15 - Pattern Matching (Naive strStr)

## 1. Find the Index of the First Occurrence (strStr)
- **Technique:** Brute Force String Matching
- **Approach:** Check each possible starting position in the main string and compare the target pattern character by character. Return the first valid matching index or -1 if no occurrence exists.
- **Time Complexity:** O(n × m)
- **Auxiliary Space:** O(1)
- **Edge Case:** The target pattern is longer than the main string or is empty.

## 2. Repeated Substring Pattern
- **Technique:** Pattern Repetition and Modular Arithmetic
- **Approach:** Generate possible pattern lengths that divide the original string length. Compare each character against the corresponding position in the candidate repeating pattern using modulo indexing.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Edge Case:** The string contains no repeating substring that can form the complete sequence.

## 3. Rotate String (via Substring Match)
- **Technique:** Circular String Matching
- **Approach:** Create a doubled version of the original string to represent its possible circular rotations. Apply the manually implemented pattern-matching algorithm to locate the target string within the doubled string.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(n)
- **Edge Case:** The strings have different lengths or both strings are empty.

## Learning Outcomes
- Developed an understanding of naive pattern matching.
- Practised character comparison using nested loops.
- Learned to identify substring occurrences without built-in search methods.
- Applied modulo operations to detect repeating patterns.
- Understood the relationship between string rotation and substring matching.
- Reused a common matching algorithm across multiple problems.

## Restrictions Followed
- No s.find().
- No s.index().
- No re.search().
- No built-in substring search.
- Used explicit nested loops for pattern matching.
- Used modular indexing for repetition checking.
- Reused the manual strStr implementation for rotation validation.
- Avoided external libraries and prohibited shortcuts.

## Key Takeaways
- Check every possible starting position when using naive matching.
- Compare characters until a mismatch or complete match occurs.
- A repeating substring must divide the original string length.
- Circular rotations can be checked through substring matching.
- Reusing a manually implemented algorithm improves problem-solving efficiency.
