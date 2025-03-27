#### Fundamentals
- When looking a tree problem, you should think _"is bottom-up or top-down a better approach here?"_
- When looking a tree problem, you should think _"is recursive or iterative better here?"_
- When looking at a recursive problem, you should think _"what is the subproblem here?"_
- Ask yourself _"What should I return to my parent?"_
	- And remember—with recursive solutions there are going to be numerous possible returns, whether it's a base case or not.
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

#### Binary Search Trees
- By default, BST's are sorted!
- Starting from the far-most left node to the right, we are in increasing order.

![[Pasted image 20250319115227.png|BST]]
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

