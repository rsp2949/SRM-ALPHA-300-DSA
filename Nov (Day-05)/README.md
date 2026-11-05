# Day 5 – Palindromes: Two Pointers from Ends

## Problem 1: Valid Palindrome
- **Technique:** Two-Pointer Character Comparison
- **Approach:** Use left and right pointers to compare characters from opposite ends. Skip spaces and special characters, and manually convert uppercase letters into lowercase using ASCII values before comparing.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)
- **Edge Case:** A string containing only spaces or special characters should return True.

## Problem 2: Palindrome Number
- **Technique:** Arithmetic Digit Reversal
- **Approach:** Check negative numbers and trailing zeroes first. Extract digits using modulo and reverse only half the number using multiplication and integer division. Compare the two halves to determine whether the number is a palindrome.
- **Time Complexity:** O(log n)
- **Auxiliary Space:** O(1)
- **Edge Case:** Zero is a palindrome, but negative numbers are not.

## Problem 3: Count Palindromic Substrings
- **Technique:** Expand Around Center
- **Approach:** Consider every character and every gap between adjacent characters as a possible center. Expand left and right while characters match, counting each valid substring.
- **Time Complexity:** O(n²)
- **Auxiliary Space:** O(1)
- **Edge Case:** Repeated characters create multiple overlapping palindromic substrings.

## Learning Outcomes
- Improved understanding of two-pointer traversal.
- Learned palindrome validation without reversing strings.
- Practiced digit manipulation using arithmetic operations.
- Understood the difference between odd-length and even-length palindromes.
- Learned to count all palindrome occurrences using center expansion.

## Restrictions Followed
- No slicing reversal (`[::-1]`).
- No reversed().
- No string conversion for reversing integers.
- No unnecessary imports.
- Manual pointer movement and character comparison.
- Primitive operations and data structures only.
