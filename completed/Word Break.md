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
- Whether a string can be segmented into substrings hangs on the notion that any substring that fits in will be recorded, so that we don't need to redo the work.
- This is a perfect scenario for dynamic programming.

#### Code
---
Iterative Approach
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

Recursive Approach

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = {}

        def dfs(i):
            if i == 0:
                return True
            if i in dp:
                return dp[i]

            for word in wordDict:
                M = len(word)
                if i - M >= 0 and s[i-M:i] == word:
                    if dfs(i - M):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return False

        return dfs(N)
```
#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**