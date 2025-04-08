---
tags:
  - linked-list
  - hard
---

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- If we need to merge sorted lists/linked lists, remember this merging algorithm.
- If we need to combine them into one list, two pointers is a good choice.

#### Code
---

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

#### Insight  
---
_"What are the important aspects of the solution?"_
- Using the `range(1, len(..))` is very powerful here because we can accumulate the merging of the lists into the final array cell of the original list.
	- More on that [[Arrays#Flattening a List of Lists|here]]

#### Takeaways
---
**Where did I go wrong?**
- The edge case where it's an empty list should just return `None`, not a linked list with `None` as it's value.
**Lessons Learned?**
- This is a great way to merge a list of lists.