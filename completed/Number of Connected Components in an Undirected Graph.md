---
tags:
  - graphs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to find all the disjoint subgraphs in a graph.
- Fully explore a graph with DFS, mark it, and move on. 
- Keep a count of all subgraphs explored.

#### Code
---

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        # Keep count of seen sets in graph
        count = 0
        # Fully explore this subgraph
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                dfs(neigh, node)

        for node in range(n):
	        # We only explore the graph if it's a new one
            if node in visited:
                continue
            dfs(node, -1)
            count += 1
        return count
```

#### Insight  
---
_"What are the important aspects of the solution?"_
In order to find all the sets in the graph where they aren't connected (disjoint), we basically need to fully explore a graph before moving on to the next one (if there is one) and if there is one, we increment the `count` by 1.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**