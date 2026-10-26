# Day 15 — Sorting Algorithms from Scratch

**Programming Language:** Python

### 1. Basic Bubble Sort
- **Technique:** Repeated adjacent comparisons
- **Approach:** Traverse the array multiple times, swapping neighboring values whenever they are in the wrong order. Reduce the comparison range after each pass.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Special Case:** An array with one element is already sorted.

### 2. Optimized Bubble Sort
- **Technique:** Early termination
- **Approach:** Introduce a Boolean flag to detect whether any swap occurs during a pass. Terminate early when the array is sorted.
- **Best-Case Time:** O(n)
- **Worst-Case Time:** O(n²)
- **Auxiliary Space:** O(1)
- **Special Case:** An already sorted array finishes after one pass.

### 3. Parity Ordering with Bubble Sort
- **Technique:** Condition-based adjacent swapping
- **Approach:** Use Bubble Sort's nested-loop structure, but swap only when an odd element is immediately followed by an even element. This places even values before odd values.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Special Case:** Arrays containing only even or only odd numbers need no swaps.

### Learning Outcomes
- Understood how Bubble Sort moves elements through repeated passes.
- Improved efficiency using early-exit detection.
- Applied adjacent swapping to satisfy a custom ordering condition.

### Restrictions Followed
- Avoided built-in sorting functions.
- Used nested loops and manual swaps.
- Implemented each sorting operation from scratch.
