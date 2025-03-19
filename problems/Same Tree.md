---
tags:
  - trees
  - dfs
  - bottom-up
  - easy
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to compare nodes from the bottom-up, and propagate that `bool` value all the way up.

#### Code
---

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q: 
                return True
            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False
        return dfs(p,q)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We return `False` as a base-case, and only recursively call IF the two nodes match, otherwise it's pointless.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**