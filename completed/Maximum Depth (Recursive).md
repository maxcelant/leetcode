---
tags:
  - recursion
  - trees
  - dfs
  - top-down
  - easy
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need a top-down approach here because the depth needs to start from the root node.

#### Code
---

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], depth: int):
            if not root: 
                return depth
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
        return dfs(root,0)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to use `max(..)` to get the biggest depth from the left and right side.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**