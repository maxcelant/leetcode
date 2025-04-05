---
tags:
  - graphs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that we need to start from the treasures and go out
- Shortest path is easiest to calculate using BFS with the [[Trees#Level Order Traversals]] strategy.

#### Code
---

```python
class Solution:
  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    q = deque([])
    visited = set()

    # Add all the gates to the queue
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 0: # We found a gate
          q.append((r, c))
          visited.add((r,c))
    
    dist = 0
    while q:
      # Go through a "layer" of the queue
      # Starting with the islands and going out.
      for _ in range(len(q)):
        r, c = q.popleft()
        grid[r][c] = dist
        for dx, dy in [(-1,0), (1, 0), (0, 1), (0, -1)]:
          next_r, next_c = r+dx, c+dy
          # Skip out bounds, seen and water 
          if (
            next_r < 0 or
            next_c < 0 or 
            next_r >= len(grid) or 
            next_c >= len(grid[0]) or
            (next_r, next_c) in visited or
            grid[next_r][next_c] == -1
          ):
            continue
          q.append((next_r, next_c))
          visited.add((next_r, next_c))
      dist += 1
    
    return grid
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**