---
tags:
  - hashing
  - medium
  - meta
link: https://leetcode.com/problems/random-pick-index/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-17
rate:
  - ★★★★★
---
#### Problem
Given an integer array `nums` with possible **duplicates**, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

Implement the `Solution` class:

- `Solution(int[] nums)` Initializes the object with the array `nums`.
- `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. If there are multiple valid i's, then each index should have an equal probability of returning.

**Example 1:**

**Input**
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
**Output**
[null, 4, 0, 2]

**Explanation**
```
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
```
#### Notes


#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def __init__(self, nums: List[int]):
        self.indexes = defaultdict(list)
        for i, n in enumerate(nums):
            self.indexes[n].append(i)

    def pick(self, target: int) -> int:
        i = random.randint(0, len(self.indexes[target])-1)
        return self.indexes[target][i]
```
