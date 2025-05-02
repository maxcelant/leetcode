---
tags:
  - medium
  - 2d-dynamic-programming
pattern: Use 2D dp table, fill in default palindromes, traverse all substrings and look at bottom left value to see if that one is also a palindrome
link: https://neetcode.io/problems/longest-palindromic-substring
rating: 3
---
#### Video Breakdown
![[longest-pali-substring.mov]]

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- If `s[i] == s[j]` AND the substring `s[i+1:j-1]` is a palindrome, then `s[i:j]` is a palindrome as well.
- We know all substrings of length 1 are palindromes.
- We can use this to find substrings of length 3.
- Check every `i,j` pair where `j - i = 2`.
- We can then use that knowledge to find length 5, then 7, etc.

#### Code
---

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = [0, 0]

		# All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

		# All adjancent letters that are the same are palindromes
        for i in range(1, n):
            if s[i] == s[i-1]:
                dp[i-1][i] = True
                res = [i-1, i]

		# Go through each possible substring
		# Use dp table to see if the smaller one is also a substring
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res = [i, j]
        
        i, j = res
        return s[i:j+1]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We 

#### Takeaways
---
**Lessons Learned?**