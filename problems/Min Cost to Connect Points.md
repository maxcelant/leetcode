---
tags:
  - graphs
  - union-find
  - medium
pattern: calc all distances, sort, use union find to merge points to a single graph
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
-  It wants us to connect all points exactly once.
- This seems like a possible union find problem.

#### Code
---

```python
class UF:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n + 1)
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UF(n)
        
        def manhattan_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        edges = []
        # Calculate all distances between two ndes
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan_dist(points[i], points[j])
                # We just add the distance and the two points
                edges.append((dist, i, j))
        
        # Sort to make sure we have the mins first in the list
        edges.sort()
        res = 0
        for dist, u, v in edges:
            # I only want to union IF they are not in the same tree already
            if uf.union(u, v):
                res += dist
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to loop through all the points and find the distance between each point, then we use the sort to find the mins of each distance.
- We use union find here to add the nodes together.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**