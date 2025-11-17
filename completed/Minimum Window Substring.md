---
tags:
  - sliding-window
  - hashing
  - hard
  - meta
rate:
  - ★★★★
last_attempt: 2025-11-16
link: https://leetcode.com/problems/minimum-window-substring/
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
        tCount = Counter(t)
        sCount = defaultdict(int)
        res = (-1, -1) # return slice l:r+1 for the min substring
        minCount = float('inf')
        l = 0
        have = 0
        need = len(tCount)
        for r in range(len(s)):
            sCount[s[r]] += 1
            if s[r] in tCount and tCount[s[r]] == sCount[s[r]]:
                have += 1
            while have == need:
                if (r - l) + 1 < minCount:
                    minCount = (r - l) + 1
                    res = (l, r)
                sCount[s[l]] -= 1
                if sCount[s[l]] == 0:
                    del sCount[s[l]]
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]		
```

#### Insight
---


#### Takeaways
---
- I shrink the window when I have met the minimum requirement of having all the elements of my substring! 