---
tags:
  - hashing
  - hard
pattern:
link: https://neetcode.io/problems/first-missing-positive?list=neetcode250
rating: 3
last_attempt: 2025-09-16
---
#### Problem
You are given an unsorted integer array `nums`. Return the **smallest positive integer** that is not present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

**Example 1:**

```java
Input: nums = [-2,-1,0]

Output: 1
```

**Example 2:**

```java
Input: nums = [1,2,4]

Output: 3
```

**Example 3:**

```java
Input: nums = [1,2,4,5,6,3,1]

Output: 7
```

#### Notes
---
- (This is technically sub-optimal solution bc im not using constant space)
- Turn the list into a set for quick lookups.
- The idea is to loop from 1 -> N+1 and see if the current index is i is in the original list.
- If we loop through the whole thing and don't see it, then the answer is N+1.

#### Code
---

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)
        found = False
        res = -1
        for i in range(1, len(nums) + 1):
            if i not in numset:
                found = True
                res = i
                break
        
        if not found:
            res = len(nums) + 1
        
        return res
```
