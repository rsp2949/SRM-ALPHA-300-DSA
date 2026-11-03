# Day 30 – Sort + Binary Search Combo

## 1. Longest Consecutive Sequence
- **Technique:** Custom Merge Sort + Binary Search
- **Approach:** Sort the array using Merge Sort and remove duplicates. Use binary search to check whether a number has a predecessor. For sequence starting elements, repeatedly search for the next consecutive number and calculate the maximum length.
- **Time Complexity:** O(n log n)
- **Auxiliary Space:** O(n)
- **Special Case:** Empty array returns 0. Duplicate numbers are removed before searching.

## 2. 3Sum
- **Technique:** Custom Merge Sort + Two Pointers
- **Approach:** Sort the array using Merge Sort. Fix one element and use left and right pointers to find pairs that make the total sum zero. Skip duplicate elements to avoid repeated triplets.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(n) for Merge Sort, excluding output.
- **Special Case:** Duplicate triplets must not be included.

## 3. Two Sum II – Input Array Is Sorted
- **Technique:** Two Pointers
- **Approach:** Start with pointers at both ends of the sorted array. Move the left pointer forward when the sum is smaller than the target and move the right pointer backward when the sum is greater. Return the positions using 1-based indexing.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Special Case:** Return 1-based indices as required by LeetCode.

## Learning Outcomes
- Practiced custom Merge Sort.
- Implemented manual binary search on a sorted array.
- Learned how sorting helps solve consecutive sequence problems.
- Understood the two-pointer technique for 3Sum.
- Practiced duplicate handling in sorted arrays.
- Applied two pointers to solve Two Sum II efficiently.

## Restrictions Followed
- No .sort() used.
- No sorted() used.
- No bisect used.
- Custom Merge Sort implemented manually.
- Binary Search implemented manually.
- Two-pointer technique implemented manually.
- No unnecessary extra data structures used.
