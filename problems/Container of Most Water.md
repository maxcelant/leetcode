---
tags:
  - two-pointers
pattern: use two pointers, get min of two sides * the distance between l and r
rating: 1000
last_attempt: 2025-09-21
link: https://neetcode.io/problems/max-water-container?list=neetcode250
---
#### Problem
You are given an integer array `heights` where `heights[i]` represents the height of the ithith bar.

You may choose any two bars to form a container. Return the _maximum_ amount of water a container can store.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/77f004c6-e773-4e63-7b99-a2309303c700/public)

```java
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
```

#### Notes
---
- 

#### Code
---

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')
        l, r = 0, len(heights) - 1 
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            res = max(res, height * width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
```
