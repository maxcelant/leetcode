---
tags:
  - easy
  - two-pointers
  - meta
link:
rating: 4
last_attempt: 2025-10-09
rate:
  - ★★★★
---
#### Problem
You are given two integer arrays `nums1` and `nums2`, both sorted in **non-decreasing order**, along with two integers `m` and `n`, where:
- `m` is the number of valid elements in `nums1`,
- `n` is the number of elements in `nums2`.
    
The array `nums1` has a total length of `(m+n)`, with the first `m` elements containing the values to be merged, and the last `n` elements set to `0` as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in **non-decreasing order** and stored entirely within `nums1`.  
You must modify nums1 in-place and do not return anything from the function.

**Example 1:**

```java
Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

Output: [1,2,10,20,20,40]
```

**Example 2:**

```java
Input: nums1 = [0,0], m = 0, nums2 = [1,2], n = 2

Output: [1,2]
```

#### Notes
---
We start from the end of `nums1` and build the correct string by comparing the values of `nums1` and `nums2` starting from `m` and `n`.

#### Code
---

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cur = len(nums1) - 1
        p1, p2 = m-1, n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[cur] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                p2 -= 1
            cur -= 1

        while p1 >= 0:
            nums1[cur] = nums1[p1]
            p1 -= 1
            cur -= 1
        
        while p2 >= 0:
            nums1[cur] = nums2[p2]
            p2 -= 1
            cur -= 1
```
