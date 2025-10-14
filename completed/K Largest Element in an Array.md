---
tags:
  - meta
  - medium
  - heaps
link: https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 5
last_attempt: 2025-10-10
rate:
  - ★★★★★
---
#### Problem
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

>Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
>Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


#### Notes
---
Use a heap, each push is a `O(logn)` operation and each pop is a `O(logk)` operation so in total it's a `O(n+klogn)` time complexity.
#### Code
---

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        res = float('-inf')
        while k > 0:
            res = heapq.heappop(heap)
            k -= 1
        return -res
```
