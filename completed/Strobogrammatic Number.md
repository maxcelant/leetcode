---
tags:
  - easy
  - meta
  - strings
link: https://leetcode.com/problems/strobogrammatic-number/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-02
rate:
  - ★★★★★
---
#### Variants
- [[Valid Palindrome]]

#### Problem
Return whether or not a given number is strobogrammatic. Strobogrammatic means it looks the same upside down.

#### Notes
Nothing to add.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo_nums = {'1':'1', '8': '8', '6':'9', '9':'6', '0':'0'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in strobo_nums or num[r] not in strobo_nums:
                return False
            if strobo_nums[num[l]] != num[r] or strobo_nums[num[r]] != num[l]:
                return False
            l += 1
            r -= 1
        return True
```