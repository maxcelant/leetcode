---
tags:
  - backtracking
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- To generate permutations, build them step by step by choosing elements that haven’t been used yet.

#### Code
---

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset: List[int]):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for n in nums:
                if n not in subset:
                    subset.append(n)
                    backtrack(subset)
                    subset.pop()
        backtrack([])
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- At each step, I add a number to the `subset` and then recursively call.
- I keep doing this and specifically ignore the same number by using the `if` condition.
- The **base case** is that the `subset` is equal to the length of`nums`. 

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**