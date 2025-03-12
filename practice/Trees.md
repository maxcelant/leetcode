#### Iterative Traversal Using Stack

###### Code

```python
def traversal_iterative(root: TreeNode):
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        print(f'node: {node.val}, depth: {depth}')
        if node.right: stack.append((node.right, depth + 1))
        if node.left: stack.append((node.left, depth + 1))
```

###### Insight
- We push the `right` first because we want the `left` to be on the top of the stack and to be popped first. 

###### Example