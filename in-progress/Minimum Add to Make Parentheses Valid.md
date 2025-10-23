---
tags:
  - medium
  - meta
  - stack
link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★★★★
---
#### Variants
- [[Minimum Remove To Make Valid Parenthesis]]

#### Problem
A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

- For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(**(**)))"` or a closing parenthesis to be `"())**)**)"`.

Return _the minimum number of moves required to make_ `s` _valid_.

**Example 1:**

**Input:** s = "())"
**Output:** 1

**Example 2:**

**Input:** s = "((("
**Output:** 3

#### Notes
Very easy question.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "": return 0
        open_parens = 0
        res = 0
        for c in s:
            if c == "(":
                open_parens += 1
            if c == ")":
                if open_parens == 0:
                    res += 1
                else:
                    open_parens -= 1
        return res + open_parens
```


#### Follow Up: *""*

```python

```