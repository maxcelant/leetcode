---
tags:
  - binary-search
  - easy
  - meta
link: https://leetcode.com/problems/kth-missing-positive-number/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-13
rate:
  - ★★★
---
#### Problem


#### Notes
---
We use an array with no missing values in it. The number of missing integers is a simple difference between the corresponding elements of these two arrays.

We look at the number in both arrays and compare.

Example:
- `[2,3,4,7,11]` vs `[1,2,3,4,5,6,7,8,9,10,11]`
- `7 - 4 = 3`
- `3` would be `k` in this case.

So by using binary search, we can track down the right `k` value. Since the value we are looking for won't be in the array itself, we need to track down the _lower bound_ of when our pointers meet ([this explains it well](https://youtu.be/9L2jd7mSeV8?si=9DE5zNBh9NVGtmTt&t=565)).

For details on [[Boundary-Based Binary Search]].

Once we reach the lower bound value (which will be our right pointer, we know we are right + k + 1 steps away from the missing value!

>[!important]
>We can use the middle index itself to know how many values are missing since the array without missing start from 1 -> N

>[!important]
>We use `while l <= r` because we want to ensure they cross passed each other!

**Example**
1. Inputs: `arr=[2,3,4,7,11]`, `k=5`
2. Initialize: `l=0`, `r=4`
3. First iteration, `m=2`, `arr[m]=4`. `4 - 2 - 1 = 1`. `1 < k`, so we shift the left pointer.
4. Now `l=3`, `r=4`, `m=3`. `arr[m]=7`. `7-3-1 = 3`. `3 < k`, so we shift the left pointer again.
5. Now `l=4`, `r=4`, `m=4`. `arr[m]=11`. `11-4-1 = 6`. `6 > k`, so we shift the right pointer to the left.
6. Now `l=4`, `r=3`, which means we break out of the loop.
7. Finally the result will be `r + k + 1`, which is `3 + 5 + 1 = 9`. Also `l + k` works!

#### Code
---
**Time Complexity**: O(logN)
**Space Complexity**: O(1)

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            # Get the difference from the actual and desired position
            if arr[m] - m - 1 >= k:
                r = m - 1
            else:
                l = m + 1
        return r + k + 1
```
