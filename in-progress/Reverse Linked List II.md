---
tags:
link:
last_attempt:
rate:
---
#### Variants

#### Problem

#### Notes

There are lots of edge cases to think about in this problem.

1. Traverse the linked list using `prev` and `cur` as normal until we reach the `left` barrier.
2. Set the `con` at the `prev` position and `tail` at the `cur` position.
3. Reverse until we reach _after_ the `right`-th node.
4. Update the pointers so that `con.next = prev` and `tail.next = cur`.
![[Pasted image 20251123233109.png]]

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur = None, head
        i = 1
        # Traverse until we reach left barrier
        while i < left:
            prev = cur
            cur = cur.next
            i += 1
        
        # Use pointers to attach at the end
        con, tail = prev, cur
        # Reverse nodes until we reach right barrier
        while i <= right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1
        
        # Attach the new nodes to the correct outer nodes
        # If the left pointer is the first node, then con will be null
        # So to avoid any runtime errors, make prev the new head instead
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

```
