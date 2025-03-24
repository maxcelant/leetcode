---
tags:
  - trees
  - hard
  - recursion
  - dfs
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- DFS makes sense here so that we can remove repetitive work done.
- A "path" can only include one node that has both it's children in it. 
	- What I mean by this is that only one node in the path can split to both right and left and include both values.

#### Code
---

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            # Find the max of the left and right subtrees
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            # Assuming this root is where the fork happens
            res = max(res, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- For every node in the tree, we need to find max sum of the left and right children.
- Since this sum can be negative, we always want to take the max between the sum and 0.
- The result CAN include both the left and the right  values + the current root. The idea is that we are splitting on the current node. (example below)
	- Since `12` is our `root`, we can take both the `left` and `right` values.

![[Pasted image 20250323122501.png|Example of subproblem]]


- The recursive value we return should be the current root value + the max of the left and right subtrees. 
- Because in this case, the subproblem is not going to split—we just want either left or right.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**