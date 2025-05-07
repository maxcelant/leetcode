---
tags:
  - 1d-dynamic-programming
  - medium
pattern: the subproblem is the amount going from 0-N, use that to build up to N using a bottom up dfs approach.
link: https://neetcode.io/problems/coin-change
rating: 2
last_attempt: 2025-05-05
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We can use our [[Dynamic Programming|boilerplate]] DP template here.

#### Code
---

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if i in dp:
                return dp[i]
            
            res = float('inf')
            for c in coins:
                res = min(res, 1 + dfs(i - c))
            dp[i] = res
            return res 
        
        out = dfs(amount) 
        return out if out != float('inf') else -1
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We loop through all of the coins for every subproblem.
- If we go below `0`, we return infinity, since it isn't possible with that coin
	- Aside: this is nicer than doing bounds checks imo.
- We return the min of the past result and subproblem including the coin. 

#### Takeaways
---
**Lessons Learned?**