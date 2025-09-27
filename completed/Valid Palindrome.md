---
tags:
  - two-pointers
  - easy
pattern: remove any non alnum values, use reverse list comparison
link: https://leetcode.com/problems/valid-palindrome/description/
rating: 5
last_attempt: 2025-05-02
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
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for c in s:
            if c.isalnum():
                new_s.append(c.lower())
        return new_s == new_s[::-1]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**