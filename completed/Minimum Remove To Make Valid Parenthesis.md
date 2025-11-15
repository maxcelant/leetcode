---
tags:
  - medium
  - stack
  - meta
link: https://neetcode.io/problems/minimum-remove-to-make-valid-parentheses?list=neetcode250
last_attempt: 2025-11-13
rate:
  - ★★★★★
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
            elif c == ")" and not stack:
                removals.add(i)
            elif c == ")" and stack:
                stack.pop()
            
        while stack:
            removals.add(stack.pop())
        
        return "".join([c for i, c in enumerate(s) if i not in removals])
```

#### Follow up: *"What if you can't use the stack"*

This can be solved by using 2 passes on the string. 
Use `count` to keep track of open parens seen.

On first pass:
1. If its an open parens then increment `count`
2. If its a closing parens AND `count` is not zero, then reduce `count` by 1 and add the char to the result string
3. If its a closing parens AND `count` IS zero, then don't add that value
4. In all other cases, add the character

On second pass:
1. We reverse the result because we want to take off all the dangling open parenthesis until `count` is zero.
2. The reason we take the open parenthesis from the end because it'll always end up being a valid string in that case—the same can not be said about taking from the beginning.

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_parens = 0
        res = []
        for c in s:
            if c == '(':
                open_parens += 1
                res.append(c)
            elif c == ')':
                if open_parens > 0:
                    res.append(c)
                    open_parens -= 1
            else:
                res.append(c)
        
        i = len(res) - 1
        while open_parens > 0:
            if res[i] == '(':
                res.pop(i)
                open_parens -= 1
            i -= 1

        return ''.join(res)
```