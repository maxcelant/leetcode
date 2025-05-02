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
    longest_seq = 0
    nums = set(nums)
    for n in nums:
      cur = n
      cur_seq = 0
      while cur in nums:
        cur += 1
        cur_seq += 1
      longest_seq = max(longest_seq, cur_seq)
    return longest_seq

```

#### Insight
---


#### Takeaways
---
- 