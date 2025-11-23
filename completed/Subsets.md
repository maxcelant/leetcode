---
tags:
  - backtracking
  - medium
  - meta
link: https://leetcode.com/problems/subsets/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-22
rate:
  - ★★★★
---
#### Variants

#### Problem
Given an integer array `nums` of **unique** elements, return _all possible_ _subsets_ _(the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```
**Input:** nums = [0]
**Output:** [[],[0]]
```
#### Notes

#### Code
**Time Complexity**: O(2^n) because at every point, we have two decisions: take or don't take.
**Space Complexity**: 

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            res.append(subset.copy())
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res
```
