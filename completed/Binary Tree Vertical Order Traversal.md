---
tags:
  - medium
  - trees
  - meta
link: https://neetcode.io/problems/binary-tree-vertical-order-traversal?list=neetcode250
rating: 5
last_attempt: 2025-10-11
rate:
  - ★★★★★
---
#### Problem
You are given the `root` node of a binary tree, return the `vertical order traversal` of its nodes' values.

For the vertical order traversal, list the nodes column by column starting from the leftmost column and moving to the right.

Within each column, the nodes should be listed in the order they appear from the top of the tree to the bottom.

If two nodes are located at the same row and column, the node that appears to the left should come before the other.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/34bb5fcd-2dd2-4edc-2397-36c4bb810c00/public)

```java
Input: root = [1,2,3,4,5,6,7]

Output: [[4],[2],[1,5,6],[3],[7]]
```

#### Notes
---
If you use a dictionary and mark the root column as `0`, then you can keep track of every move left as a `-1` and every move right as a `+1`. That will allow you to group the nodes by column. To ensure that we go from left to right, you just need to sort the dictionary at the end.

#### Code
---

```python
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        q = deque([])
        if root:
            q.append((root, 0))
        while q:
            node, col = q.popleft()
            if node:
                cols[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        return [col for _, col in sorted(cols.items())]
```
