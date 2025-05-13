---
tags:
  - 1d-dynamic-programming
pattern: Use bottom up approach, checking if superseding numbers are larger than current and keep track of LIS from each position using DP table.
link: https://neetcode.io/problems/longest-increasing-subsequence
rating: 2
last_attempt: 2025-05-12
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We cannot use sliding window or [[Kadane's Algorithm]] here because the values are not contiguous.
- We must use dynamic programming here.
- The LIS needs to check all superseding numbers.

#### Code
---

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = {}
        
        def dfs(i):
            if i == N:
                return 0
            
            if i in dp:
                return dp[i]

            dp[i] = 1
            # Loop through all of the superseding numbers
            for j in range(i + 1, N):
                # Only compute if it's less than next number
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dfs(j))

            return dp[i]
        
        # Try to find longest sequence from all positions in the list
        return max(dfs(i) for i in range(N)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to check starting from all the positions because any of them could be the start of the LIS.
- We iterate through all superseding numbers from that starting position, using cache if you can.
- Only if `i` is less than `j` otherwise we ignore.

#### Takeaways
---
**Lessons Learned?**
It's okay to have O(N) time complexity with DP problems.