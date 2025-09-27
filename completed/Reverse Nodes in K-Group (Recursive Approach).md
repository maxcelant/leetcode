---
tags:
  - linked-list
  - hard
  - recursion
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Since we are breaking it into groups, recursion is a good choice.
- Make sure to check if there are `k` nodes before trying to reverse.
- Since we need to connect the previous groups ORIGINAL head to the newest groups NEW reversed head, bottom-up approach makes a lot of sense.

#### Code (Recursive Solution)
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
        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        
        # See if there are K nodes left,
        while cur and count < k:
            cur = cur.next
            count += 1
        
        # If not, we don't reverse them
        if count != k:
            return head
        
        # If there are, then we will reverse them
        rev_head = self.reverse(head, k)

        # Recursively call func, "bottom-up" approach
        # So the last reversed head will become attached to 
        # the previous groups "head"
        head.next = self.reverseKGroup(cur, k)

        # We return the reversed head, because we will
        # need to connect it to the `head.next` of 
        # the previous group
        return rev_head
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Because we are doing this recursively, this makes it a bottom-up approach, meaning that the `reversedHead` value is going to be the reversed head from the end of the list.
	- This is key because if it was a top-down approach, then the `reversedHead` would be incorrect.
- The `head` returned from the reverse function needs to be attached to `head.next`, which is the original head from the previous segment. This makes sense if you think about it because that original head is what we now want to connect to the reversed segment.
- We recursively call `reverseKGroup` and pass in the `cur` node, because that points to the "next grouping".

>![[Pasted image 20250311150129.png]]

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**