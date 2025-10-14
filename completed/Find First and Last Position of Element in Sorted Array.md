---
tags:
  - medium
  - meta
  - binary-search
link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-14
rate:
  - ★★★★
---
#### Problem
You are given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```java
Input: nums = [5,7,7,8,8,10], target = 8

Output: [3,4]
```

#### Notes
---
We use binary search but we don't stop when we find the target, we need to continue and find the left and right boundaries. We do a separate search for the left and right side.

The way we find the boundary is by continuing the binary search and moving the opposite pointer towards the biased side. 

Example: If we are looking for the left boundary, we will continue to move the right pointer towards the left side.

Be aware that we only want to do this once the middle is pointing to the target—otherwise this would create problems.


![[Pasted image 20251012225932.png]]
#### Code
---
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBoundary(left_side):
            l, r = 0, len(nums) - 1
            boundary = -1
            while l <= r:
                m = l + (r - l) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    boundary = m
                    if left_side:
                        r = m - 1
                    else:
                        l = m + 1
            return boundary
        return [findBoundary(True), findBoundary(False)]
```


#### Follow Up: *""*

```python

```