---
tags:
  - linked-list
  - medium
  - meta
link: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-02
rate:
  - ★
---
#### Variants
- [[Linked List Cycle]]

#### Problem
Imagine you are given a circular linked list of sorted in increasing order. Add a value to the linked list such that it retains it's sorted order.

#### Notes
Use a two pointers approach. There are three main edge cases:
1. **Easy Case**: node fits between two existing nodes, nice, easy—just slot it in.
2. **Tail/Head Case:** If we hit the tail (where the next node is smaller than previous), then we need to check if the new value is larger than `prev` or smaller than `cur`.
3. **Loop Case**: If all the values are the same or something and we've looped back to the start, then we simply add the node at that location.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head: 
            n = Node(insertVal)
            n.next = n
            return n
        
        node = Node(insertVal)
        prev, cur = head, head.next
        while True:
            # Case 1: Node fits between two existing nodes
            if prev.val <= insertVal <= cur.val:
                prev.next = node
                node.next = cur
                break
            # Case 2: It's a tail/head node.
            # Bigger than tail or less than head
            if prev.val > cur.val:
                if insertVal >= prev.val:
                    prev.next = node
                    node.next = cur
                    break
                if insertVal <= cur.val:
                    prev.next = node
                    node.next = cur
                    break
            prev = cur
            cur = cur.next
            # Case 3: We've gone through the whole
            # loop and haven't found a place to put it
            # which means the values are all identical
            if prev == head:
                prev.next = node
                node.next = cur
                break
        
        return head
```
