---
tags:
  - linked-list
  - easy
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to create a new list.
- They are sorted, so `list1` and `list2` values should be compared to see which one should be added next.

#### Code
---

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return head.next
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Make sure to create a `ListNode()` at the beginning for this new linked list.
- Make sure to keep track of the beginning of the list by using the `head` node. 
- Set the `next` value of `cur` to the smaller list node.
- Any remaining nodes should be captured at the end.

#### Takeaways
---
**Where did I go wrong?**
- I didn't create a `ListNode()` value.
- I over-complicated the problem.
**Lessons Learned?**
- I don't need to keep track of previous because im just creating a new list instead.
**Aha Moments?**
