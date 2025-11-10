---
tags:
  - 1d-dynamic-programming
  - sliding-window
  - kadanes-algorithm
link: https://neetcode.io/problems/maximum-subarray
last_attempt: 2025-11-03
rate:
  - ★★★★
---
#### Variants


#### Problem


#### Notes
Use [[Kadane's Algorithm]]! See if the current sum is less than 0, then reset it.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```go
func maxSubArray(nums []int) int {
    res, cursum := nums[0], 0
    for _, n := range nums {
        if cursum < 0 {
            cursum = 0
        }
        cursum += n
        res = max(res, cursum)
    }
    return res
}
```


#### Follow Up: *""*

```python

```