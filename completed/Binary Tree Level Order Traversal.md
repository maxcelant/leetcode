---
tags:
  - trees
  - bfs
  - hashing
pattern: Use BFS algorithm, go layer at a time using for loop of length queue. and sublist to result
rating: 1000
last_attempt: 2025-05-31
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use BFS since we need the nodes a layer at a time.
- We need to store the nodes from each layer somewhere—a hash map makes sense.

#### Code
---
First approach
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        layers = defaultdict(list)
        q = deque([(root, 1)]) # node, layer
        while q:
            node, layer = q.popleft()
            layers[layer].append(node.val)
            if node.left:
                q.append((node.left, layer + 1))
            if node.right:
                q.append((node.right, layer + 1))
        return [v for v in layers.values()] 
```

Simpler Approach w/ out dict
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                level.append(n.val)
            res.append(level)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Since we need the nodes for each layer, we can use a dict of `layer: list of nodes`.
- We simply add 1 from the previous layer when we dequeue.
- We concat the lists at the end from the dict.

#### Takeaways
---
**Where did I go wrong?**
- Forgot about the edge case of an empty tree.
**Lessons Learned?**