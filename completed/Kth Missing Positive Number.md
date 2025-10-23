---
tags:
  - binary-search
  - easy
  - meta
link: https://leetcode.com/problems/kth-missing-positive-number/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-19
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

![[Pasted image 20251019133946.png]]


>[!important]
>We can use the middle index itself to know how many values are missing since the array without missing start from 1 -> N

>[!important]
>We use `while l <= r` because we want to ensure they cross passed each other!

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
            if arr[m] - m - 1 >= k:
                r = m - 1
            else:
                l = m + 1
        return r + k + 1
```


#### Follow Up: *""*

```python

```