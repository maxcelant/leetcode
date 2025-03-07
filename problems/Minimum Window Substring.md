---
tags:
  - sliding-window
  - hashing
---

#### Intuition
---
- I need to think about the condition in which I shrink the window.
- When the current element in the counter is greater than that of `t`, then we need to shrink the window and remove it from the counter.
- How do we make sure all the correct letters (and frequencies) are in the substring? 
- I dont really care about additional letters, as long as the important ones are in there.

#### Code
---

```python

class Solution:
	def minWindow(self, s: str, t: str) -> str:
		res = ""
		resLen = float('inf')
		counter_t = Counter(t)
		counter_s = Counter()
		have, need = 0, len(counter_t)
		l = 0
		for r in range(len(s)):
			c = s[r]
			counter_s[c] += 1
			if c in counter_t and counter_t[c] == counter_s[c]:
				have += 1
			while have == need:
				# calculate new result
				if (r - l + 1) < resLen:
					resLen = (r - l + 1)
					res = "".join(s[l:r+1])
				counter_s[s[l]] -= 1
				# shrink window
				if s[l] in counter_t and counter_s[s[l]] < counter_t[s[l]]:
					have -= 1 
				l += 1
		return res		
			
```

#### Insight
---


#### Takeaways
---
- I shrink the window when I have met the minimum requirement of having all the elements of my substring! 