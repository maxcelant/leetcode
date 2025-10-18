---
tags:
  - binary-search
  - meta
  - medium
link:
rating: 3
last_attempt: 2025-10-10
rate:
  - ★★★★
---
#### Problem
A valley element is an element strictly less than its neighbors.

Given a 0-indexed integer array nums, find a valley element and return its index. If multiple valleys exist, return the index of any one. Assume nums[-1] = nums[n] = +∞ (so edge elements can be valleys). Must run in O(log n).

Examples: 
>Input: [1,2,3,1] 
>Output: 0 (or 3) 

>Input: [1,2,1,3,5,6,4] 
>Output: 2 (or 0 or 6)

#### Notes
---
Look at [[Find Peak Element]]e

#### Code
---

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
		l, r = 0, len(nums) - 1
		while l < r:
			m = l + (r - l) // 2
			if nums[m] < nums[m+1]:
				r = m
			else:
				l = m + 1
		return l
```
