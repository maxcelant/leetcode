---
tags:
  - linked-list
  - medium
insight: Use dummy, get value and store carry for next nodes.
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that we need to create a new list (aka create a `ListNode` with `dummy`).
- Realize that we need to use a pointer for each linked list.
- Understand basic math with carries and values.

#### Code
---

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, val = divmod(v1+v2+carry, 10)
            cur = ListNode(val)
            head.next = cur
            head = cur

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We use a `dummy` node to hold the head. We create a `prev` and continuously add nodes to the end of the list.
- We need to be extra careful and handle the case where `l1` or `l2` is potentially `None`.

#### Takeaways
---
**Where did I go wrong?**
- I accidentally flipped the carry and val for `divmod`. Note to self: `carry` is first!

**Lessons Learned?**
- Clever ways to handle null nodes.