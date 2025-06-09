---
tags:
  - trees
  - top-down
  - dfs
rating: 4
pattern: DFS and keep track of max node seen thus far, top down approach. Use global var for tracking
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that we need to keep track of a count, so using a global is a good idea.
- We need to see the parent before the child—so top-down approach makes sense.
- Since we need to see the parent of the current node down a chain, DFS makes sense.

#### Code
---

```python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, curmax):
            nonlocal res
            if not root:
                return
            
            if curmax <= root.val:
                res += 1
            
            dfs(root.left, max(curmax, root.val))
            dfs(root.right, max(curmax, root.val))
                

        dfs(root, float('-inf'))
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We have a global `count` value.
- If we find a "bad" node, we don't want to use that value for it's children—since it's invalid, we should continue to use the last valid node in the tree!
	- Ex:  `3 -> 1 -> 3`, if we used `1` for `last_valid`, that would break this. 

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
