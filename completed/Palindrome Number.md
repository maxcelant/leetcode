---
tags:
  - meta
  - easy
  - math
link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-06
rate:
  - ★★★
---
#### Variants


#### Problem
Given an integer `x`, return `true` _if_ `x` _is a_ _**palindrome**__, and_ `false` _otherwise_.

**Example 1:**

>**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

>**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

>**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

#### Notes
We build the reverse half of the number by taking the digits from `x` until the `reverse` is larger. 

Doing `x % 10` always takes the last digit. `x /= 10` gets rid of the last digit.

At the end they will either match OR the `reverse` will have the middle number, for which we can remove since it's the middle of the palindrome and doesn't have an effect.

>**Example**
>`reversed = 123` while `x=12`, we get rid of the `3`.

#### Code
**Time Complexity**: O(logN)
**Space Complexity**: 

```go
func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    // If the last digit is 0 then it can only be a 
    // palindrome if the whole number is 0
    if x % 10 == 0 && x != 0 {
        return false
    }
    reversed := 0
    for x > reversed {
	    lastDigit := x % 10
        reversed = reversed * 10 + lastDigit
        x /= 10
    }
    // If the number is odd, we need to get rid of the middle digit
    return reversed == x || reversed / 10 == x
}
```
