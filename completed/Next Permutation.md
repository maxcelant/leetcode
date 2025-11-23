---
tags:
  - two-pointers
  - medium
  - meta
link: https://leetcode.com/problems/next-permutation/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-17
rate:
  - ★★★★★
---
#### Problem
A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, _find the next permutation of_ `nums`.

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

#### Notes
---
>[!tip] 
>One way to think about this problem is "What is the next greatest value you could make with the integers?". If you have 123, then the next greater value is 132.

Find the pivot point:
To find the pivot, we start from the right and move left. The values should be monotonically increasing UP TO the `pivot` point. It should be the max.

What this means conceptually is that the value to the left of the `pivot` _should_ be smaller than it (since its no longer monotonically increasing). So we need to swap the value to the left of the `pivot` with the right-most value that is GREATER than the left.

![[Pasted image 20251018155305.png]]

>[!example]
>- `[1,2,3,9,6,4,2]`, we reach `9`, the pivot. So we look at the value left of the pivot, `3`.
>- We find the first number greater than `3` starting from the right. In this case it's `4`. 
>- We swap `3` and `4`.
>- Result: `[1,2,4,9,6,3,2]. THIS IS NOT THE END.


After swapping them, we need to "reset" the values starting from the pivot. We do this by reversing the substring from `pivot` to the end.

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums) - 1
        # Find the pivot point
        pivot = N
        while pivot > 0 and nums[pivot-1] >= nums[pivot]:
            pivot -= 1
        
        # Now we need to find the best value to swap with
        if pivot != 0:
            right = N
            while nums[right] <= nums[pivot-1]:
                right -= 1
            # Swap rightmost and pivot
            nums[right], nums[pivot-1] = nums[pivot-1], nums[right]
        
        # Reverse the entire substring from pivot to end
        left = pivot
        right = N
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left, right = left + 1, right - 1
```


#### Follow Up: *""*

```python

```