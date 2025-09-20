---
tags:
  - easy
  - two-pointers
pattern: Walk through strings with a pointer to each, alternate adding to the list
link: https://neetcode.io/problems/merge-strings-alternately?list=neetcode250
rating: 1000
last_attempt: 2025-09-20
---
#### Problem
You are given two strings, `word1` and `word2`. Construct a new string by merging them in **alternating** order, starting with `word1` — take one character from `word1`, then one from `word2`, and repeat this process.

If one string is longer than the other, append the remaining characters from the longer string to the end of the merged result.

Return the final merged string.

**Example 1:**

```java
Input: word1 = "abc", word2 = "xyz"

Output: "axbycz"
```

**Example 2:**

```java
Input: word1 = "ab", word2 = "abbxxc"

Output: "aabbbxxc"
```

#### Notes
---
- 

#### Code
---

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        res = []
        while p1 < len(word1) and p2 < len(word2):
            res.append(word1[p1])
            res.append(word2[p2])
            p1, p2 = p1 + 1, p2 + 1
        
        if p1 < len(word1):
            res.append(word1[p1:])
        if p2 < len(word2):
            res.append(word2[p2:])
        
        return "".join(res)
```
