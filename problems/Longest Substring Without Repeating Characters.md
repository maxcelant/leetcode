---
tags:
  - sliding-window
---

#### Intuition
---
- 

#### Code
---

```python
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    window = set()
    l = 0
    res = 0
    for r in range(len(s)):
      while s[r] in window:
        window.remove(s[l])
        l += 1
      window.add(s[r])
      res = max(res, len(window))
    return res
```

#### Analysis
---


#### Takeaways
---
- Using an external data structure like a set here is helpful because we need to keep track of the chars in the window.