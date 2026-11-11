
# Day 11 - String Rotation

## 1. Rotate String
- **Technique:** Circular String Matching
- **Approach:** Check every possible starting index in the original string. Compare characters using modular indexing to determine whether the target string can be formed through rotation.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Edge Case:** Both strings have equal lengths but contain different characters.

## 2. Shift 2D Grid
- **Technique:** Flattening and Index Transformation
- **Approach:** Convert the matrix into a one-dimensional list, calculate each element's new position using modular arithmetic, and reconstruct the shifted matrix with its original dimensions.
- **Time Complexity:** O(m × n)
- **Auxiliary Space:** O(m × n)
- **Edge Case:** The shift count is a multiple of the total number of elements.

## 3. Rotate String by K
- **Technique:** Modular Position Mapping
- **Approach:** Normalize the rotation count using modulo string length. Calculate the destination index for each character and place it directly into the result list to perform a right rotation.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** Rotation count is zero or greater than the string length.

## Learning Outcomes
- Developed an understanding of circular indexing.
- Applied modulo operations to string rotation.
- Practised comparing strings without concatenation-based shortcuts.
- Learned to transform 2D grids through linear indexing.
- Improved understanding of right and left rotations.
- Strengthened array and string index manipulation skills.

## Restrictions Followed
- No `s in (s + s)` rotation shortcut.
- No reverse slicing.
- No `reversed()`.
- Used modular index traversal for rotation checking.
- Used manual loops for position mapping.
- Used lists and `join()` for string construction.
- Avoided external libraries and prohibited shortcuts.
