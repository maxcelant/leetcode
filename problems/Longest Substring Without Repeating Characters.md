---
tags:
  - sliding-window
  - medium
rating: 1000
last_attempt: 2025-09-21
link: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode250
---
#### Problem
Given a string `s`, find the _length of the longest substring_ without duplicate characters.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```java
Input: s = "zxyzxyz"

Output: 3
```

Explanation: The string "xyz" is the longest without duplicate characters.

**Example 2:**

```java
Input: s = "xxxx"

Output: 1
```

#### Notes
---
Use a set for the window for O(1) checks. Remove the left char from the window until the right char isn't inside the window anymore.
#### Code
---

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, len(window))
        return res
```
