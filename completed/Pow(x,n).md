---
tags:
  - math
  - meta
  - medium
link: https://leetcode.com/problems/powx-n/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 3
last_attempt: 2025-10-13
rate:
  - ★★★
---
#### Problem
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

>Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

>Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

>Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


#### Notes
---
Use a recursive divide and conquer approach. On each iteration we:
1. Multiply x by itself
2. Divide n by 2
The important detail is that when `n` is odd, we need to split off the constant (example below). So there are two possible branches in this recursive func.

![[Pasted image 20251012213146.png]]

In the case that `n` is negative e.g. `pow(2, -3)`, this is the same as doing `1 / pow(2, 3)`. Hence, the correct way to handle this is to do 1 over the negative `n` value.

#### Code
---
**Time Complexity**: O(logn)
**Space Complexity**: O(logn)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: we simply return 1
        if n == 0:
            return 1
        # Edge case: if n is negative then we do 1 / pow(x, -n)
        # example: pow(2, -3) becomes 1 / pow(2, 3)
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # When it's odd, we split of the single and multiply the remaining chunk
        # example: 2^5 -> 2 * 2^4
        if n % 2:
            return x * self.myPow(x * x, (n-1) / 2)
        # When even, we simply multiply x by 2 and divide n by 2
        return self.myPow(x * x, n / 2)
```


#### Follow Up: *"What about iterative approach?"*
**Time Complexity**: O(logn)
**Space Complexity**: O(1)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        # Keep track if it was a negative exponent
        is_neg = n < 0
        n = abs(n)
        while n != 0:
            if n % 2 == 1:
                n -= 1
                res *= x
            n //= 2
            x *= x
        if is_neg:
            res = 1 / res
        return res
```