---
tags:
  - backtracking
  - retry
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- I need to ALL solutions, including the intermediate steps, so backtracking is the key.

#### Code
---

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def findAllSubsets(start: int, subset: List[int]):
            res.append(subset.copy())
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                findAllSubsets(i + 1, subset)
                subset.pop()
        findAllSubsets(0, [])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- This problem boils down to understanding [[Backtracking#Understanding the For Loop Approach|For Loop Backtracking DFS]] very well.
- Except because we want **all** values, we are just going to `append` no matter what.
- The key is that the `for` loop range decreases as we go on.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**