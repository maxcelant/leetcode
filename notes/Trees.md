#### Fundamentals
- When looking a tree problem, you should think _"is bottom-up or top-down a better approach here?"_
- When looking a tree problem, you should think _"is recursive or iterative better here?"_
- Bottom-up and top-down are strategies that can both be accomplished through recursion and iteration.
- If the result does not necessarily get computed from the final response, this is a great indicator to use a closure value.
#### About Top-down
The idea is that when you need the parent data before the children, then a bottom-up strategy is the way to go.

```python "title:Top-down approach"
def top_down_dfs(node, depth):
    if not node:
        return
    
    print(f'Node: {node.val}, Depth: {depth}')  # Process parent first
    top_down_dfs(node.left, depth + 1)
    top_down_dfs(node.right, depth + 1)
```

Use top-down when you **want to pass data downwards.**

Example: Finding node depth
#### About Bottom-up
The idea is that when you need the children of something before the parent, then a bottom-up strategy is the way to go.

```python title:"Bottom-up approach"
def bottom_up_height(node):
    if not node:
        return 0
    
    left_height = bottom_up_height(node.left)
    right_height = bottom_up_height(node.right)
    return max(left_height, right_height) + 1  # Aggregate from children
```

Use bottom-up when you **want to compute results in children first, then combine at the parent.**

Example: Computing tree height

#### Depth and Height
- The `depth` is the how far down a node is from the root.
- The `height` is the longest path from that node down to the bottom.
- The `height` of the root is also the max `depth` in the tree.

![[Pasted image 20250312204921.png|Depth and Height]]

#### Level Order Traversals

```python
    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
```

- While a standard BFS will traverse all nodes in a tree, it does **not** do all the nodes in a layer as a single step.
- That's what this level order traversal accomplishes—it allows you to iterate through **all** nodes in a layer before moving on to the next one.
- This is important when you need to look at all the nodes in a layer and get some value (like [[Binary Tree Right Side View]]).