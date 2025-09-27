---
tags:
  - strings
  - easy
pattern: concat the strings
link: https://leetcode.com/problems/concatenation-of-array/
rating: 1000
last_attempt: 2025-09-01
---
#### Problem
Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (**0-indexed**).

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return _the array_ `ans`.

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```go
import (
	"fmt"
	"slices"
)

func getConcatenation(nums []int) []int {
	return slices.Concat(nums, nums)
}
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Lessons Learned
---
- 

#### Video Breakdown
---