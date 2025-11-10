---
tags:
  - strings
  - meta
  - medium
  - nvidia
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


#### Go Solution

The annoying bit in Go is doing the bounds check. Basically we are checking to see if adding the new digit will cause an overflow or not. We shift around the variables such that we can check if the `res` is greater.

```
MaxInt = 100
res = 10
digit = 5

10 > (100 - 5) / 10
10 > 9.5 which means doing '10 * 10 + 5 = 105' would cause an overflow
```

```python
func myAtoi(s string) int {
    i, sign, res := 0, 1, 0
    for i < len(s) && s[i] == ' ' {
        i++
    }
    if i < len(s) && s[i] == '-' {
        sign = -1
        i++
    } else if i < len(s) && s[i] == '+' {
        i++
    }
    for i < len(s) && s[i] == '0' {
        i++
    }
    for i < len(s) && unicode.IsDigit(rune(s[i])) {
        num := int(s[i] - '0')
        if res > (math.MaxInt32 - num) / 10 {
            if sign == 1 {
                return math.MaxInt32
            }
            return math.MinInt32
        }
        res = res * 10 + num
        i++
    }
    return res * sign
}
```