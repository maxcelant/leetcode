---
tags:
  - meta
  - medium
  - 2d-matrix
  - graphs
link: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 3
last_attempt: 2025-10-12
rate:
  - ★★★★
---
#### Problem
Given an `n x n` binary matrix `grid`, return _the length of the shortest **clear path** in the matrix_. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)

>**Input:** grid = [[0,1],[1,0]]
**Output:** 2

#### Notes
---
Basically just BFS in all 8 directions. Watch out for edge cases like when the starting or ending cell is `1` which means you cannot find a path.

Use a visited matrix to keep track of visited cells.

Make sure to do bounds checks and make sure you don't get your rows and columns mixed up.
#### Code
---
**Time Complexity**: O(N\*M)
**Space Complexity**: O(N\*M)

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0]) # N=ROWS, M=COLS
        if grid[0][0] != 0 or grid[N-1][M-1] != 0:
            return -1
        q = deque([])
        q.append((0, 0, 1))
        target = (N-1, M-1)
        # Init the visited array
        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True

        while q:
            x, y, path = q.popleft()
            if (x, y) == target:
                return path
            for dx, dy in [
                (0, 1),   # right
                (0, -1),  # left
                (1, 0),   # down
                (-1, 0),  # up
                (1, 1),   # bottom left
                (-1, -1), # top right
                (1, -1),  # top left
                (-1, 1),  # bottom right
            ]:
                nx, ny = x+dx, y+dy
                if (
                    0 <= nx < N and 
                    0 <= ny < M and
                    not visited[nx][ny] and
                    grid[nx][ny] == 0
                ):
                    visited[nx][ny] = True
                    q.append((nx, ny, path + 1))
        return -1
```


#### Follow Up: *""*

```python

```