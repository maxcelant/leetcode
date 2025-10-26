---
tags:
  - trees
  - recursion
  - dfs
  - bottom-up
  - easy
  - meta
link: https://neetcode.io/problems/binary-tree-diameter
last attempted: 2025-10-22
rate:
  - ★★★★★
last_attempt: 2025-10-21
---
#### Variants


#### Problem


#### Notes

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def traverse(root) -> int:
            if not root:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1
        traverse(root)
        return self.res
```


#### Follow Up: *""*

```python

```