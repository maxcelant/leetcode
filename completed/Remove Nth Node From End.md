---
tags:
  - linked-list
  - medium
  - meta
last_attempt: 2025-11-17
rate:
  - ★★★★★
link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
---
#### Variants

#### Problem
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

**Input:** head = [1,2,3,4,5], n = 2
**Output:** [1,2,3,5]

#### Notes

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        l = dummy
        r = head
        # Move r N nodes ahead
        while n > 0 and r:
            r = r.next
            n -= 1
        
        # Move both pointers simultaneously until r reaches the end
        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return dummy.next
```

