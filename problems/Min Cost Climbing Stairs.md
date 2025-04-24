---
tags:
  - 1d-dynamic-programming
  - easy
pattern: Use dp array, the current value is the min of the previous 2 + the current cost, return the min of the last two values
link: https://neetcode.io/problems/min-cost-climbing-stairs
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

Solution using `O(N)` space complexity
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
```

Solution using `O(1)` space complexity
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = cost[0]
        p2 = cost[1]
        for i in range(2, len(cost)):
            temp = cost[i] + min(p2, p1)
            p1 = p2
            p2 = temp
        return min(p1, p2)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**