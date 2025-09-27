---
tags:
  - stack
  - easy
link: https://leetcode.com/problems/valid-parentheses/description/
rating: 1000
last_attempt: 2025-05-02
---
#### Problem
You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise

#### Notes
---

#### Code
---

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matcher = {'}': '{', ']':'[', ')':'('}
        for ele in s:
            if ele in matcher:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if matcher[ele] != top:
                    return False
                stack.pop()
            else:
                stack.append(ele)
        return len(stack) == 0
```
