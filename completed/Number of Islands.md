---
tags:
  - graphs
  - medium
  - nvidia
  - dfs
link: https://leetcode.com/problems/number-of-islands/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-three-months
last_attempt: 2025-11-28
rate:
  - ★★★★★
---
#### Variants
- [[Making a Large Island]]

#### Problem
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

#### Notes
Use visited set, traverse each island, increment result.

#### Code
**Time Complexity**: O(N\*M)
**Space Complexity**: O(N\*M))

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.visited = set()
        res = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == "0":
                    continue
                if (r, c) not in self.visited:
                    self.explore(r, c)
                    res += 1
        return res

    def explore(self, r, c):
        if (
            not (0 <= r < len(self.grid)) or
            not (0 <= c < len(self.grid[0])) or
            self.grid[r][c] == "0" or
            (r, c) in self.visited
        ):
            return
        self.visited.add((r, c))
        self.explore(r + 1, c)
        self.explore(r - 1, c)
        self.explore(r, c + 1)
        self.explore(r, c - 1)
```
