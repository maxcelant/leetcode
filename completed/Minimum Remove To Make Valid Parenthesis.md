---
tags:
  - medium
  - stack
  - meta
link: https://neetcode.io/problems/minimum-remove-to-make-valid-parentheses?list=neetcode250
rating: 4
last_attempt: 2025-10-02
---
#### Problem
You are given a string `s` consisting of lowercase English characters, as well as opening and closing parentheses, `(` and `)`.

Your task is to remove the minimum number of parentheses so that the resulting string is valid.

Return the resulting string after removing the invalid parentheses.

A parentheses string is valid if all of the following conditions are met:

1. It is the empty string, contains only lowercase characters, or
2. It can be written as AB (A concatenated with B), where A and B are valid strings, or
3. It can be written as (A), where A is a valid string.

**Example 1:**

```java
Input: s = "nee(t(c)o)de)"

Output: "nee(t(c)ode)"
```

> Explanation: "nee(t(co)de)" , "nee(t(c)o)de" would also be accepted.

**Example 2:**

```java
Input: s = "x(y)z("

Output: "x(y)z"
```

#### Notes
---
Every opening parenthesis needs a matching closing. We use a `stack` to keep track of the opening parenthesis and a `removals` set to include all the indices we want to eventually eliminate.

There are two main reasons to add to removals:
1. If the stack is empty and it's a closing parenthesis then we want to add that to `removals`.
2. After we finish iterating the string, any remaining values in the stack should be added to the `removals` because this meant they didn't have a closing parenthesis.

#### Code
---

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removals = set()
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            if c == ")":
                if not stack:
                    removals.add(i)
                else:
                    stack.pop()
        for i in stack:
            removals.add(i)
        res = []
        for i, c in enumerate(s):
            if i not in removals:
                res.append(c)
        return "".join(res)
```
