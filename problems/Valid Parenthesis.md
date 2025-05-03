---
tags:
  - stack
  - easy
pattern: Use a lookup table for bracket types, see if top of stack matches the current iter val. return true if stack is empty
link: https://leetcode.com/problems/valid-parentheses/description/
rating: 5
last_attempt: 2025-05-02
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        t = {')': '(', '}':'{', ']':'['}

        for c in s:
            if c in t:
                if stk and stk[-1] == t[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return len(stk) == 0

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**