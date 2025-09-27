---
tags:
  - graphs
  - dfs
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- A valid tree is one without cycles and is not disjoint (two or more groups of nodes).
- Create an undirected graph adjacency list `a: [b], b: [a]`
- If the visited is equal to the nodes, then we know we **don't have a disjoint set**.

#### Code
---

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create adjacency list
        # Both side bc its undirected     
        adj = collections.defaultdict(list)
        for (a, b) in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node, parent):
	        # We have found a cycle!
            if node in visited:
                return True
           
            visited.add(node)
            for neigh in adj[node]:
	            # Skip the immediate parent, this doesn't count as a cycle
                if parent == neigh:
                    continue
                if dfs(neigh, node):
                    return True
            return False
        
        found_cycle = dfs(0, -1)
        # We also make sure we have visited all the nodes
        # aka no disjoint sets in graph
        return not found_cycle and len(visited) == n

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Since it's an undirected graph, the adjacency list for two nodes needs to have each others nodes!
- In undirected graphs, going back to a nodes parent **does not count as a cycle**.

#### Takeaways
---
**Where did I go wrong?**
- Forgot about disjoint sets
**Lessons Learned?**
- In undirected graphs, we add each other's nodes to the adjacency lists.
- We can use the visited to see if we have a disjoint graph.
- We skip on parents when checking neighbors, since that doesn't count as a cycle.