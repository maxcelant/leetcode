---
tags:
  - medium
  - heaps
link:
rating:
last_attempt: 2025-09-21
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
The idea is simple. Since it's a sorted array, we need to find the subarray range which has all the closest values. By using two pointers, we check the delta of a given value and move the side that has a larger delta.
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
