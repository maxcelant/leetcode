---
tags:
  - backtracking
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Backtracking is a good choice here because we need to discover all solutions.

#### Code
---

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def findTargets(start: int, total: int, subset: List[int]):
            if total == target:
                res.append(subset.copy())
                return 
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                subset.append(candidates[i])
                findTargets(i + 1, total + candidates[i], subset)
                subset.pop()

        findTargets(0, 0, [])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Here we skip duplicates in the for loop. Importantly, we make sure that `start` and `i` aren't the same when doing this.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**