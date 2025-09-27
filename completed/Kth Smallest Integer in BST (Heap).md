---
tags:
  - trees
  - heaps
  - dfs
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We could add the values one-by-one into a heap then pop `k` nodes from the heap.

#### Code
---

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        def dfs(root):
            if not root:
                return
            heapq.heappush(h, root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        res = None
        while k > 0:
            res = heapq.heappop(h)
            k -= 1
        
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We are using a min-heap to maintain the nodes in a sorted order.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**