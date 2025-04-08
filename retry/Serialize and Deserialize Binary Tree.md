---
tags:
  - trees
  - dfs
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- For serialization: If we run through the tree using DFS and collect the nodes `Inorder` (Root->Left->Right), then we will be able to reconstruct the tree using `Inorder`
- For deserialization: We can also use DFS and recreate the tree if we add a node one at a time.
#### Code
---

```python
class Codec:

    def serialize(self, root):
        s = []
        def dfs(root):
            if not root:
                s.append('N')
                return

            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(s)
        

    def deserialize(self, data):
        i = 0
        s = data.split(",")
        
        def dfs():
            nonlocal i 
            if s[i] == 'N':
                i += 1
                return 

            node = TreeNode(int(s[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs() 
```

#### Insight  
---
_"What are the important aspects of the solution?"_
**For Serialization**
- We need to keep track of the null nodes, so that we can recreate the tree correctly. So storing them with `N` covers that.
**For Deserialization**
- We need to use a `i` counter to traverse the list recursively and keep track of where we are. This allows us to skip null nodes.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
- 