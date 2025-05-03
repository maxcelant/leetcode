---
tags:
  - sliding-window
  - hashing
rating: 2
pattern: Use a table to keep track of frequency, on each iteration, check if current char is the most frequent. Shrink the window if the length - most frequent is greater than K
last_attempt: 2025-05-02
---

#### Intuition
---
- 

#### Code
---

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        res = 0
        most_freq = float('-inf')
        for r in range(len(s)):
            freq[s[r]] += 1
            most_freq = max(most_freq, freq[s[r]])
            # There are too many letters in the window
            # that ARENT the most frequent, we need to shrink window
            while (r - l + 1) - most_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
```

#### Insight
---


#### Takeaways
---
- I can only have K changes, which means we only count changes that aren't the most frequent element. Hence why window length - most frequent is used.