---
tags:
  - two-pointers
pattern: Use two pointers, if above target decrement right pointer...
link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
rating: 5
last_attempt: 2025-05-02
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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot < target:
                l += 1
            elif tot > target:
                r -= 1
            else:
                return [l+1,r+1]
        return [-1,-1]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**