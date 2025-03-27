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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start: int, total: int, subset: List[int]):
            if total == target:
                res.append(subset[:])
                return
            if total > target or start == len(candidates):
                return
            
            subset.append(candidates[start])
            dfs(start + 1, total + candidates[start], subset)
            subset.pop()

            while start + 1 < len(candidates) and candidates[start] == candidates[start + 1]:
                start += 1

            dfs(start + 1, total, subset)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
- ALWAYS put your out of bounds check BEFORE checking an index in a `if` statement.
- **Example:**
	```python
	while start + 1 < len(candidates) and candidates[start] == candidates[start + 1]:
		...
	```
- This will fail if you flip them because you are trying to get `candidates[start]`, but that may be out of bounds.