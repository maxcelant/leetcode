---
tags:
  - sliding-window
  - easy
  - meta
link: https://leetcode.com/problems/contains-duplicate-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★★
  - ★★★
  - ★★★★
  - ★★★★★
---
#### Variants


#### Problem
Given an integer array `nums` and an integer `k`, return `true` _if there are two **distinct indices**_ `i` _and_ `j` _in the array such that_ `nums[i] == nums[j]` _and_ `abs(i - j) <= k`.

**Example 1:**

**Input:** nums = [1,2,3,1], k = 3
**Output:** true

#### Notes
The window is the size of k, once we reach the size of k, we start removing from the left side.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(K)

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True
            window.add(n)
            if len(window) > k:
                window.remove(nums[i - k])
        return False
```


#### Follow Up: *""*

```python

```