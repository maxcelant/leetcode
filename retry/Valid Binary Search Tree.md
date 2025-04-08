---
tags:
  - trees
  - dfs
  - top-down
  - retry
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to know the parent node before the child, so DFS with top-down makes sense here.

#### Code
---

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            if not root: return True
            if not (left < root.val < right):
                return False
            
            # If we are going left, update the upper bound to be the parent
            # If we are going right, update the lower bound to be the parent
            return dfs(root.left, left, root.val) and \
                    dfs(root.right, root.val, right)

        return dfs(root, float('-inf'), float('inf'))
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- At each step of the tree, we need to ensure that the current node is `l < cur < r`.
- as we drill down—update the bounds.
- If we are going left, then we should make the nodes parent it's upper bound.
- If we are going right, then we should make the nodes parent it's lower bound.

![[Pasted image 20250319110919.png|Upper and Lower Bounds Example]]

#### Takeaways
---
**Where did I go wrong?**
- I was only checking the current subtree and was _ignoring_ the larger tree, this is a problem because there could be nodes that are valid in the current subtree, but may be invalid to the larger tree.
**Lessons Learned?**