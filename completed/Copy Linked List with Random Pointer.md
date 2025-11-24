---
tags:
  - linked-list
  - medium
  - dfs
  - meta
  - nvidia
last_attempt: 2025-11-23
rate:
  - ★★★★★
link: https://leetcode.com/problems/copy-list-with-random-pointer/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
---
#### Problem
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

>val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

#### Notes
---
As we traverse, we store seen nodes in `copies` so that we don't do repeated (or cyclical) work. It's important we store the node itself as the key and NOT the value, because the value can be repeated by more than one node.

We simply recursively call the function on the `next` and `random` pointer to get those values. It's a bottom-up approach. We solve the children before the parent.

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        def traverse(node):
            if not node:
                return None
            if node in copies:
                return copies[node]
            
            new_node = Node(node.val)
            copies[node] = new_node
            new_node.random = traverse(node.random)
            new_node.next = traverse(node.next)
            return new_node
        return traverse(head)
```
