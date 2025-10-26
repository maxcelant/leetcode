---
tags:
  - graphs
  - medium
  - meta
link: https://leetcode.com/problems/clone-graph/submissions/1808121854/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-25
rate:
  - ★★★★
---
#### Variants
- [[Copy Linked List with Random Pointer]]

#### Problem
Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_\(graph_theory\)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```
#### Notes
The idea is similar to other clone problems. We use a map to return the cloned structure and we traverse until we have seen the whole thing.

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def traverse(node):
            if node in clones:
                return clones[node]
            
            clone = Node(node.val)
            clones[node] = clone
            for neigh in node.neighbors:
                clone.neighbors.append(traverse(neigh))
            return clone
            
        return traverse(node) if node else None
```


#### Follow Up: *"BFS Solution"*

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clones = {}
        q = deque([node])
        clones[node] = Node(node.val)
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    q.append(n)
                clones[cur].neighbors.append(clones[n])
        return clones[node]
```