---
tags:
  - trees
  - medium
  - meta
link: https://leetcode.com/problems/diameter-of-n-ary-tree/description/
last_attempt: 2025-10-22
rate:
  - ★★★★★
---
#### Variants
- [[Diameter of a Binary Tree]]

#### Problem
Given a `root` of an `N-ary tree`, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the **longest** path between any two nodes in the tree. This path may or may not pass through the root.

(_Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)_

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/07/19/sample_2_1897.png)

>**Input:** root = [1,null,3,2,4,null,5,6]
**Output:** 3
**Explanation:** Diameter is shown in red color.

#### Notes
We traverse and keep track of the top 2 branches and then return the top branch + 1. 

If we find a deeper branch, we basically "shift" the values such that h1 becomes h2 and the new deepest becomes h1.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N) because of the function call stack.

```python
class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        def traverse(root) -> int:
            if not root:
                return 0

            h1, h2 = 0, 0
            for child in root.children:
                h = traverse(child)
                if h > h1:
                    h1, h2 = h, h1
                elif h > h2:
                    h2 = h
            self.res = max(self.res, h1 + h2)
            return h1 + 1
        traverse(root)
        return self.res
```


#### Follow Up: *""*

```python

```