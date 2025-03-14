#### Traversal Using Stack (Iterative) | Top-down approach

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

#### Max Depth (Recursive) | Top-down approach

###### Code
```python
def max_depth(root: TreeNode):
    def dfs(root: TreeNode, depth: int):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)
```

These are equivalent

```python
def max_depth(root: TreeNode):
    def dfs(root: TreeNode, depth: int):
        if not root:
            return depth
        left = dfs(root.left, depth + 1)
        right = dfs(root.right, depth + 1)
        return max(left, right)

    return dfs(root, 0)
```
###### Insight
- Each subtree will continuously call and add 1 to the depth, as we propagate back up, the largest one will win.

#### Total Value Accumulation (Recursive) | Bottom-up approach

###### Code
```python
def total_value(root: TreeNode):
    def dfs(root: TreeNode):
        if not root:
            return 0
        return root.val + dfs(root.left) + dfs(root.right)
        
    return dfs(root)
```
###### Insight
- We accumulate the current value with those of each subtree.

#### Total Node Count Using Closure (Recursive) | Top-down approach

###### Code
```python
def get_total_count(root: TreeNode):
    count = 0
    def dfs(root: TreeNode):
        nonlocal count
        if not root:
            return 
        
        print(f'node: {root.val}, count: {count}')
        count += 1
        dfs(root.left)
        dfs(root.right)
        return count

    return dfs(root)
```
###### Insight
- Uses an outside variable and then reference it using `nonlocal`.

#### 