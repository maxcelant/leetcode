---
tags:
  - sliding-window
  - medium
link: https://neetcode.io/problems/minimum-size-subarray-sum?list=neetcode250
rating: 4
last_attempt: 2025-09-21
---
#### Problem
You are given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

A **subarray** is a contiguous non-empty sequence of elements within an array.

**Example 1:**

```java
Input: target = 10, nums = [2,1,5,1,5,3]

Output: 3
```

Explanation: The subarray `[5,1,5]` has the minimal length under the problem constraint.

#### Notes
---
We keep track of a running total, if go above the target, we continuously shrink until we are below the target. All the while, we jot down the length of the window to see if it's smaller than the current result.

#### Code
---

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = cur = 0
        res = float('inf')
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
```
