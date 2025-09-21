---
tags:
  - two-pointers
  - medium
pattern:
link: https://neetcode.io/problems/rotate-array?list=neetcode250
rating: 3
last_attempt: 2025-09-21
---
#### Problem
You are given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```java
Input: nums = [1,2,3,4,5,6,7,8], k = 4

Output: [5,6,7,8,1,2,3,4]
```

Explanation:  
```
rotate 1 steps to the right: [8,1,2,3,4,5,6,7]  
rotate 2 steps to the right: [7,8,1,2,3,4,5,6]  
rotate 3 steps to the right: [6,7,8,1,2,3,4,5]  
rotate 4 steps to the right: [5,6,7,8,1,2,3,4]
```

#### Notes
---
- If we reverse the entire array, then reverse the first k elements and the last k+1 elements, we get the correct rotated array.
- `k` can be larger than N, so use modulo to get the true rotation value.

**Example**
1. `[1,2,3,4,5], k=3`
2. Reverse entire array:`[5,4,3,2,1]`
3. Reverse first k values: `[3,4,5,2,1]`
4. Reverse last k+1 values: `[3,4,5,1,2]`
5. Done.

#### Code
---

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums) - 1
        k %= N+1
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        reverse(0, N)
        reverse(0, k-1)
        reverse(k, N)
```
