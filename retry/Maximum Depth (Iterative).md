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
- We should use a stack and add the children to it.
- Use a tuple to keep track of the `depth` as we go along—incrementing it on each layer.

#### Code
---

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to keep track of the `max_depth` as we go along.
#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**