---
tags:
  - two-pointers
pattern: use two pointers, get min of two sides * the distance between l and r
rating: 5
last attempted: 2025-05-02
---

#### Intuition
---
- Use two pointers, decrement the smallest side.
- Calculate the area by doing the min of left and right.
- Multiplied by distance between left and right pointers.

#### Code
---

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(area, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
```

#### Insight
---


#### Takeaways
---
- 