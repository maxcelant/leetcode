---
tags:
  - backtracking
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- **Base Case:** Our `start` value is the same length as `s`.
- **Branching Paths:** We have successfully created a palindrome from `start` to `i`!
- **Pruning:** We were unable to make a successful palindrome.

#### Code
---

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(start: int, parts: List[int]):
            if start == len(s):
                res.append(parts.copy())
                return

            for i in range(start, len(s)):
				# Only continue down the subtree if we
				# find a valid palindrome
                if self.is_palindrome(start, i, s):
                    parts.append(s[start:i+1])
                    dfs(i + 1, parts)
                    parts.pop()
        dfs(0, [])
        return res

    def is_palindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need the entire string to create valid palindromes (in segments), so if any of them fail to do so, we "backtrack", by just pruning that subtree.

![[Pasted image 20250402134949.png|DFS Tree]]

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**