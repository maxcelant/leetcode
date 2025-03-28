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
        def backtrack(start, set):
            res.append(set[:])
            for i in range(start, len(nums)):
                set.append(nums[i])
                backtrack(start + 1, set)
                set.pop()
        backtrack(0, [])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- This sort of follows the boilerplate for backtracking that you can find [[Backtracking|here]].
- Except because we want **all** values, we are just going to `append` no matter what.
- The key is that the `for` loop range decreases as we go on.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**