---
tags:
  - arrays
  - medium
---

#### Intuition
---
- 

#### Code
---

```python
class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    last = m + n - 1
    a, b = m - 1, n - 1
    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[last] = nums1[a]
            a -= 1
        else:
            nums1[last] = nums2[b]
            b -= 1
        last -= 1
```

#### Analysis
---


#### Takeaways
---
Didn't realize that I needed to start from the end of the list and use pointers to traverse each list separately.