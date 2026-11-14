
# Day 14 - Common Prefix and Suffix

## 1. Longest Common Prefix
- Technique: Character-by-Character Comparison
- Approach: Use the first string as a reference and compare its characters with every other string at the same index. Stop when a mismatch or the end of a string is reached and return the matching prefix.
- Time Complexity: O(N × L), where N is the number of strings and L is the shortest string length.
- Auxiliary Space: O(L) for the prefix list.
- Edge Case: One string is empty or the strings have no common starting characters.

## 2. Longest Common Suffix
- Technique: Backward String Traversal
- Approach: Compare characters from the end of every string using backward indexing. Stop at the first mismatch and manually reverse the collected characters to construct the common suffix.
- Time Complexity: O(N × L), where N is the number of strings and L is the shortest string length.
- Auxiliary Space: O(L) for the suffix list.
- Edge Case: One string is shorter than the common suffix candidate or the strings have no common ending characters.

## 3. Check If Prefix of String
- Technique: Sequential Character Matching
- Approach: First verify that the prefix length does not exceed the original string length. Compare each prefix character with the corresponding character in the original string and return False immediately when a mismatch occurs.
- Time Complexity: O(P), where P is the prefix length.
- Auxiliary Space: O(1).
- Edge Case: The prefix is longer than the original string or is an empty string.

## Learning Outcomes
- Understood the difference between prefixes and suffixes.
- Practised comparing multiple strings manually.
- Learned forward and backward character traversal.
- Applied index-based comparison without built-in shortcuts.
- Implemented early termination when a mismatch occurs.
- Improved string boundary checking and traversal skills.

## Restrictions Followed
- Did not use os.path.commonprefix().
- Did not use zip(*strs).
- Used explicit nested loops for string comparison.
- Used manual backward traversal for suffix matching.
- Did not use reverse slicing or reversed().
- Used lists and join() for constructing results.
- Avoided external libraries and prohibited shortcuts.

## Key Takeaways
- Prefix comparison starts from index 0.
- Suffix comparison starts from the last index.
- Prefix checking requires only one traversal.
- Early termination avoids unnecessary comparisons.
- Manual indexing helps understand string matching algorithms.
