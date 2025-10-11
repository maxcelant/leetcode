---
tags:
  - trees
  - dfs
  - top-down
  - medium
rating: 4
pattern: Check whether the node is bigger than both p an q or smaller, move the node down the tree.
last_attempt: 2025-05-28
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that the lowest common ancestor means that it's greater than `p` and less than `q` (or vice versa).
- We need to traverse top-down using DFS until we find that common ancestor.

#### Code
---

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode'):
            if not root: 
                return None
            if root.val > p.val and root.val > q.val:
                return dfs(root.left)
            if root.val < p.val and root.val < q.val:
                return dfs(root.right)
            return root
            
        return dfs(root) 
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- On each recursive call, we should compare the current value with `p` and `q` to know whether we should go left or right.
- Going left means that the current node is too big—vice-versa for right.

#### Takeaways
---
**Where did I go wrong?**
- I incorrectly assumed that `p` would always be less than `q`, but that's not always the case.
Example:
```
    6
   / \
  2   8
     / \
    7   9

p = 8, q = 7
```
**Lessons Learned?**
- Pay careful attention to details / edge-cases with nodes.