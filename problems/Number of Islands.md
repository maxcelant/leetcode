---
tags:
  - graphs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use dfs to "traverse" an entire island, keeping track of the visited cells.
- Once we fully dfs, we just move to the next cell and skip those that we've already visited and also skip "0" ones.
- When we reach a `(r,c)` that's unvisited, we can increment the island count by 1.
- We should check all four directions, just to cover all cases.

#### Code
---

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        visited = set() # of (r, c) tuples

        def dfs(r: int, c: int):
            # base case
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == '0':
                return
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if (r+dx, c+dy) in visited:
                    continue
                visited.add((r+dx, c+dy))
                dfs(r+dx, c+dy)
                
		# dfs all four directions
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '0':
                    continue
                if (r, c) in visited:
                    continue
                dfs(r, c)
                res += 1
        
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We should ignore visited and `'0'` cells as early as we can in our search—so in our double for loop.
- By using DFS we can map out the entire island in one go.
- `dx, dy` is for all four cardinal directions.

#### Takeaways
---
**Where did I go wrong?**
- The base case condition didn't have the `grid[r][c] == 0` in it, so it caused an infinite error bug.
**Lessons Learned?**
- Pay close attention to your base cases.