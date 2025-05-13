---
tags:
  - linked-list
  - medium
rating: 2
pattern: Use fast-slow to find halfway point, reverse second half, merge two halves.
last_attempt: 2025-05-13
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Since we need to split the linked list (in a certain sense), that should indicate using a fast/slow pointer **to find the middle position**.

#### Code
---

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the linked list
        slow, fast = head, head.next
        # ? Question: Why fast and fast.next here?
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # merge
        p1 = head
        p2 = prev
        while p1:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- This problem can be broken down into three sections: finding the middle, reversing the second half, and merging the two halves.
- I should become comfortable with merging two lists and also with reversing a linked list.

#### Takeaways
---
**Where did I go wrong?**
- I was trying to make a copy of the list, this is not the right approach. Instead I should use fast/slow pointers to find the middle and reverse the second half.
**Lessons Learned?**
- The `slow` pointer will point to the middle of the linked list once the fast pointer reaches the end. This is good for finding the middle of a list.
- In the first part, we use `while fast and fast.next` because we are calling `fast.next`, we need to make sure that's `fast.next` IS a node, otherwise we will get a `NoneType` error.
