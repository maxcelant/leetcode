#### Approach
---
- 

#### Code
---

```python
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    res = 0
    smallest = float('inf')
    for p in prices:
      smallest = min(smallest, p)
      res = max(res, p - smallest)
    return res
```


#### Where did I go wrong?
---
- 