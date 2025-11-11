---
tags:
  - medium
  - meta
  - trees
last_attempt: 2025-11-10
rate:
  - ★★★★
---
#### Variants


#### Problem
The **boundary** of a binary tree is the concatenation of the **root**, the **left boundary**, the **leaves** ordered from left-to-right, and the **reverse order** of the **right boundary**.

The **left boundary** is the set of nodes defined by the following:

- The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is **empty**.
- If a node is in the left boundary and has a left child, then the left child is in the left boundary.
- If a node is in the left boundary, has **no** left child, but has a right child, then the right child is in the left boundary.
- The leftmost leaf is **not** in the left boundary.

The **right boundary** is similar to the **left boundary**, except it is the right side of the root's right subtree. Again, the leaf is **not** part of the **right boundary**, and the **right boundary** is empty if the root does not have a right child.

The **leaves** are nodes that do not have any children. For this problem, the root is **not** a leaf.

Given the `root` of a binary tree, return _the values of its **boundary**_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/11/boundary1.jpg)

**Input:** root = [1,null,2,3,4]
**Output:** [1,3,4,2]
**Explanation:**
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

#### Notes
We break this up to three parts:
1. Traverse left border using pre-order traversal.
2. Traverse all leaf nodes using any order, it doesn't matter, you just need to check if it's a leaf node.
3. Traverse right border using post-order traversal.

There are some caveats:

For the left and right traversals, have to make sure that the node you are looking is not a leaf node aka it needs to have at least one child.

When traversing, for instance if the left side doesn't have a left child, then the right child becomes the border. Same goes for right side.

![[Screenshot 2025-11-10 at 10.42.16 PM.png]]

#### Code
**Time Complexity**: O(N + H), N nodes on the leaf traversal and H on the left and right
**Space Complexity**: O(N)

```python
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]
        def traverse_left(root):
            if not root:
                return
            if root.left:
                res.append(root.val)
                traverse_left(root.left)
            elif root.right:
                res.append(root.val)
                traverse_left(root.right)
            
        def traverse_right(root):
            if not root:
                return
            if root.right:
                traverse_left(root.right)
                res.append(root.val)
            elif root.left:
                res.append(root.val)
                traverse_left(root.left)

        def traverse_leaves(root):
            if not root:
                return
            if not root.right and not root.left:
                res.append(root.val)
            traverse_leaves(root.left)
            traverse_leaves(root.right)
        
        if root.left:
            traverse_left(root.left)
        if root.left or root.right:
            traverse_leaves(root)
        if root.right:
            traverse_right(root.right)
        return res
```
