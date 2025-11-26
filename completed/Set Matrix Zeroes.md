---
tags:
  - 2d-matrix
  - meta
  - medium
link: https://leetcode.com/problems/set-matrix-zeroes/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★
---
#### Problem
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

**Input:** matrix = [[1,1,1],[1,0,1],[1,1,1]]
**Output:** [[1,0,1],[0,0,0],[1,0,1]]

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

**Input:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**Output:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

#### Notes
**For the O(N) space complexity approach:**
we first create a set of all the zeros in the matrix. We then loop through and update the row and col for those zero values.

**For the O(1) space complexity approach:**
Use the matrix itself as an indicator.
Use the first cell of every row and column as a flag.
We later use these flags to convert the row/col to zeros.
We must handle the first row/column a little differently since technically the first row and column both use `matrix[0][0]` as an indicator. So we will use `matrix[0][0]` to indicate the first row and a `first_col` flag for first column.

#### Code
**Time Complexity**: O(N\*M)
**Space Complexity**: O(N\*M)

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_cells = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_cells.add((r,c))
        
        for r, c in zero_cells:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
            for i in range(len(matrix)):
                matrix[i][c] = 0
```


#### Follow Up: *"Use O(1) Space"*

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    
```