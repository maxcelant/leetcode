---
tags:
  - two-pointers
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
    max_area = 0
    l, r = 0, len(height) - 1
    while l < r:
      min_height = min(height[l], height[r])
      area = min_height * (r - l)
      max_area = max(area, max_area)
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
    return max_area

```

#### Insight
---


#### Takeaways
---
- 