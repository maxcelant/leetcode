---
tags:
  - 2d-dynamic-programming
  - meta
  - medium
link: https://leetcode.com/problems/palindromic-substrings/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-16
rate:
  - ★★★★
---
#### Variants
- [[Longest Palindromic Substring]]

#### Problem
Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

```
**Input:** s = "abc"
**Output:** 3
**Explanation:** Three palindromic strings: "a", "b", "c".
```
**Example 2:**

```
**Input:** s = "aaa"
**Output:** 6
**Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

#### Notes

Almost identical to [[Longest Palindromic Substring]] except we use a boolean DP matrix here because we just want the total palindromes.

![[Pasted image 20251116182408.png]]

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            dp[i][i] = True
            res += 1
            
        for i in range(len(s) - 1):
            j = i + 1
            if s[i] == s[j]:
                dp[i][j] = True
                res += 1 
        
        for size in range(2, len(s)):
            for i in range(len(s) - size):
                j = i + size
                if s[i] == s[j]:
                    # Check if the inner palindrome is also valid
                    dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    res += 1
        return res
```
