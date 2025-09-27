---
tags:
  - graphs
  - two-pointers
link: https://leetcode.com/problems/spiral-matrix/description/
rating: 2
last_attempt: 2025-09-27
---
#### Problem
Given an `m x n` `matrix`, return _all elements of the_ `matrix` _in spiral order_.

**Example 1:**
![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```
**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]
```

#### Notes
---
The important part about this problem is bounds checking when traversing the bottom row and the left column. You shouldn't traverse the bottom row if the top and bottom pointers are pointing to the same row because that means you've already walked that row (example for context).


>![[Pasted image 20250927174625.png|600]]


#### Code
---

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1
        res = []
        while left <= right and top <= bot:
            # Go from left to right on the top row
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            # Go from top right to bottom right
            for i in range(top, bot+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bot:
                # Go from bot right to bot left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bot][i])
                bot -= 1
            if left <= right:
                # Go from bot left to top left
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
```
