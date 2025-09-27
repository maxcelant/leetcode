---
tags:
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- I need to use DFS, but I only need to run the traversal from the edges, and see which cells connect to them that meet the condition,

#### Code
---

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dx, c+dy
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited) 
        
        for c in range(COLS):
            # Top row
            dfs(0, c, pac)
            # Bottom row
            dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            # left column
            dfs(r, 0, pac)
            # right column
            dfs(r, COLS - 1, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return re
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Perform DFS starting from the top and bottom row, 
    - on the top row, keep track of the cells that reach the `pacific`
      - `row = 0`, `col = 0..M`
    - on bottom, keep track of the cells that reach the `atlantic`.
      - `row = N`, `col = 0..M`
- We can only visit a cell if it's **GREATER than or EQUAL** to the current cell, 
  so we will need some way of capturing the prev cell
- Perform DFS on left and right-most column.
  - on left col, keep track of the cells that reach the pacific
    - `row = 0..N`, `col = 0`
  - on right col, keep track of the cells that reach the atlantic
    - `row = 0..N`, `col = M`
- Keep track of the visited nodes respectively as `pac` and `atl` for the oceans.
#### Takeaways
---
**Where did I go wrong?**
- I didn't think about the fact that the edges of the graph being the important parts.
**Lessons Learned?**