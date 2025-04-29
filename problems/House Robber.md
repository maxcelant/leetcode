---
tags:
  - 1d-dynamic-programming
  - medium
pattern: Use a dp array (or pointers), cur in dp will become max of (cur num + n - 2, n - 1), return last value in dp
link: https://neetcode.io/problems/house-robber
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- The problem says we cannot rob two adjacent houses, which means the max will be the either the previous house OR the house before that + the current.

#### Code
---
Using a preallocated list `O(N)` space complexity
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return max(dp[-1], dp[-2])
```

Using shifting variables `O(1)` space complexity

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevprev, prev = 0, 0
        for n in nums:
            # Max be the maximum of the current pos + the position 2 behind
            # OR the previous position by itself (not including current) 
            temp = max(n + prevprev, prev)
            prevprev = prev
            prev = temp
        return prev
```
#### Insight  
---
_"What are the important aspects of the solution?"_
- We are using the `dp` array to aggregate the result, by the end `max(dp[-1], dp[-2])`, one of these two will be the max result.

####  Takeaways
---
**Lessons Learned?**