# Day 2 – Character Transformation

## 1. To Lower Case
- **Technique:** ASCII Character Conversion
- **Approach:** Traverse each character and check its ASCII value using ord(). If it is uppercase, add 32 and convert it back using chr().
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** String contains only lowercase letters or numbers.

## 2. Capitalize the Title
- **Technique:** ASCII Conversion + Word Processing
- **Approach:** Build each word manually. Convert every character to lowercase for words of length 1 or 2. For longer words, capitalize the first character and lowercase the remaining characters.
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** Words containing only one or two characters.

## 3. Defanging an IP Address
- **Technique:** Character Traversal and String Building
- **Approach:** Traverse the IP address. Replace every dot with [.] and preserve all other characters using a result list and join().
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(n)
- **Edge Case:** IP address contains multiple dots.

## Learning Outcomes
- Understood ASCII values of uppercase and lowercase letters.
- Practiced ord() and chr() for character conversion.
- Learned manual word processing.
- Practiced character replacement without built-in shortcuts.
- Understood efficient string construction using lists.

## Restrictions Followed
- No lower() used.
- No upper() used.
- No swapcase() used.
- No unnecessary library imports.
- Character transformations implemented manually.
- Strings built using lists and join().
