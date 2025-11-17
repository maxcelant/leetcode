---
tags:
  - trees
  - medium
  - meta
link: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-16
rate:
  - ★★★★★
---

#### Problem
You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return _the total sum of all root-to-leaf numbers_. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

>**Input:** root = [1,2,3]
**Output:** 25
**Explanation:**
The root-to-leaf path `1->2` represents the number `12`.
The root-to-leaf path `1->3` represents the number `13`.
Therefore, sum = 12 + 13 = `25`.

#### Notes
---
We stringify the accumulation so that we can simply add the next digit in the number. Note: doing the accumulation using an int works as well if you follow [[Digit Accumulation]].

When we reach a leaf node, we add that accumulation to the final result.

>[!important]
>We can't do the accumulation in the `if not root` because that would mean it would occur twice for every leaf node!
#### Code
---
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def traverse(root, acc):
            acc += str(root.val)
            if not root.left and not root.right:
                self.res += int(acc)
            if root.left:
                traverse(root.left, acc)
            if root.right:
                traverse(root.right, acc)
        traverse(root, '')
        return self.res
```


#### Follow Up: *"Can you do it without using the string?"*

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def traverse(root, acc):
            acc = acc * 10 + int(root.val)
            if not root.left and not root.right:
                self.res += acc
            if root.left:
                traverse(root.left, acc)
            if root.right:
                traverse(root.right, acc)
        traverse(root, 0)
        return self.re
```