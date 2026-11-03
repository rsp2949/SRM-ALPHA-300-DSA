# Day 28 – Binary Search on Condition (Parametric Search)

## 1. Capacity to Ship Packages Within D Days
- **Technique:** Binary Search on Answer
- **Approach:** Search between the heaviest package and the total package weight. Use a feasibility function to check whether all packages can be shipped within the given number of days for a selected capacity.
- **Time Complexity:** O(n × log(sum(weights)))
- **Auxiliary Space:** O(1)
- **Special Case:** Capacity cannot be smaller than the heaviest package.

## 2. Koko Eating Bananas
- **Technique:** Binary Search on Answer
- **Approach:** Search for the minimum eating speed between 1 and the largest pile. Calculate the total hours using ceiling division and check whether Koko can finish within the given hours.
- **Time Complexity:** O(n × log(max(piles)))
- **Auxiliary Space:** O(1)
- **Special Case:** A speed of 1 may require more hours than available.

## 3. Allocate Minimum Pages
- **Technique:** Binary Search on Answer
- **Approach:** Search between the largest book and the total pages. Use a feasibility function to check whether books can be allocated in continuous order to at most k students without exceeding the selected page limit.
- **Time Complexity:** O(n × log(sum(arr)))
- **Auxiliary Space:** O(1)
- **Special Case:** If the number of students is greater than the number of books, return -1.

## Learning Outcomes
- Understood binary search on answer.
- Learned how to create feasibility functions.
- Practiced finding minimum feasible values.
- Understood monotonic conditions in binary search.
- Applied parametric search to allocation and scheduling problems.

## Restrictions Followed
- No bisect used.
- No built-in binary search used.
- Feasibility checks implemented manually.
- Ceiling division implemented using integer arithmetic.
- No unnecessary extra arrays or data structures used.
