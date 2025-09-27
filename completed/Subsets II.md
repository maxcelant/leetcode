---
tags:
  - backtracking
  - dfs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- **Base case:** When our start reaches the same length as `nums`.
- **Branching Paths**
	1. We add the number to the subset.
	2. We don't add the number to the subset.

#### Code
---

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, subset):
            if start == len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[start])
            backtrack(start + 1, subset)
            while start + 1 < len(nums) and nums[start + 1] == nums[start]:
                start += 1
            subset.pop()
            backtrack(start + 1, subset)
        backtrack(0, [])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- we go deep first, adding all the values to the subset and then we will remove one at time by backtracking.
- The key is that we keep start the same while popping from subset
- We need to sort the list first to make sure we skip duplicates correctly.

#### Takeaways
---
**Where did I go wrong?**
- Didn't sort at the beginning.
**Lessons Learned?**
- This is similar to the [[Subsets]] problem + the added condition + sorted list.