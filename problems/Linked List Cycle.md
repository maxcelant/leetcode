---
tags:
  - linked-list
  - easy
  - hashing
pattern: Use a set to keep track of seen values, return True if you see the same one again.
rating: 1000
last_attempt: 2025-05-10
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
        visited = set()
        cur = head
        while cur:
            if cur.val in visited:
                return True
            visited.add(cur.val)
            cur = cur.next
        return False
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Use the values seen so far.
#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**

**Aha Moments?**
