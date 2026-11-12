
# Day 12 - String Compression and Encoding

## 1. String Compression
- **Technique:** Run-Length Encoding (RLE)
- **Approach:** Traverse the character array and identify consecutive groups of identical characters. Count each group manually and overwrite the array with the character followed by its frequency when the count exceeds one.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(log n) for temporary storage of count digits.
- **Edge Case:** A character repeats more than nine times and its frequency requires multiple digits.

## 2. Encode and Decode Strings
- **Technique:** Length-Based String Encoding
- **Approach:** Store every string with its length and a delimiter before the actual content. During decoding, read the length first and extract exactly the specified number of characters to recover the original strings.
- **Time Complexity:** O(n), where n represents the total input and output size.
- **Auxiliary Space:** O(n) for constructing the encoded or decoded result.
- **Edge Case:** Input contains empty strings, spaces, or the delimiter character itself.

## 3. Count and Say
- **Technique:** Iterative Run Counting
- **Approach:** Generate each sequence term from the previous term by counting consecutive identical digits. Append the frequency and digit to a temporary list and join the elements to create the next term.
- **Time Complexity:** Proportional to the total length of all generated terms.
- **Auxiliary Space:** O(L), where L is the current generated term's length.
- **Edge Case:** When n = 1, return the initial sequence "1".

## Learning Outcomes
- Learned the fundamentals of run-length encoding.
- Practised consecutive character frequency counting.
- Implemented in-place compression with read and write pointers.
- Understood length-prefix encoding and decoding.
- Learned to handle delimiters safely within encoded data.
- Practised iterative sequence generation.
- Improved string traversal and memory management skills.

## Restrictions Followed
- Did not use itertools.groupby().
- Did not use collections.Counter.
- Counted consecutive character runs using manual loops.
- Used read and write pointers for string compression.
- Used length-prefix encoding for string serialization.
- Used lists and join() for efficient string construction.
- Avoided external libraries and prohibited shortcuts.
