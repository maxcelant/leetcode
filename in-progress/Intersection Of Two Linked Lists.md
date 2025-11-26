---
tags:
link:
last_attempt: 2025-11-25
rate:
---
#### Variants

#### Problem

#### Notes


#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        cur = headA
        while cur:
            seen.add(cur)
            cur = cur.next
        cur = headB
        while cur and cur not in seen:
            cur = cur.next
        return cur if cur in seen else None
```

