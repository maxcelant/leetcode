---
tags:
  - sliding-window
  - hashing
---

#### Intuition
---
- Always keep track of the most frequent element in the window.
- You can expand the window as much as you want, as long as the element in the most frequent.
- However, if it isn't the most frequent element then we can continue to expand, but we need to decrease `k`.
- If we reach a point where `k = 0`, then we need to start decreasing the window from the left.
- All this time, still keeping track of the most frequent element.
- What is the best way to keep track of the most frequent element?
	- I could use a `Counter`, and do `.most_common(1)`.
- In need some condition for shrinking the window...
	- if total count > k (but excluding the most common element)
		- So this means we should only update total count if it _isnt_ the most common element.
- The total count is the sum of all values in the counter
- if the length of the window

#### Code
---

```python

from collections import Counter

class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		res = 0
		l = 0
		c = Counter()
		for r in range(len(s)):
			c[s[r]] += 1
			while (r - l + 1) - c.most_common(1)[0][1] > k:
				c[s[l]] -= 1
				l += 1
			res = max(res, (r - l + 1))
		return res
```

#### Analysis
---


#### Takeaways
---
- I can only have K changes, which means we only count changes that aren't the most frequent element. Hence why window length - most frequent is used.