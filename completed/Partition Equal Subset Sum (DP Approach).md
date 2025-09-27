---
tags:
  - 1d-dynamic-programming
pattern:
link: https://neetcode.io/problems/partition-equal-subset-sum
rating: 1
last_attempt: 2025-05-13
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- It's asking us to find a solution and the values are not contiguous, which means we need to use dp

#### Code
---

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: 
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
		dp[0] = True
        for n in nums:
	        # Go from target to num
            for i in range(target, n - 1, -1):
	            # see if target value without including the current number is possible
                dp[i] = dp[i] or dp[i - n]
        
        return dp[target]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We are trying to find the sum to _half of the total_ because if we can sum to half, then we can prove that we can make two equal halves.
- The DP table consists of `total // 2 + 1` spaces
- The first space is always `True`, because a total of 0 is always going to be possible.
- Each space in the dp table indicates whether a subset sum of that amount is possible.

Let's say sum total is:

`nums = [1,2,3,4]`, hence subset sum will be 5, we need to make sure we can create 5

`dp = [T, F, F, F, F, F]`

At each iteration we are asking, is the subproblem (`i - current number`) also possible?
If we reach the final position `dp[-1]` and it's true then that means that the target can be reached using the values.


#### Takeaways
---
**Lessons Learned?**