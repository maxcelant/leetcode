---
tags:
  - medium
  - 2d-dynamic-programming
  - nvidia
  - meta
pattern: Use 2D dp table, fill in default palindromes, traverse all substrings and look at bottom left value to see if that one is also a palindrome
link: https://neetcode.io/problems/longest-palindromic-substring
rate:
  - ★★★★
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

```go
func longestPalindrome(s string) string {
    // Default the result to a single value palindrome
    res := string(s[0])
    N := len(s)
    // Create a 2d matrix.
    dp := make([][]bool, N)
    for i := range s {
        dp[i] = make([]bool, N)
    }
    // A single value palindromes are valid 
    for i := range s {
        dp[i][i] = true
    }
    // Check if 2 digit palindromes are valid
    for i := 1; i < N; i++ {
        if s[i] == s[i-1] {
            dp[i-1][i] = true
            res = s[i-1:i+1]
        }
    }
    // Check sizes larger than 2
    for size := 2; size < N; size++ {
        for i := 0; i < N - size; i++ {
            j := i + size
            if s[i] == s[j] && dp[i+1][j-1] {
                dp[i][j] = true
                res = s[i:j+1]
            }
        }
    }
    return res
}
```
