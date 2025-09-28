---
tags:
  - two-pointers
  - 2d-matrix
link: https://leetcode.com/problems/spiral-matrix/description/
rating: 3
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

Also, be careful with your right and bottom pointers, they are technically out of bounds if you loop starting from those positions so make sure to subtract one.

#### Code
---

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L, R = 0, len(matrix[0])
        TOP, BOT = 0, len(matrix)
        res = []
        while L < R and TOP < BOT:
            # Top row
            for i in range(L, R):
                res.append(matrix[TOP][i])
            TOP += 1
            # Right col
            for i in range(TOP, BOT):
                res.append(matrix[i][R-1])
            R -= 1
            # If the top and right pointers or the left and right pointers
            # are pointing to the same row, then we can skip since it
            # would be doing repetitive work
            if TOP < BOT:
                # ? might be off by 1
                for i in range(R-1, L-1, -1):
                    res.append(matrix[BOT-1][i])
                BOT -= 1
            if L < R:
                for i in range(BOT-1, TOP-1, -1):
                    res.append(matrix[i][L])
                L += 1
        return res
```
