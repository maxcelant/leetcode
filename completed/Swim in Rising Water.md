---
tags:
  - graphs
  - hard
pattern: Use shortest path algorithm, priority queue + bfs, return max weight seen along the path
link: https://neetcode.io/problems/swim-in-rising-water
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We are finding the "shortest path", by always picking the next smallest cell.

#### Code
---

```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # Create a min heap
        pq = [(grid[0][0], 0, 0)] # (weight, r, c) 
        visited = set()
        res = 0
        # Traverse BFS
        while pq:
            # Pop the smallest node seen so far
            w, r, c = heapq.heappop(pq)
            # Skip if seen
            if (r, c) in visited:
                continue
            visited.add((r, c))
            res = max(res, w)
            # If we reach the bottom right node, then we stop!
            if (r, c) == (ROWS - 1, COLS - 1): 
                break
            # Look at the neighbors of this node
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r+dx, c+dy
                # Check for corner
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                if (nr, nc) in visited: 
                    continue
                # Add to the min heap
                heapq.heappush(pq, (grid[nr][nc], nr, nc))
        return res

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We use a priority queue, using the weight of the cell as the priority metric.
- We BFS and always pick the lowest weight of the neighbors to be popped (by pq).
- The result is just the max weight seen along the path from start to finish (bottom left corner).

#### Takeaways
---
**Lessons Learned?**