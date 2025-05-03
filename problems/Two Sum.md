---
tags:
  - arrays
  - easy
rating: 5
last_attempt: 2025-04-30
---

#### Intuition
---
- 

#### Code
---
```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      t = {}
      for i, n in enumerate(nums):
        diff = target - n
        if diff in t:
            return [t[diff], i]
        else:
            t[n] = i
      return [-1,-1]
```

#### Insight
---
- 

#### Takeaways
---
- **Where did I go wrong?**
- **Lessons Learned?**
- **Aha Moments?**
