# Day 19 — Quick Sort and Partitioning

**Date:** October 19, 2026  
**Topic:** Quick Sort Implementation  
**Programming Language:** Python

## 1. Quick Sort
Implemented Quick Sort using two different partitioning techniques: Lomuto and Hoare. Both approaches recursively divide the array around a pivot to achieve sorting.

- Average Time: O(n log n)
- Worst Time: O(n²)
- Space: O(log n) average
- Edge Case: Already sorted array.

## 2. Quick Sort with 3-way Partition
Implemented three-way partitioning using three pointers. The array is separated into smaller-than-pivot, equal-to-pivot, and greater-than-pivot sections.

- Average Time: O(n log n)
- Worst Time: O(n²)
- Space: O(log n) average
- Edge Case: All elements are identical.

## 3. Kth Largest Element in Array
Solved the problem using the Quickselect algorithm. Instead of completely sorting the array, partitioning is repeated only on the required side until the kth largest element is found.

- Average Time: O(n)
- Worst Time: O(n²)
- Auxiliary Space: O(1)
- Edge Case: Single-element array.

## What I Learned
- Understanding pivot selection and partitioning.
- Comparing Lomuto and Hoare partition schemes.
- Handling duplicate values using three-way partitioning.
- Applying Quickselect to find the kth largest element.
- Improving efficiency by avoiding unnecessary full sorting.

## Implementation Rules
- No built-in sorting methods.
- No `sorted()` or `.sort()`.
- Manual partition implementation.
- Recursive implementation of Quick Sort.
