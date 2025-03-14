---
tags:
  - trees
  - dfs
  - bottom-up
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- The response does not necessarily need to get "propagated up", so using a closure value creates a simpler approach.
- We need to look at the left and right subtrees before looking at the parent, so bottom-up approach.

#### Code
---

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            if not root: 
	            return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1: 
                balanced = False
            return 1 + max(left, right)
        dfs(root)
        return balanced
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We are keeping track of the `depth` as we go, and propagating it up.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**