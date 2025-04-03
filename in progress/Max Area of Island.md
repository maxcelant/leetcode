---
tags:
  - graphs
  - dfs
  - medium
  - bottom-up
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use a bottom-up dfs approach to calculate the area.

#### Code
---

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        res = 0
        visited = set() # of (r,c)
        def dfs(r: int, c: int):
            # base case
            if r < 0 or r == N or c < 0 or c == M or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return (1 + 
                dfs(r + 1, c) + 
                dfs(r, c + 1) + 
                dfs(r - 1, c) +
                dfs(r, c - 1)
            )
            
        for r in range(N):
            for c in range(M):
                if (r,c) in visited or grid[r][c] == 0:
                    continue
                res = max(res, dfs(r, c))
        
        return res 
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- By using a bottom up approach, we ensure that we get the area starting from the edges and coming in.
- We can skip the visited and `0` cells to make this more optimized.

#### Takeaways
---
**Where did I go wrong?**
- I was trying to get the max or all the directions but instead I should have been summing them all up!
**Lessons Learned?**