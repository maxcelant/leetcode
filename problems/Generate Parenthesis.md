---
tags:
  - backtracking
  - medium
rating: 1000
last_attempt: 2025-05-14
pattern: Use dfs/backtracking approach, add a parenthesis and recursively call, add a closing only if closing num is less than open, append to result when both equal N
---

#### Intuition
---
- Use a DFS type approach, when we need more open parenthesis, we add them, when we need more closed, we add them.
- We do this by calling the function recursively.
#### Code
---

```python

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        
        def dfs(o, c):
            if o == c == n:
                print(cur)
                res.append("".join(cur))
                return
            
            if o < n:
                cur.append("(")
                dfs(o + 1, c)
                cur.pop()
            
            if c < n and c < o:
                cur.append(")")
                dfs(o, c + 1)
                cur.pop()
        
        dfs(0, 0)
        return res
```

#### Insight
---

#### Takeaways
---
- When you are dealing with different permutations of a thing, it's most likely recursion
- You don't actually need to use a stack here. You can just add to the string and that would work.