---
tags:
  - dfs
  - trees
  - bottom-up
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- A BST by nature is going to be the smallest from left to right.
- We start from the bottom and go up because the most left node will be the SMALLEST node in the tree, so we should start the count from there and decrement `k` as we propagate up.

#### Code
---

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        def dfs(root):
            nonlocal k, res
            if not root:
                return 
            
            dfs(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            dfs(root.right)

        dfs(root)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We should go from left -> right on the tree using DFS.
- Decrement the count `k` as we go along.

![[Pasted image 20250319114853.png|BST Smallest to Largest Pattern]]

#### Takeaways
---
**Where did I go wrong?**
**Lessons Learned?**
- I should have realized that the nature of a BST is "sorted" technically.