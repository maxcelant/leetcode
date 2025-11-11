---
tags:
  - meta
  - hard
  - dfs
rate:
  - ★★★
last_attempt: 2025-11-07
link: https://leetcode.com/problems/making-a-large-island/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
---

#### Variants


#### Problem
You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

Return _the size of the largest **island** in_ `grid` _after applying this operation_.

An **island** is a 4-directionally connected group of `1`s.

**Example 1:**

**Input:** grid = [[1,0],[0,1]]
**Output:** 3
**Explanation:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

**Example 2:**

**Input:** grid = [[1,1],[1,0]]
**Output:** 4
**Explanation:** Change the 0 to 1 and make the island bigger, only one island with area = 4.

#### Notes
There are two main parts to this problem.
1. Traverse the map and find all the islands.
2. Traverse the map and find all the `0`s.

Track the islands using an incrementing `islandId`. Store the sizes of the islands in a map.

When traversing the island the second time, you need to check all adjacent coordinates but be sure to not check the same island twice! Using a set solves this.

#### Code
**Time Complexity**: O(N\*M)
**Space Complexity**: O(N\*M)

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = set()
        island_sizes = defaultdict(int)
        island_id = 2
        res = 0

        # Explore all islands using DFS
        # Increment island_id every time you see a new one
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 1 and (r, c) not in self.visited:
                    size = self.explore_island(island_id, r, c)
                    island_sizes[island_id] = size
                    res = max(res, size)
                    island_id += 1

        # There are no islands
        if not island_sizes:
            return 1
        
        # If there is only one island, see if it takes up the whole map or not
        if len(island_sizes) == 1:
            if res == len(grid) * len(grid[0]):
                return res
            # If it doesn't take up the whole map, we can confidently add 1 to the result
            return res + 1
        
        # Explore all 0's on the map
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 0:
                    # We need to use a set here to avoid adding the 
                    # same adjacent island more than once
                    islands_seen = set()
                    if r-1 >= 0:
                        islands_seen.add(grid[r-1][c])
                    if r+1 < len(grid):
                        islands_seen.add(grid[r+1][c])
                    if c-1 >= 0:
                        islands_seen.add(grid[r][c-1])
                    if c+1 < len(grid[r]):
                        islands_seen.add(grid[r][c+1])
                    total = 1
                    for island_id in islands_seen:
                        total += island_sizes[island_id]
                    res = max(res, total)
        return res

    def explore_island(self, island_id: int, r: int, c: int) -> int:
        if (
            not (0 <= r < len(self.grid)) or
            not (0 <= c < len(self.grid[0])) or
            (r, c) in self.visited or
            self.grid[r][c] == 0
        ):
            return 0
        self.visited.add((r, c))
        self.grid[r][c] = island_id
        size = 0
        size += self.explore_island(island_id, r + 1, c)
        size += self.explore_island(island_id, r - 1, c)
        size += self.explore_island(island_id, r, c + 1)
        size += self.explore_island(island_id, r, c - 1)
        return 1 + size
```
