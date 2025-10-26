---
tags:
  - graphs
  - trees
  - medium
  - meta
link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★★★★
---
#### Variants
- [[Amount of Time for Binary Tree to Be Infected]]

#### Problem
Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return _an array of the values of all nodes that have a distance_ `k` _from the target node._

You can return the answer in **any order**.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
**Output:** [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

#### Notes
Turn the tree into an graph. Now we can traverse like normal to find all the nodes that are K distance away from the target.

Make sure that the graph is _undirected_ and make sure to use a visited set in the traversal to avoid running into the same nodes twice and accidentally adding the target node to the final result.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        # Create an graph using adjacency lists for each node
        def create_graph(root: TreeNode):
            q = deque([root])
            while q:
                node = q.popleft()
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    q.append(node.right)
        
        create_graph(root)

        visited = set()
        res = []
        # Add all the nodes that are K distance away from the target
        def traverse(node, depth):
            if node in visited:
                return
            if depth > k:
                return
            if depth == k:
                res.append(node)
            visited.add(node)
            for n in graph[node]:
                traverse(n, depth + 1)
        
        traverse(target.val, 0)
        return res
```


#### Follow Up: *""*

```python

```