---
tags:
  - linked-list
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that we need the length of the list and need the count from the end—hence we should use fast/slow pointers.
#### Code
---

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy.next

		# Move fast pointer N spaces ahead
        while n > 0:
            fast = fast.next
            n -= 1

		# Move both pointers a space at a time til we reach the end
		# This ensures we are N spaces from the end.
        while fast:
            fast = fast.next
            slow = slow.next
        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        
        return dummy.next
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Since we need the n-th index from the end, we need to make sure that the fast pointer is N nodes **in front of** the slow one
- Using a `dummy` node and pointing it to the head makes our life easier. Because we can have our slow pointer starting from there instead of the `head`.
	- This is especially useful when we need to modify the `head` node.

#### Takeaways
---
**Where did I go wrong?**
- 
**Lessons Learned?**
- Use a dummy node to simplify things.
- We can separate the fast and slow pointers by N spaces to find the node that is N from the end.