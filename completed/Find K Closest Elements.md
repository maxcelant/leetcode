---
tags:
  - medium
  - binary-search
link: https://leetcode.com/problems/find-k-closest-elements/description/
last_attempt: 2025-09-21
rate:
  - ★★★
---
#### Problem
You are given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

- `|a - x| < |b - x|`, or
- `|a - x| == |b - x|` and `a < b`

**Example 1:**

```java
Input: arr = [2,4,5,8], k = 2, x = 6

Output: [4,5]
```

#### Notes
---
An important realization is that the left pointer can never be greater than `len(array) - k`. Because that's the size of the window.

At each step in the binary search we need to ask ourselves, is `arr[l]` closer to `x` than `arr[l+k]`? Only one of these two can possibly be in the window! 

So if `arr[l]` is closer to `x`, then we know we need to move the right pointer.

If `arr[l+k]` is closer to `x`, then we need to move the left pointer. 

#### Code
---

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while (r - l) + 1 > k:
            # If delta between left value and x is less than
            # right value and delta, then move right pointer
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]
```
