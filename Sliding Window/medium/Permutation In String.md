#### Approach
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

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()
        l = 0

        for r in range(len(s2)):
            window_count[s2[r]] += 1
            
            # Maintain the window size equal to s1's length
            if (r - l + 1) > len(s1):
                if window_count[s2[l]] == 1:
                    del window_count[s2[l]]
                else:
                    window_count[s2[l]] -= 1
                l += 1

            # Compare window count with s1_count
            if window_count == s1_count:
                return True
        
        return False
```


#### Where did I go wrong?
---
- I can compare counters, duh. 
- I just need to make sure to stay within the window size of `s1`.
	- If i go outside of that size, then i shrink it from the left by deleting from the counter.