---
tags:
  - backtracking
pattern: Check each subset to see if it reaches the target, prune if you go over the sum
link: https://neetcode.io/problems/partition-equal-subset-sum
rating: 2
last_attempt: 2025-05-13
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        def dfs(i, subset):
            if sum(subset) == target:
                return True
            
            if sum(subset) > target or i >= N:
                return False
            
            for j in range(i, N):
                subset.append(nums[j])
                if dfs(j + 1, subset):
                    return True
                subset.pop()
            
            return False
        
        return dfs(0, [])
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**