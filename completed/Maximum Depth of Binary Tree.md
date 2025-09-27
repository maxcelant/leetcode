---
tags:
  - trees
  - easy
pattern: Use recursion, return 1 + the max depth of the two leaf nodes
link: https://neetcode.io/problems/depth-of-binary-tree
rating: 1000
last_attempt: 2025-05-22
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---
Iterative Approach
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
        return max_dept
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**