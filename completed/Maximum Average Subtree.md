---
tags:
  - trees
  - medium
  - meta
link: https://leetcode.com/problems/maximum-average-subtree/description/
last_attempt: 2025-10-23
rate:
  - ★★★★★
---
#### Variants
- [[Count Nodes Equal to Average Subtree]]

#### Problem
Given the `root` of a binary tree, return _the maximum **average** value of a **subtree** of that tree_. Answers within `10-5` of the actual answer will be accepted.

A **subtree** of a tree is any node of that tree plus all its descendants.

The **average** value of a tree is the sum of its values, divided by the number of nodes.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/09/1308_example_1.png)

**Input:** root = [5,6,1]
**Output:** 6.00000
**Explanation:** 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.

#### Notes
Just make sure you add the `root.val` to the sum and not just add 1. 

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        def traverse(root: Optional[TreeNode]) -> tuple[int,int]:
            if not root:
                return (0,0)
            
            l_sum, l_count = traverse(root.left)
            r_sum, r_count = traverse(root.right)
            t_sum = l_sum + r_sum + root.val
            t_count = l_count + r_count + 1
            self.res = max(self.res, (t_sum / t_count))
            return t_sum, t_count
        traverse(root)
        return self.res
```
