---
tags:
  - graphs
  - bfs
  - shortest-path
pattern:
---
#### Video Breakdown
![[cheaptest-flights-with-k-stops.mov]]

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Shortest path algorithm -> accumulate cost as we go
- BFS -> use queue
- Priority Queue / min heap approach -> use `heapq`
- Directed graph -> adjacency list creation

#### Code
---

```python

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        
        pq = [(0, src, k+1)]
        while pq:
            w1, n1, stops = heapq.heappop(pq)
            if n1 == dst:
                return w1
            if stops > 0:
                for n2, w2 in adj[n1]:
                    heapq.heappush(pq, (w1+w2, n2, stops - 1))
        return -1
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We use a min heap to always pop the cheapest node,
- We accumulate the "cost" of a node as we add it to the heap.
- We decrement the stops as we go, because we can only go K stops (at most).
- We use adjacency list.

#### Takeaways
---
**Lessons Learned?**