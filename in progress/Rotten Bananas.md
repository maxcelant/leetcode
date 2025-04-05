---
tags:
  - graphs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that we need to do a BFS, and keep track of the time passed for each layer.
- We should only continue if there are valid paths.

#### Code
---

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        Q = deque([])
        fresh = 0 # Keep track of fresh bananas remaining

        # Add all the rotten bananas to queue
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 2:
                    Q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        def in_bounds(r, c):
            if not (0 <= r < N and 0 <= c < M):
                return False
            if grid[r][c] == 2 or grid[r][c] == 0:
                return False
            return True
        
        ticks = 0
        # Either we've reached the end of the queue or all bananas are rotten
        while Q and fresh > 0:
            for _ in range(len(Q)):
                r, c = Q.popleft()
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr, nc = r + dx, c + dy
                    if in_bounds(nr, nc):
                        grid[nr][nc] = 2 # Make banana rotten
                        fresh -= 1
                        Q.append((nr, nc))
            ticks += 1
        
        return ticks if fresh == 0 else -1 
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We only want to increase a tick IF there are still fresh bananas left, otherwise we should just stop.
- If we end and there are still fresh bananas, then we need to return `-1` because we couldn't reach them
- We need to count the number of fresh bananas right away.

#### Takeaways
---
**Where did I go wrong?**
I didn't account for the fresh bananas. I needed to keep track of how many there were.

**Lessons Learned?**
