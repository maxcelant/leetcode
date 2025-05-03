---
tags:
  - 1d-dynamic-programming
  - medium
pattern: Use reverse dynamic programming where each position represents the number of ways to decode the remaining string, combining single- and valid double-digit steps.
link: https://leetcode.com/problems/decode-ways/description/
rating: 2
last_attempt: 2025-05-03
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Identify the subproblem
- "How many different ways can we decode the string **without the current character?**"

#### Code
---

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Add 1 more position to allow us to do reverse look ups easier
        dp = [0] * (n + 1) 
        # Initialize Nth position with 1 which means there is 1 way 
        # to decode an empty string
        dp[n] = 1 

        # Start from the end and fill in dp table as we go
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # Single digits, there is AT LEAST dp[i + 1] ways to decode the string
                dp[i] = dp[i + 1]

                # OPTIONALLY there may be more ways to decode if we look at the two
                # digits together
                if (i + 1 < n) and (10 <= int(s[i:i+2]) <= 26):
                    dp[i] += dp[i + 2]
        return dp[0]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Each step in the dp table is the number of ways to decode **starting at that step**.
- Every value in the array starts with getting the number of subproblems that came before, which makes sense because we are asking "How many ways are there to decode this string?"—If the previous substring says `2`, then adding one more value to it will still gives us 2 ways of decoding. Things get interesting when we look the the optional portion.
- Optionally, we can have another way to decode IF the neighboring digits `s[i] and s[i+1]` are from 10 to 26 (inclusive), that means we've found a new way to decode! So we should ADD the total ways to decode from the value BEFORE the `s[i] and s[i+1]`.

#### Takeaways
---
**Lessons Learned?**
We are using a dp table of size `N + 1` because our base case is an empty string which will always have 1 way to decode.