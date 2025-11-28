---
tags:
  - nvidia
  - medium
  - 2d-dynamic-programming
link: https://leetcode.com/problems/maximal-square/?envType=company&envId=nvidia&favoriteSlug=nvidia-more-than-six-months
last_attempt: 2025-11-26
rate:
  - ★★
---
#### Variants

#### Problem
Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, _find the largest square containing only_ `1`'s _and return its area_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

```
**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
**Output:** 4
```
#### Notes
Use a DP Matrix. Where the value in the DP matrix indicates the size of the square at the bottom right corner of the square (example below for context).

![[Pasted image 20251126000723.png]]

Whenever we have a `1` we ask the question, is my what are the values of my top, diagonal top-left and left? If they are all 1, then I am a square!

>[!important]
>Notice how the DP matrix is one row/col larger. This is to account for the looking behind in the matrix and so that we have defaults for the first row and column in our original matrix. Otherwise we would do a look-back and get a "index out of range" error.

#### Code
**Time Complexity**: O(N\*M)
**Space Complexity**: O(N\*M)

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Make DP matrix bigger to account for looking behind
        # aka dp[1][1] is technically [0][0] in the original
        # This is so we can have a row/col of 0's as a baseline
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        res = 0
        # +1 because we are looking one row/col behind
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == "1":
                    # Check top, top-left diag and left and find min, add 1 to it
                    dp[i][j] = min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1]) + 1
                res = max(res, dp[i][j])
        return res * res
```
