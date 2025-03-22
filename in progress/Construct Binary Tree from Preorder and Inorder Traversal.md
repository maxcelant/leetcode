---
tags:
  - trees
  - retry
  - dfs
  - recursion
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- **`Preorder` (Root → Left → Right)**: The first element in `preorder` is always the root.
- **`Inorder` (Left → Root → Right)**: The root divides the `inorder` list into left and right subtrees.
- Since `Inorder` tells us how many nodes are in the left and right, we can use that index position to determine how many nodes belong to the left and right subtree in the `Preorder` list.

#### Code
---

```python


```

#### Insight  
---
_"What are the important aspects of the solution?"_
- The first value in our `preorder` list is the root of the tree! This is great because it tell us how we need to split up the left and right subtrees recursively.
- We need to find that index of the root in the `inorder` list, we call that `mid`. 
- The left subtree in the `inorder` list will be **all the values before `mid`** and right subtree will be **all the values after `mid`**.
- Since `preorder` lists nodes in **Root → Left → Right** order:
- The next `mid` elements in `preorder` must be the **left subtree** (they appear first).
- The remaining elements after that are the **right subtree**.

![[Pasted image 20250322121511.png|Left and right subtrees explained]]

**Example**
- In the image `mid = 4`, so we know that there are `3` nodes in the left subtree and `3` nodes in the right subtree.
- Since the `Preorder` list is created `root->left->right`, we know that the next `3` nodes will be in the left subtree and the remaining will be in the right subtree!

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
- The root will always be `preorder[0]`
- I now understand that the next N nodes in the preorder list are the nodes in the left subtree, and the remaining are the right subtree.