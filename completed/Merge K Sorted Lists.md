---
tags:
  - linked-list
  - hard
link:
last_attempt: 2025-11-03
rate:
  - ★★★★
---
#### Variants


#### Problem


#### Notes
Merging the linked lists together is a bit like a zipper. We keep assigning the `next` pointer to the next lowest value in the two lists. 

#### Code
**Time Complexity**: O(k*N) where we have k lists and N total nodes
**Space Complexity**: O(1)

```python
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        # Accumulation merge
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i-1], lists[i])

        # Last index has the final merging
        return lists[-1]
    
    def merge(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        
        return dummy.next
```


#### Follow Up: *""*

```python

```