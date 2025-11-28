---
tags:
  - medium
  - nvidia
  - two-pointers
link: https://leetcode.com/problems/sort-colors/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-thirty-days
last_attempt: 2025-11-28
rate:
  - ★★★
---
#### Variants

#### Problem

#### Notes
Uses the "Dutch flag algorithm".
1. Init 3 pointers.
2. Swap with `p0` if `cur` is 0. Shift both
3. Swap with `p2` if `cur` is 2. Only shift p2 left.
4. Go until `cur > p2`.

>[!important]
>Pay careful attention as to why we don't increment when we swap with `p2`.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cur, p0, p2 = 0, 0, len(nums) - 1
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            # Swap and shift the p2 pointer down
            # We don't shift the cur pointer in this 
            # case because the swapped value could be a 0
            # Which means we need to do another swap with p0
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1
```
