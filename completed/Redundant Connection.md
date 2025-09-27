---
tags: 
pattern:
---
#### Video Breakdown
![[unionfind.mov]]

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that you can find redundant connections using the union find algorithm.
- Just need to find where the parent of each set is the same! That's our edge that caused the cycle.

#### Code
---

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = list(range(n))
        rank = [0] * (n)

        def find(x):
            node = x
            while node != parent[node]:
                node = parent[node]

			# (optimization not really necessary)
            while x != node:
                temp = parent[x]
                parent[x] = node
                x = temp

            return node

        def union(u, v):
            root_u, root_v = find(u), find(v)

			# Parents are the same! cycle found
            if root_u == root_v:
                return False

            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return True


        for u, v in edges:
            if not union(u,v):
                return [u, v]

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Really you just need to know the union find algorithm, if you do, this is an easy problem.
- Pay close attention to the optimization/compression portion of the `find`

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
- Union find algorithm