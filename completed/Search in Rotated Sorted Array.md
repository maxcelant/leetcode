---
tags:
  - binary-search
  - medium
rating: 3
last_attempt: 2025-05-10
---
#### Variants


#### Problem
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4

#### Notes
1. Figure out which side you are on, left or right.
2. Think about the 2 possible cases for each side.

If I'm on the left side and the target is greater than the left boundary, which direction should I go? **left**
If I'm on the left side and the target is greater than the middle value, which direction should I go? **left**



#### Code
**Time Complexity**: O(logn)
**Space Complexity**: O(1)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # On left side
            if nums[l] <= nums[m]:
	            # Target is greater than middle or
	            # Target is less than left boundary
	            # Go right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # On right side
            else:
	            # Target is less than middle or
	            # Target is greater than right boundary
	            # Go left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
```