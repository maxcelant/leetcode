---
tags:
  - easy
  - hashing
link: https://neetcode.io/problems/contains-duplicate-ii?list=neetcode250
rating: 1000
last_attempt: 2025-09-21
---
#### Problem
You are given an integer array `nums` and an integer `k`, return `true` if there are **two distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`, otherwise return `false`.

**Example 1:**

```java
Input: nums = [1,2,3,1], k = 3

Output: true
```

**Example 2:**

```java
Input: nums = [2,1,2], k = 1

Output: false
```

#### Notes
---
Use a hash table of `[value]: index`.
#### Code
---

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in seen:
                j = seen[nums[i]]
                if abs(i - j) <= k:
                    return True
            seen[nums[i]] = i
        return False
```
