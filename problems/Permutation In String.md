---
tags:
  - sliding-window
rating: 3
pattern: Use a counter for s1, create a counter for window. If length of window is greater than s1, then shrink window.
---

#### Intuition
---
- We need to create a frequency counter for both `s1` and `s2`.
- Build the s1 counter.
- We need a counter for the number of "changes" needed to successfully determine that 1 word is inside the other.
- When frequency of a character match **exactly** then we can increment our changes counter by 1.
- If the frequency of a character stops matching, then we decrement our changes counter by 1.
- We check to make sure our changes counter matches the amount of letters in our original word.
- The reason we need to check for exact matches of characters is because we don't want to accidentally count a change for a character that already has the right amount of changes.

#### Code
---

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        # we need to check if the counter of s1 == window
        s1cnt = Counter(s1)
        window = Counter()
        l = 0
        for r in range(len(s2)):
            window[s2[r]] += 1
            if (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                l += 1
            if s1cnt == window:
                return True
        return False
```

#### Insight
---


#### Takeaways
---
- I can compare counters, duh. 
- I just need to make sure to stay within the window size of `s1`.
	- If i go outside of that size, then i shrink it from the left by deleting from the counter.