---
tags:
  - binary-search
  - medium
rating: 2
pattern: Use right value compared to middle value to decrement until you find smallest element.
last_attempt: 2025-05-09
---
#### Intuition
---
- There are two cases to handle:
	1. The array is actually not rotated, and in that case the min is `nums[0]`.
		- We can check by seeing if `nums[0] < nums[-1]`.
		- Just return `nums[0]`
	2. The array is rotated.
		- if `m < r` then `r = m
		- if `m > r` then `l = m + 1`

>![[Pasted image 20250306111027.png]]

#### Code
---

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
```

#### Insight
---
- We return `nums[l]` because that is the last updated value that points to the minimum. Since we stop when `l == r`, this occurs BEFORE we update `m` again, so to have the correct min, we return `nums[l]`.
- 

#### Takeaways
---
- **Where did I go wrong?**
	- I was trying to compare mid to the left value and then decrementing the right pointer, which makes no sense. Compare it the to the right instead and decrement.
	- I need to use `r = m`, because when the middle is less than the right pointer. It _could_ be the minimum already.
- **Lessons Learned?**
	- Think about edge cases like the array actually not being rotated.
	- 
- **Aha Moments?**