---
tags:
  - sliding-window
rating: 5
link:
last_attempt: 2025-09-21
---
#### Problem
You are given two strings `s1` and `s2`.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

**Example 1:**

```java
Input: s1 = "abc", s2 = "lecabee"

Output: true
```

Explanation: The substring `"cab"` is a permutation of `"abc"` and is present in `"lecabee"`.

#### Notes
---
The whole idea is to compare the Counters to see if the frequencies of all the elements in the current window match that of `c1`.

We shrink the window when it's larger than the size of `s1`, since that's not a viable solution.

Caveat: remember to delete the element from the counter IF it reaches 0. Because that will count in the equality.

#### Code
---

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            c2[s2[r]] += 1
            while (r - l + 1) > len(s1):
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1
            if c2 == c1:
                return True
        return False
```
