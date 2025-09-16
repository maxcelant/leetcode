---
tags:
  - arrays
  - medium
rating: 4
pattern: Use a set, and traverse the set. Only start if n - 1 is not in the set
---

#### Intuition
---
- Turn this list into a set, and starting from the bottom
- Increment the value by 1 and see if it's still in the set
- Keep track of the highest consecutive sequence.

#### Code
---

```python
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    nums = set(nums) # Remove duplicates, they dont serve a purpose here
    res = 0
    for n in nums:
        cur = n
        acc = 0
        while cur + acc in nums:
            acc += 1
        res = max(res, acc)
    return res

```

#### Insight
---


#### Takeaways
---
- 