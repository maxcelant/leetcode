---
tags:
  - trees
  - hard
  - recursion
  - bottom-up
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We don't necessarily need to use a global to solve this.
- For the current node, i need two things
	1. What is the max including both of my children?
	2. What is the max if i include only one of my children?
- We want to return the max found of the entire tree AND the current max of the subtree to the parent.

#### Code
---

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # We ONLY take one of the branching paths and return that max to the parent
        # We also see if the max of this node + both sides is larger than our current
        def dfs(root) -> Tuple[int, int]:
            if not root:
                # Max value, Sum at this path
                return 0, float('-inf')            
            
            l_max, l_pathsum = dfs(root.left)
            r_max, r_pathsum = dfs(root.right)

            # Max when forking at this node (check if this is better than our current best)
            cur_pathsum = root.val + max(l_max, 0) + max(r_max, 0)
            best_pathsum = max(r_pathsum, l_pathsum, cur_pathsum)

            cur_max = root.val + max(l_max, r_max, 0)

            return cur_max, best_pathsum

        _, res = dfs(root)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- At each step, we calculate the current max—which is the max path that we will return up to the parent in which we can only choose one side (left or right).
- We also calculate the max path if the current node was the one that forked—so we include both the left and right max's.
- Since this is a bottom-up approach, at each step we ask "Is this best found better than left or right total we have calculated?"
- If so, then take that one instead of the left and right and send it up!

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**