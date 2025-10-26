---
tags:
  - arrays
  - medium
  - nvidia
last_attempt: 2025-10-24
rate:
  - ★★★
link: https://leetcode.com/problems/product-of-array-except-self/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
---
#### Variants


#### Problem
Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

#### Notes
As you scan from left to right, we are accumulating the prefix. Since the prefix needs to be the produce of everything **before the current value**, we want to calculate it AFTER we get the result for that index!

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
```go
func productExceptSelf(nums []int) []int {
    N := len(nums)
    res := make([]int, N)
    prefix := 1
    for i := 0; i < N; i++ {
        res[i] = prefix
        prefix *= nums[i]
    }
    postfix := 1
    for i := N - 1; i >= 0; i-- {
        res[i] *= postfix
        postfix *= nums[i] 
    }
    return res
}
```

```python
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]
    
    return res
```
```


#### Follow Up: *""*

```python

```