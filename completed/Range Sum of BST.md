---
tags:
  - trees
  - easy
  - meta
link: https://leetcode.com/problems/range-sum-of-bst/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 4
last_attempt: 2025-10-11
rate:
  - ★★★★
---
#### Problem
Given the `root` node of a binary search tree and two integers `low` and `high`, return _the sum of values of all nodes with a value in the **inclusive** range_ `[low, high]`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg)

>**Input:** root = [10,5,15,3,7,null,18], low = 7, high = 15
**Output:** 32
**Explanation:** Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

#### Notes
---
Walk the tree DFS style. Keep track of a global count for the result. If the current node is within range, add it to the total. If the `low` value is less than the current node, then we can go left some more. Same goes with `high` and going right.

#### Code
---

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def traverse(root):
            if not root: return
            if low <= root.val <= high:
                self.res += root.val
            if low < root.val:
                traverse(root.left)
            if high > root.val:
                traverse(root.right)
        traverse(root)
        return self.res
```

Follow up: *"What if you can't use a global variable"*

```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(root) -> int:
            if not root: return 0
            acc = 0
            if low <= root.val <= high:
                acc += root.val
            if root.val > low:
                acc += traverse(root.left)
            if root.val < high:
                acc += traverse(root.right)
            return acc
        return traverse(root)
```