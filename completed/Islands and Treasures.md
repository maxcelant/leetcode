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
		N, M = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # Find all the treasures and add them to the queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        def is_valid(r, c):
            if not (0 <= r < N and 0 <= c < M):
                return False
            if (r, c) in visited or grid[r][c] == -1:
                return False
            return True

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if is_valid(r+dx, c+dy):
                        visited.add((r+dx, c+dy))
                        q.append((r+dx, c+dy))
            dist += 1 # Add one to the distance for every layer
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need a `visited` set here because we would accidentally override the shortest path of a cell if we go over it again.
- We are starting our BFS simultaneously from ALL the treasure chests and going out. That's why we add them all to the queue before anything.
	- This will ensure shortest path for every cell.
- Making sure we do `for _ in range(len(q)):` ensures we go a layer at a time.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**