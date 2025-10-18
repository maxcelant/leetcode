---
tags:
  - strings
  - meta
  - medium
link: https://leetcode.com/problems/string-to-integer-atoi/description/?envType=company&envId=facebook&favoriteSlug=facebook-three-months
last_attempt: 2025-10-18
rate:
  - ★★★★
---
#### Problem
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

1. **Whitespace**: Ignore any leading whitespace (`" "`).
2. **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
3. **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. **Rounding**: If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-231` should be rounded to `-231`, and integers greater than `231 - 1` should be rounded to `231 - 1`.

Return the integer as the final result.

**Example 1:**
```
**Input:** s = "42"

**Output:** 42

**Explanation:**

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
```

#### Notes
---
Easy but has lots of edge cases. We remove leading whitespace (not all whitespace). We figure out the sign if it has one. Then we figure out the final value. The last thing we do is sign and clamp it so its not out of range.

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = res = 0
        sign = 1

        # Remove leading whitespace
        while i < len(s) and s[i] == " ":
            i += 1

        # Sign it
        if i < len(s) and s[i] == "+":
            i += 1
        elif i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        # Loop until we reach a non-numeric char
        while i < len(s) and s[i].isnumeric():
            res = res * 10 + int(s[i])
            seen_nonzero = True
            i += 1
        
        # Attach sign
        res = res * sign
        # Clamp to range
        return min((2**31)-1, max(-2**31, res))
```


#### Follow Up: *""*

```python

```