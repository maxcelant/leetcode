---
tags:
  - 1d-dynamic-programming
pattern: 
link: https://neetcode.io/problems/maximum-product-subarray
rating: 
last_attempt: 2025-05-08
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
    def maxProduct(self, nums: List[int]) -> int:
		# Initialize res to the first value
        res = nums[0]
        curmin, curmax = 1, 1
	
        for n in nums:
			# Store the old max calculated to use for current min
            oldmax = curmax
            curmax = max(n * oldmax, n * curmin, n)
            curmin = min(n * oldmax, n * curmin, n)
            res = max(res, curmax)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- As we go through each value in the list, we keep track of the min and max product. The reason is that the max/min max can change depending on if the next element is negative or not.
- We multiply our current element by min/max, but we also check to see if the element itself is the max.
	- Ex: `[-1, 8]` In this case, the min/max is both `-1`, and `num = 8`, so we would get the new max to be `8`.
- We store the old max in a temporary variable before calculating the new current min because we want to use the _previous max calculated_ for the new min.
- 

#### Takeaways
---
**Lessons Learned?**