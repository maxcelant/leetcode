---
tags:
pattern:
link: https://neetcode.io/problems/two-integer-sum-ii?list=neetcode250
rating: 1000
last_attempt: 2025-09-20
---
#### Problem
Given an array of integers `numbers` that is sorted in **non-decreasing order**.

Return the indices (**1-indexed**) of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 < index2`. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be **exactly one valid solution**.

Your solution must use O(1)O(1) additional space.

**Example 1:**

```java
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
```

Explanation:  
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, `index1` = 1, `index2` = 2. We return `[1, 2]`.

#### Notes
---
- Pretty simple two pointers problem

#### Code
---

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cursum = numbers[l] + numbers[r]
            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [l+1, r+1]
        return [-1, -1]
```
