---
tags:
  - trees
  - medium
pattern: Use level order traversal, store last node of that layer seen. Make sure to append left and then right
rating: 5
last_attempt: 2025-05-31
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that you need to do a [[plan/Trees#Level Order Traversals|level order traversal]] because you need all the nodes of a given layer.

#### Code
---

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- The most important part of this problem is the pattern where we add all the children of a layer to the queue at the same time.

```python
	for _ in range(qLen):
		node = q.popleft()
		if node:
			rightSide = node
			q.append(node.left)
			q.append(node.right)
```

- This is crucial to get down and understand.
	1. We pop all the nodes currently in the queue.
	2. For each one of those nodes, we add all their children.
- You do not make the `right_side` equal to the children—you make it equal to the node itself (aka the layer you are checking!) Otherwise you will basically skip the layer you are on.
#### Takeaways
---
**Where did I go wrong?**
- I was trying to set the children of the current node to `right_side`  instead of just setting the node itself as i traversed that layer. 
- I was setting `right_side` to `node.val` instead of `node`, which caused my `if right_side` to fail when the node value was `0`! This was a good edge case to find and remember.
**Lessons Learned?**
- If you are going to use `if X`, then make sure that `X` should just be `None` and not falsey.