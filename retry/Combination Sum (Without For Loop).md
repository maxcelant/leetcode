---
tags:
  - backtracking
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use dfs with backtracking to construct all the solutions.
- **Base case:** We reach the target.
- **Prune case:** We go above target OR `i` is larger than `len(nums)`
- **Branching Paths:** 
	1. Continue to include this number until we reach base case
	2. Remove current number and move on to next number 

#### Code
---

```python
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i: int, total: int, subset: List[int]):
            # Base case
            if total == target:
                res.append(subset[:])
                return
            
            # Prune case
            if total > target or i >= len(nums):
                return

            # Try including the current num
            subset.append(nums[i])
            dfs(i, total + nums[i], subset)
            
            # Don't include current num and move on to next
            subset.pop()
            dfs(i + 1, total, subset)
        dfs(0, 0, [])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We should prune if we reach above the target
- When we decide to not include the current num, we shouldn't update the total AND remove the current num from the `subset`.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**