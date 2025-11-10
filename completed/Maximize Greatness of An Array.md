---
tags:
  - medium
  - nvidia
  - two-pointers
link: https://leetcode.com/problems/maximize-greatness-of-an-array/
last_attempt: 2025-11-03
rate:
  - ★★★★
---
#### Variants


#### Problem
You are given a 0-indexed integer array `nums`. You are allowed to permute `nums` into a new array `perm` of your choosing.

We define the **greatness** of `nums` be the number of indices `0 <= i < nums.length` for which `perm[i] > nums[i]`.

Return _the **maximum** possible greatness you can achieve after permuting_ `nums`.

**Example 1:**

>**Input:** nums = [1,3,5,2,1,3,1]
**Output:** 4
**Explanation:** One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.

**Example 2:**

>**Input:** nums = [1,2,3,4]
**Output:** 3
**Explanation:** We can prove the optimal perm is [2,3,4,1].
At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.

#### Notes
If we sort it, we can simply use two pointers. Every time the right values is larger than the left, we move the left pointer forward one and increment the result.

#### Code
**Time Complexity**: O(nlogn)
**Space Complexity**: O(n)

```python
func maximizeGreatness(nums []int) int {
    res := 0
    slices.Sort(nums)
    l := 0
    for r, _ := range nums {
        if nums[r] > nums[l] {
            l += 1
            res += 1
        }
    }
    return res
}
```


#### Follow Up: *""*

```python

```