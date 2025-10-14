---
tags:
  - trees
  - medium
  - meta
rating: 5
last_attempt: 2025-10-12
link: https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rate:
  - ★★★★★
---
#### Problem
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return _the values of the nodes you can see ordered from top to bottom_.

**Example 1:**
```
**Input:** root = [1,2,3,null,5,null,4]
**Output:** [1,3,4]
```

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

#### Notes
---
Use BFS with a level order traversal so that you are looping through all the nodes on a particular level before moving on. Store the last one you see on that level.

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(D) where D is the diameter of the tree since each level can have at most one node.

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([])
        if root:
            q.append(root)
        while q:
            rightmost = None
            for _ in range(len(q)):
                node = q.popleft()
                rightmost = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(rightmost)
        return res
```


#### Follow Up: *"What if we wanted left side view?"*

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([])
        if root:
            q.append(root)
        while q:
            leftmost = None
            for _ in range(len(q)):
                node = q.popleft()
				if not leftmost:
	                leftmost = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(leftmost)
        return res
```