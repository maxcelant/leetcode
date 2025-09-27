---
tags:
  - linked-list
  - medium
  - dfs
rating: 5
pattern: Use a cache and recursion, create a new node and store it, if you see it again, grab it from cache. The key should be the original node
last_attempt: 2025-05-22
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that the connections kind-of create a graph like structure.
- DFS should pop in my head when I see that I need to traverse like this.

#### Code
---

```python
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        visited = {}

        def dfs(head):
            if not head:
                return None

			# If seen, return the cloned copy
            if head in visited:
                return visited[head]
           
            clone = Node(head.val, None, None)

            visited[head] = clone

            clone.next = dfs(head.next)            
            clone.random = dfs(head.random)
          
            return clone
        
        return dfs(head)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to use a `visited` dictionary because we need to retrieve the **same cloned node** when rather than creating a new one. 
- Using DFS to traverse the linked list here.
- Remember that the `clone.next` and `clone.random` need to be attained from the children nodes, so we need to call `dfs` recursively.

#### Takeaways
---
**Where did I go wrong?**
- I thought I could use a `set` instead of a dictionary, but simply knowing that a node is visited is not enough—since the `random` pointer might point to an already existing cloned node, we need to return that node so using a dictionary makes perfect sense for this.
**Lessons Learned?**
- When cloning, keep track of cloned copies in a dictionary.
- Get better at recursion!