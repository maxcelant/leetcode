---
tags:
  - linked-list
  - hard
  - iteration
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Since we need to connect the old head from the previous group to new head of this group, we need to store that somewhere.
- We should use a look ahead to see if there are K nodes remaining and do something depending on that outcome.
- Since we are reversing the list, we need to store the new head.

#### Code
---

```python
class Solution:
    def reverse(self, head, k):
        prev, cur = None, head
        while k > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            k -= 1
        return prev # This will return the "new head"

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev_tail = None
        new_head = None
        cur = head
        while cur:
            cur = head
            count = 0
            # cur acts as a look-ahead
            while cur and count < k:
                cur = cur.next
                count += 1
            
            # Handle group smaller than K
            if count != k:
                break

            # Handle group equal to K, reverse them
            rev_head = self.reverse(head, k)

            # Once the first group is reversed,
            # this `rev_head` will become the new head of the entire list.
            if not new_head:
                new_head = rev_head
            
            # Since we don't want to accidentally assign the first 
            # tail to the same groups head, we need this condition here
            if prev_tail:
                prev_tail.next = rev_head
            
            # Assign the head of the previous group as the tail
            prev_tail = head
            # Assign head to cur
            head = cur

        # Handling the final group if nodes < k
        if prev_tail:
            prev_tail.next = head
        
        return new_head if new_head else head
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We use `cur` as a look-ahead in this problem, not to actually perform any computations. Then after the group was accounted for, we assign `head` to `cur` effectively moving it to the next group.
- `if not new_head` section ensures that as soon as we have the new head of the entire linked list, we will store it and not update it.
	- Ex:`1 -> 2 -> 3 -> 4, k = 2`. When updated `2 -> 1 -> 4 -> 3`, As soon as `2` which is the `new_head` is found, we store it and use it to return the list at the end.
- We use a `if prev_tail` to ensure that the first grouping does not connect to itself. Without it, as soon as we found `rev_head`, we would be assigning it to the tail of it's own group.
- At the end of each loop, we move forward `prev_tail` to be the previous `head`.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**