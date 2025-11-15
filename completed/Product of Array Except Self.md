---
tags:
  - arrays
  - medium
  - nvidia
last_attempt: 2025-11-15
rate:
  - ★★★★
link: https://leetcode.com/problems/product-of-array-except-self/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
---
#### Variants


#### Problem
Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

```
**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]
```

#### Notes
Remember to create a `result` array. We use the `nums` array to calculate the updated prefix / suffix.

As you scan from left to right, we are accumulating the prefix. Since the prefix needs to be the produce of everything **before the current value**, we want to calculate it AFTER we get the result for that index!

#### Code
**Time Complexity**:
**Space Complexity**: 

```go
func productExceptSelf(nums []int) []int {
    res := make([]int, len(nums))
    prefix, suffix := 1, 1
    for i := range nums {
        res[i] = prefix
        prefix *= nums[i]
    }
    for i := len(nums) - 1; i >= 0; i-- {
        res[i] *= suffix
        suffix *= nums[i]
    }
    return res
}
```