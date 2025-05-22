---
tags:
  - trees
  - easy
  - dfs
  - top-down
rating: 5
pattern: Use two helpers, one to traverse the main tree and the other two compare the two trees. Return true if the trees match exactly, continue to search each subtree.
last_attempt: 2025-05-22
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that a top down approach is necessary.
	- At each step, we  need to compare the root and the subroot, starting from the top node.
- We need some sort of comparison function.
- DFS is a good approach for this.

#### Code
---

```python
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], subroot: Optional[TreeNode]):
            if not root: return False
            if self.compare_trees(root, subroot):
                return True
            return (dfs(root.left, subroot) or dfs(root.right, subroot))
        
        return dfs(root, subRoot)

    def compare_trees(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return self.compare_trees(root.left, subroot.left) and self.compare_trees(root.right, subroot.right)
        return False
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- On each step, we can call the comparison func, and let it determine whether it's found a full subtree in it.
- In the `dfs` func, we are returning `True` if either the left or right subtree return `True`.
	- This is important because we only need to find it once, so using `or` is a great way to do this.

#### Takeaways
---
**Where did I go wrong?**
- I tried to use a global variable for `found`, but that ended up being way too messy.
**Lessons Learned?**