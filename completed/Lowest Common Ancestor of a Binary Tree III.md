---
tags:
  - trees
  - medium
  - meta
link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 3
last_attempt: 2025-10-11
rate:
  - ★★★
---
#### Problem
Given two nodes of a binary tree `p` and `q`, return _their lowest common ancestor (LCA)_.

Each node will have a reference to its parent node. The definition for `Node` is below:

```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

According to the **[definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor)**: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow **a node to be a descendant of itself**)."

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

>**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
**Output:** 3
**Explanation:** The LCA of nodes 5 and 1 is 3.

#### Notes
---
**Set-based solution:** This one is very simple. You walk up from the start of `p` and add it to a visited set, then do the same thing with `q` and stop when you find the first value that already exists in the set.

**Walking-based solution:** A little trickier (but probably the one they want you to implement).
1. Find the height from `p` and `q` to the root.
2. If height of `q` is less than `p`, swap them so that `p` is always shallower (for ease).
3. Make `q` walk the difference between the two heights.
4. They are now the same height! So we can walk them simultaneously until they meet.

#### Code — Set-based Solution
---

```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while p:
            visited.add(p)
            p = p.parent
        
        while q:
            if q in visited:
                return q
            q = q.parent
```

#### Code — Tree-walking Solution
---

```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def distance(node):
            dist = 0
            while node:
                node = node.parent
                dist += 1
            return dist
        
        h1, h2 = distance(p), distance(q)
        if h1 > h2:
            p, q = q, p
        diff = abs(h1 - h2)
        while diff:
            q = q.parent
            diff -= 1
        
        while p != q:
            p = p.parent
            q = q.parent
        
        return p
```