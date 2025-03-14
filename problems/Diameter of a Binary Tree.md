---
tags:
  - trees
  - recursion
  - dfs
  - bottom-up
---
 #### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- In order to find the max diameter, we will need the height of all the subtrees, so we need to take a bottom-up approach.

#### Code
---

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root: 
	            return 0
	        
            left = dfs(root.left)
            right = dfs(root.right)
            # Calculate the root
            res = max(res, left+right)

			# We only care about the max of the two subtrees
            return 1 + max(left, right)

        dfs(root)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We calculate `res` separately because **the longest diameter path may not pass through the root**.
- Calculate the left and right subtrees, calculate the result, and pass up the bigger of the two sides.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**