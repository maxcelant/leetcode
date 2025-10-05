---
tags:
  - medium
  - 2d-matrix
link: https://leetcode.com/problems/rotate-image/
rating: 3
last_attempt: 2025-09-28
---
#### Problem
You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [[7,4,1],[8,5,2],[9,6,3]]
```

#### Notes
---
You first transpose the matrix (the rows and columns flip so now that cols are the rows and vice-versa) and then reverse each row. Ta-da.

#### Code
---

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for r in matrix:
            r.reverse()
```
