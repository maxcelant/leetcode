---
tags:
  - 1d-dynamic-programming
  - sliding-window
  - kadanes-algorithm
pattern: Use kedanes algorithm
link: https://neetcode.io/problems/maximum-subarray
rating: 4
last_attempt: 2025-05-08
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that you are asked to find the sum of a contiguous subarray and know that [[Kadane's Algorithm]] solves exactly this.

#### Code
---

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0
        for n in nums:
            cursum = max(cursum + n, n)
            maxsum = max(cursum, maxsum)
        return maxsum
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**