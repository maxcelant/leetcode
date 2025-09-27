---
tags:
  - graphs
  - bfs
  - medium
pattern: Use bfs and a min heap to always pop the smallest path, add weight from parent, return max
---
#### Video Breakdown
![[network-delay-time.mov]]

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to use some sort of shortest path algorithm.
- BFS is a good approach.

#### Code
---

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        visited = set()
        heap = [(0, k)] # (weight, node)
        res = 0

        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, weight)
            for n2, w2 in adj[node]:
                if n2 in visited:
                    continue
                heapq.heappush(heap, (weight+w2, n2))
        
        return res if len(visited) == n else -1
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- The min heap needs to have the weight FIRST, since we sort by that.
- There's a chance we may have a disjoint graph, so checking to make sure all the nodes are visited at the end stops us from this edge case.
- The result is going to be the max weight found from all the visited nodes.

#### Takeaways
---
**Where did I go wrong?**
- Didn't realize that I needed to add a check `if node in visited...` . This is important because nodes can queue the same neighbor multiple times _before_ that node ever gets visited, so we need to make sure that we only check that node once.
- Be careful about variable shadowing.

**Lessons Learned?**