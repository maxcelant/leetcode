---
tags:
  - meta
  - medium
  - binary-search
link: https://leetcode.com/problems/find-peak-element/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-11
rate:
  - ★★★★★
---
#### Problem
A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**

>**Input:** nums = [1,2,3,1]
**Output:** 2
**Explanation:** 3 is a peak element and your function should return the index number 2.

**Example 2:**

>**Input:** nums = [1,2,1,3,5,6,4]
**Output:** 5
**Explanation:** Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

#### Notes
---
The fact we need to answer this in `O(logn)` is a dead give away that we should use binary search. 

The idea is that if the middle value is greater then its right neighbor e.g. `[5,4,3]`, then we should go left, because that is where the peak is and we are on the descending slope.

If the middle value is less than the right neighbor e.g. `[3,4,5]`, then we should go right, because we are on the ascending slope.

>[!important]
>The reason we do `r = mid` is because the answer _could be the middle element_ so we don't want to accidentally exclude that value from the range.



#### Code
---

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # We are on the descent of a slope
            # Go the the left
            if nums[mid] > nums[mid+1]:
                r = mid
            # We are an ascent, go to the right
            else:
                l = mid + 1
        return l
```
