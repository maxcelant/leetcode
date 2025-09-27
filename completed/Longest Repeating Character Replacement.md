---
tags:
  - sliding-window
  - hashing
  - medium
rating: 5
last_attempt: 2025-09-21
link: https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode250
---
#### Problem
You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

**Example 1:**

```java
Input: s = "XYYX", k = 2

Output: 4
```

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

**Example 2:**

```java
Input: s = "AAABABB", k = 1

Output: 5
```

#### Notes
---
We keep track of the most frequent element as we go along by using a dict + a variable to check if the new character is the most frequent.

If the size of the window minus the most frequent is less than or equal to `k`, then that's a viable result. Otherwise, we need to shrink the window.
#### Code
---

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = res = most_freq = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most_freq = max(most_freq, freq[s[r]])
            if (r - l + 1) - most_freq <= k:
                res = max(res, r-l+1)
            else:
                freq[s[l]] -= 1
                l += 1
        return res
```
