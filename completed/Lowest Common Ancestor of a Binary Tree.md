---
tags:
  - meta
  - medium
  - trees
link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 3
last_attempt: 2025-10-11
rate:
  - ★★★
---
#### Problem
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

>**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**Output:** 3
**Explanation:** The LCA of nodes 5 and 1 is 3.

#### Notes
---
Plain binary trees don't have any order, so going left or right to decrease/increase value won't work. We need to rely on plain old searching.

The idea is to mark a branch as `True` as soon as we find one of the markers (`p` or `q`) and then propagate that value up the tree. We do this in both left and right branches so that when both sides return `True`, we know we found the LCA.

**Important caveat:** The current node _can be p or q_ and that will count as the LCA if the other pointer is it's child.


#### Code
---

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def traverse(root) -> bool:
            if not root:
                return False
            left = traverse(root.left)
            right = traverse(root.right)
            # See if current node is p or q 
		    cur = root is q or root is p
            # This is important! The LCS can be q or p!
            # As long as two of these are true, then we've found the LCS
			# This will only be true for the LCA
            if cur + left + right >= 2:
                self.res = root
            # Propagate up True if one of these has been found otherwise 
            # it'll be False for deadends or dead branches
            return cur or left or right
        traverse(root)
        return self.res
```

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def traverse(root) -> list[bool]:
            if not root:
                return [False, False]
            
            left = traverse(root.left)
            right = traverse(root.right)
            combined = [left[0] or right[0], left[1] or right[1]]
            if root is p:
                combined[0] = True
            if root is q:
                combined[1] = True
            if combined == [True, True] and self.res is None:
                self.res = root
            return combined
        traverse(root)
        return self.res
```

Follow Up: *"Can you solve it iteratively?"*

The approach is that we use a stack and traverse down the tree. As we go, we keep track of a `parent` dict which maps a node to its parent (key: node, val: parent).

This will allow us to basically start from p and walk up its tree, add those to a set and then let us do a similar thing for q until we find a match

```python
def LCA(root, p, q) -> int:
  stack = [root]
  parent = { root: None }
  while p not in parent or q not in parent:
    node = stack.pop()
    if node.left:
      parent[node.left] = node
      stack.append(node.left)
    if node.right:
      parent[node.right] = node
      stack.append(node.right)
  
  ancestors = set()
  while p:
    ancestors.add(p)
    p = parent[p]
  
  while q not in ancestors:
    q = parent[q]
  return q
```