---
tags:
  - linked-list
  - easy
  - hashing
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to see if the same node has already been seen—this should make us think two things: hashing OR fast/slow pointers. 
- I went with hashing this time because it seemed easier.

#### Code
---

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if id(cur) in seen:
                return True
            seen.add(id(cur))
            cur = cur.next
        return False
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- I keep track of seen nodes by using `id()` and a `set`.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**

**Aha Moments?**
