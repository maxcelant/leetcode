---
tags:
  - nvidia
  - prefix
  - medium
link: https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-thirty-days
last_attempt: 2025-11-04
rate:
  - ★★★★
---
#### Variants

#### Problem
You are given a **0-indexed** integer array `nums` of length `n`.

`nums` contains a **valid split** at index `i` if the following are true:

- The sum of the first `i + 1` elements is **greater than or equal to** the sum of the last `n - i - 1` elements.
- There is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.

Return _the number of **valid splits** in_ `nums`.

#### Notes
We first get the total sum of all the values and store that in `rightSum`.

We iterate from left to right (excluding last value). At each step we subtract the i-th term from `rightSum` and add that i-th term to `leftSum`.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```go
func splitArray(nums []int) int {
    res, leftSum, rightSum := 0, 0, 0
    for _, n := range nums {
        rightSum += n
    }
    for i := 0; i < len(nums) - 1; i++ {
        leftSum += nums[i]
        rightSum -= nums[i]
        if leftSum >= rightSum {
            res += 1
        }
    }
    return res
}

```
