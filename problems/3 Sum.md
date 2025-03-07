---
tags:
  - two-pointers
---

#### Intuition
---
- We need to sort it to make it possible to use two pointers algorithm.
- Use a set instead of a list because we don't want to store duplicates.
- We loop through each value, and try to sum to 0.
- Perform two pointers on values after `i`.
- At the end, we turn the set of tuples into a set of lists. 

#### Code
---

```python
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = set()
    for i in range(len(nums)):
      l, r = i + 1, len(nums) - 1
      while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total == 0:
          res.add((nums[i], nums[l], nums[r]))
          l += 1
          r -= 1
        elif total < 0:
          l += 1
        else:
          r -= 1
    return [[i, l, r] for (i, l, r) in res ]
```

#### Insight
---


#### Takeaways
---
- 