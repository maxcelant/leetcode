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
	1. Include this number, increment total, and go to next number in sequence.
	2. Don't include this number (loop to see if there are duplicates)

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
- Since we only include the same number once, we need to increment the `start` value on every recursive call, unlike [[Combination Sum (Without For Loop)]] which allowed the same value more than once.
- The `if` condition allows us to skip the same value if it shows up multiple times.
- 

#### Takeaways
---
**Where did I go wrong?**
- I should have my `if` conditions flipped since python short-circuits its if statements.

**Lessons Learned?**
- ALWAYS put your out of bounds check BEFORE checking an index in a `if` statement.
- **Example:**
	```python
	while start + 1 < len(candidates) and candidates[start] == candidates[start + 1]:
		...
	```
- This will fail if you flip them because you are trying to get `candidates[start]`, but that may be out of bounds.