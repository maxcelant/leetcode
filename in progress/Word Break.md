---
tags:
  - 1d-dynamic-programming
pattern: use a boolean dp table, keep track of which substrings create words, use table to see if remaining string also form a word
link: https://neetcode.io/problems/word-break
rating: 3
last_attempt: 2025-05-10
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(N+1):
            for word in wordDict:
                M = len(word)
                if (i - M) < 0:
                    continue
                if s[i-M:i] == word and dp[i - M]:
                    dp[i] = True
        return dp[-1]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**