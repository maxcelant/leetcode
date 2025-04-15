---
tags:
  - backtracking
  - medium
insight: backtracking, base case is we reach target, prune if we go over target.
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Backtracking works best because we need to find ALL solutions with X condition.

#### Code
---

```python
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def findTargets(start: int, total: int, subset: List[int]):
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                # Doesn't cause infinite loop because 
                # we continuously add to the total
                findTargets(i, total + nums[i], subset)
                subset.pop()
        
        findTargets(0, 0, [])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We recursively call `findTargets` while not incrementing `i`, because we can use the same index again and again.
- This works because the total accumulation prevents stack overflows for occurring.
#### Takeaways
---
**Where did I go wrong?**
- I did `findTargets(i + 1, ...)` which is wrong because it immediately goes to the next value, instead of continuously adding the current one.
**Lessons Learned?**