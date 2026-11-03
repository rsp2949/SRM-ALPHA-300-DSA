# Day 27 – Binary Search in 2D Matrix

## 1. Search a 2D Matrix
- **Technique:** Binary Search using 1D index mapping
- **Approach:** Treat the matrix as a virtual sorted 1D array. Convert the middle index into row and column using division and modulo. Apply binary search to locate the target.
- **Time Complexity:** O(log(m × n))
- **Auxiliary Space:** O(1)
- **Special Case:** Target is not present in the matrix.

## 2. Row with Maximum Ones
- **Technique:** Binary Search on Each Row
- **Approach:** Find the first occurrence of 1 in every sorted row. Calculate the number of ones and track the row with the maximum count.
- **Time Complexity:** O(rows × log(cols))
- **Auxiliary Space:** O(1)
- **Special Case:** Matrix contains no ones. Return -1.

## 3. Peak Element in 1D Array
- **Technique:** Binary Search on Slope
- **Approach:** Compare the middle element with its next element. If the next element is greater, move right; otherwise, move left. Continue until the peak index is found.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Special Case:** Peak occurs at the first or last index.

## Learning Outcomes
- Learned to apply binary search directly on a 2D matrix.
- Understood row and column mapping using division and modulo.
- Practiced binary search on individual sorted rows.
- Learned to identify peak elements using slope-based binary search.
- Improved understanding of logarithmic search techniques.

## Restrictions Followed
- No NumPy used.
- No flatten() used.
- No bisect used.
- No built-in sorting used.
- Binary search implemented manually.
- Constant auxiliary space maintained where possible.
