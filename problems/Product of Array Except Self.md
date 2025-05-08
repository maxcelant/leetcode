---
tags:
  - arrays
  - medium
rating: 4
last_attempt: 2025-05-07
---

#### Intuition
---
- Initialize result array to all 1's. `[1,1,1,1]`
- Prefix (left to right), not including self. `[1,1,2,8]`
- Postfix (right to left), not including self. `[48, 24, 6, 1]`
- Multiply them together! `[(1x48), (1x24), (2x6), (1x8)]`
- You can optimize this to `O(1)` space complexity by using a prefix/postfix value instead of array.

#### Code
---

```python
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]
    
    return res
```

#### Insight
---


#### Takeaways
---
- 