---
tags:
  - easy
  - nvidia
  - two-pointers
link: https://leetcode.com/problems/move-zeroes/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-11-25
rate:
  - ★★★
---
#### Variants

#### Problem
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example 1:**

```
**Input:** nums = [0,1,0,3,12]
**Output:** [1,3,12,0,0]
```
#### Notes
Think of the problem as "move all non-zero values to the front".

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            # If the right value is non zero
            # Update the left value and shift it forward
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
        
        # Replace all remaining left values with 0s
        while l < len(nums):
            nums[l] = 0
            l += 1
        
        return nums
```
