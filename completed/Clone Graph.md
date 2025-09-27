---
tags:
  - graphs
  - medium
  - retry
pattern:
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that similar to the other "construct" problems, we need to have a dictionary easily get the nodes we've already seen and return the clones.
- Use DFS with a bottom-up approach to return the clone, looping through all of it's children.

#### Code
---

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen_nodes = {} # Keep track of the nodes we've already cloned
        def dfs(node):
            if node in seen_nodes:
                return seen_nodes[node] # Return the clones
            
            clone = Node(node.val)
            seen_nodes[node] = clone # Make old -> new pairing
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
    
            return clone
        
        return dfs(node) if node else None
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Using the `seen_nodes` dictionary is probably the most important takeaway from this problem.

#### Takeaways
---
**Where did I go wrong?**
Since the graph data structure is using a neighbor list, there is no need to say `if not node`, since it will only loop through the list. So instead, I needed to use a dictionary to keep track of the "seen nodes", so that I can easily just return the clone when I reach that same node again! 
**Lessons Learned?**
Use this copy dictionary to keep track of the copies, almost like a visited set.