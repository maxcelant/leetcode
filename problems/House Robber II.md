---
tags:
  - 1d-dynamic-programming
  - medium
pattern: Use house robber 1 approach, but get max of not including first and not including last
link: https://neetcode.io/problems/house-robber-ii
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- This is a continuation of house robber 1, so we can follow the same dp approach.

#### Code
---

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        # You can either rob this house (n) and the n - 2 houses
        # Or you can rob the n - 1 house
        # Choose the higher one
        prev, prevprev = 0, 0
        for n in nums:
            temp = max(n + prevprev, prev)
            prevprev = prev
            prev = temp
        return prev
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- The idea is that we can ONLY include either the first or the last, not both (since we are saying the list cycles back around the end).
- So the easiest approach is to just avoid having them in the same list, run the dp problem twice: once not including the first and once not including the last.

#### Takeaways
---
**Lessons Learned?**