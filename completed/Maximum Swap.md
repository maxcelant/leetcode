---
tags:
  - greedy
  - medium
  - meta
link: https://leetcode.com/problems/maximum-swap/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-22
rate:
  - ★★★
---
#### Variants

#### Problem

#### Notes
Start from the right side and go left. We are scanning and trying to find the smallest value to the left of our `maxVal` to swap with.

>[!important]
>Even if we find a better `maxVal`, we don't update the swap until we find a smaller value to it's left.
#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Store the max value as a (index, value) tuple since we will need both
        maxVal = (-1, -1) 
        swap1 = swap2 = -1
        num = list(str(num))
        for r in range(len(num) - 1, -1, -1):
            # Update the max value if we find a bigger value
            if int(num[r]) > maxVal[1]:
                maxVal = (r, int(num[r]))
            # Only update the swap if we found a new swap with that bigger value
            # otherwise this won't change
            elif int(num[r]) < maxVal[1]:
                swap1 = r
                swap2 = maxVal[0]
        if swap1 != -1 and swap2 != -1:
            num[swap1], num[swap2] = num[swap2], num[swap1]
        return int(''.join(num))
        
```
