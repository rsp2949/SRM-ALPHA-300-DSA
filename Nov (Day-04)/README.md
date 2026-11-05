# Day 4 – Character Counting Advanced

## 1. Ransom Note
- **Technique:** Two Frequency Dictionaries
- **Approach:** Build separate frequency dictionaries for the magazine and ransom note. Compare the required count of every note character against the available magazine count.
- **Time Complexity:** O(n + m)
- **Auxiliary Space:** O(k)
- **Edge Case:** A character is required more times than it appears in the magazine.

## 2. Find Common Characters
- **Technique:** Multiple Frequency Dictionaries + Minimum Frequency
- **Approach:** Build the frequency dictionary of the first word. For every remaining word, build another dictionary and update each common character's count to the minimum frequency.
- **Time Complexity:** O(n × m)
- **Auxiliary Space:** O(k), excluding output.
- **Edge Case:** A character appears in one word but is missing from another.

## 3. Jewels and Stones
- **Technique:** Character Frequency Counting
- **Approach:** Build a dictionary of jewel characters and another dictionary containing stone frequencies. Add the frequencies of all jewel characters to calculate the answer.
- **Time Complexity:** O(j + s)
- **Auxiliary Space:** O(k)
- **Edge Case:** No stones match any jewel characters.

## Learning Outcomes
- Practiced building and comparing two frequency dictionaries.
- Learned to check character availability.
- Understood minimum frequency across multiple strings.
- Practiced counting matching characters.
- Improved dictionary-based string problem-solving.

## Restrictions Followed
- No collections.Counter used.
- No Counter arithmetic used.
- Two dictionaries built manually.
- No unnecessary library imports.
- No built-in sorting used.
- Only primitive data structures used.
