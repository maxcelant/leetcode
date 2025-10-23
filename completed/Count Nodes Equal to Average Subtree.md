---
tags:
  - trees
  - meta
  - medium
link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★★★★
---
#### Variants


#### Problem


#### Notes
Since the current nodes value relies on it's children, we need to take a bottom-up approach and propagate up the count and sum from the children to parent.

The average subtree value _includes the current node_ in both the total sum and total node count.

We send the information up to the parent with a tuple of `(sum, node_count)`.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def traverse(root: TreeNode) -> tuple[int, int]:
            if not root:
                return (0, 0)
            
            # Propagate up the sum and node count as a tuple (sum, count)
            left_sum, left_count = traverse(root.left)
            right_sum, right_count = traverse(root.right)
            total_sum = left_sum + right_sum
            total_count = left_count + right_count
            if (total_sum + root.val) // (total_count + 1) == root.val:
                self.res += 1
            
            return (total_sum + root.val, total_count + 1)
        traverse(root)
        return self.res
```


#### Follow Up: *""*

```python

```