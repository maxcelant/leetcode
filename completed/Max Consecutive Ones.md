---
tags:
  - medium
  - meta
  - sliding-window
link: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-16
rate:
  - ★★★★★
---
#### Problem
Given a binary array `nums` and an integer `k`, return _the maximum number of consecutive_ `1`_'s in the array if you can flip at most_ `k` `0`'s.

**Example 1:**

>**Input:** nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
**Output:** 6
**Explanation:** [1,1,1,0,0,**1**,1,1,1,1,**1**]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

#### Notes
---
This is a pretty straight-forward sliding window problem.

You continue to expand the window while k > 0, and when we reach the point where k < 0, then we need to close the window from the left side.

#### Code
---
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, (r - l) + 1)
        return res
```


#### Follow Up: *""*

```python

```