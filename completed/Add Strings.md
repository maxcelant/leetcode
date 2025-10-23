---
tags:
  - strings
  - meta
  - easy
  - math
link: https://leetcode.com/problems/add-strings/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-21
rate:
  - ★★★★
---
#### Variants
- [[Add Two Numbers]]

#### Problem
Given two non-negative integers, `num1` and `num2` represented as string, return _the sum of_ `num1` _and_ `num2` _as a string_.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

**Example 1:**

>**Input:** num1 = "11", num2 = "123"
**Output:** "134"

**Example 2:**

>**Input:** num1 = "456", num2 = "77"
**Output:** "533"

#### Notes
---
This problem is very similar to the linked list one: [[Add Two Numbers]].

We use pointers to walk the strings using elementary school addition to calculate the value and the carry.

>[!important]
>Remember how to calculate the carry and the value!
>`13 % 10 = 3`, this is the value.
>`13 // 10 = 1`, this is the carry.


#### Code
---
**Time Complexity**: O(max(N, M))
**Space Complexity**: O(1)

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        # Move while at least one of them still has numbers
        while p1 >= 0 or p2 >= 0:
            v1 = int(num1[p1]) if p1 >= 0 else 0
            v2 = int(num2[p2]) if p2 >= 0 else 0
            value = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            res.append(str(value))
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(str(carry))
        
        # Flip the final result bc we did it back to front
        return ''.join(res[::-1])
            
```


#### Follow Up: *""*

```python

```