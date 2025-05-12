---
tags:
  - linked-list
  - easy
rating: 4
pattern: use temp node for next, swap until you reach end of list
last_attempt: 2025-05-10
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to store the next node in the linked list as a temporary value because if we lose the connection, then that's it. So before assigning `cur.next` to the previous node. Save that next node!

>![[Pasted image 20250307160647.png|400]]

#### Takeaways
---
**Where did I go wrong?**
- Need to remember to return the `prev` value at the end. That will point to the new head of the list since `cur` will be `null`.
**Lessons Learned?**
- Whiteboard it and take it a step at a time.
**Aha Moments?**
- Save the previous!