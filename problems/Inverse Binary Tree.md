---
tags:
  - trees
  - dfs
  - easy
rating: 1000
pattern: Use recursion, flip the left and right, recursively call on left and right, return root
last_attempt: 2025-05-22
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- I need to make the changes in-place.
- I need to use DFS to traverse the tree.

#### Code
---

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Recursive call after reversal

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
- You can do in-place changes without temps with `x,y = w,v`