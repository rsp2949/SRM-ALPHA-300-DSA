# Day 29 – Sort + Merge Intervals

## 1. Merge Intervals
- **Technique:** Merge Sort + Interval Merging
- **Approach:** Sort intervals by starting value using custom Merge Sort. Compare each interval with the last merged interval. If they overlap, extend the ending value; otherwise, add a new interval.
- **Time Complexity:** O(n log n)
- **Auxiliary Space:** O(n)
- **Special Case:** Empty interval list returns an empty list.

## 2. Insert Interval
- **Technique:** Linear Traversal + Interval Merging
- **Approach:** Use the existing sorted order. Add intervals before the new interval, merge overlapping intervals, and append the remaining intervals.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n) for the output list.
- **Special Case:** New interval does not overlap with any existing interval.

## 3. Non-overlapping Intervals
- **Technique:** Merge Sort + Greedy Algorithm
- **Approach:** Sort intervals by ending value using custom Merge Sort. Select the interval that finishes earliest and remove overlapping intervals to minimize removals.
- **Time Complexity:** O(n log n)
- **Auxiliary Space:** O(n)
- **Special Case:** Intervals touching at endpoints are considered non-overlapping.

## Learning Outcomes
- Learned how to merge overlapping intervals.
- Practiced implementing Merge Sort without built-in sorting.
- Understood insertion and merging of intervals.
- Learned greedy interval scheduling.
- Understood why sorting by ending time helps minimize removals.

## Restrictions Followed
- No .sort() used.
- No sorted() used.
- Custom Merge Sort implemented manually.
- No bisect used.
- No built-in sorting shortcuts used.
- Interval merging implemented manually.
