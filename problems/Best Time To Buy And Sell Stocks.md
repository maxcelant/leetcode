---
tags:
  - sliding-window
  - easy
pattern: if right pointer is smaller than left, move pointer forward, calc max of cur and max
rating: 5
last attempted: 2025-05-02
---

#### Intuition
---
- 

#### Code
---

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res
```

#### Insight
---


#### Takeaways
---
- 