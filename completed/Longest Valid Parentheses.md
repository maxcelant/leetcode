---
tags:
  - hard
  - two-pointers
  - meta
link: https://leetcode.com/problems/longest-valid-parentheses/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★★★
---
#### Variants
- [[Valid Parenthesis]]

#### Problem
Given a string containing just the characters `'('` and `')'`, return _the length of the longest valid (well-formed) parentheses_ _substring_.

**Example 1:**

**Input:** s = "(()"
**Output:** 2
**Explanation:** The longest valid parentheses substring is "()".

**Example 2:**

**Input:** s = ")()())"
**Output:** 4
**Explanation:** The longest valid parentheses substring is "()()".

**Example 3:**

**Input:** s = ""
**Output:** 0

#### Notes
This is called a "two pass approach".

The idea is simple, we pass over the string from left to right and we try to find the largest valid parentheses from the left. When we reach a point where the **right** parens count is **greater** than the **left**, then we need to reset. There's no chance for you to make a larger valid set from then on.

Coming from the reverse, going right to left. We know the parens are valid as long as the left and right count match. As soon as we reach a point where the left count is greater than the right, we reset the counters.

#### Code
**Time Complexity**: O(2N)
**Space Complexity**: O(1)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Counts to keep track of total left and right parens
        l, r, res = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, r * 2)
            # If there are more right than left
            # Then we reset since there's nothing we can do
            # to create a larger valid paren
            elif r > l:
                l = r = 0
        
        # Do the same thing, but from the other side
        l, r = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, r * 2)
            # Going in the reverse direction, if there are more left than right
            # than we reset
            if l > r:
                l = r = 0 
        return res
```
