---
tags:
  - two-pointers
  - 2d-matrix
link: https://leetcode.com/problems/spiral-matrix-ii/description/
rating: 4
last_attempt: 2025-09-27
---
#### Problem
Look at [[Spiral Matrix]]

Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n2` in spiral order.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)

```
**Input:** n = 3
**Output:** [[1,2,3],[8,9,4],[7,6,5]]
```
#### Notes
---
Basically same idea as the first problem except you need to build that matrix and have a constantly increasing value (`cur`) to fill in the current cell as you go along.
#### Code
---

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)] 
        cur = 1
        top = left = 0
        bot = right = n - 1
        while left <= right or top <= bot:
            for i in range(left, right+1):
                matrix[top][i] = cur
                cur += 1
            top += 1
            for i in range(top, bot+1):
                matrix[i][right] = cur 
                cur += 1
            right -= 1
            if top <= bot:
                for i in range(right, left-1, -1):
                    matrix[bot][i] = cur
                    cur += 1
                bot -= 1
            if left <= right:
                for i in range(bot, top-1, -1):
                    matrix[i][left] = cur 
                    cur += 1
                left += 1
        return matrix
```
