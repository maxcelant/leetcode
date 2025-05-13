---
tags:
  - linked-list
pattern: Use a dict and a doubly-linked list. Use dummy head and tail. Use helper remove and add methods.
link: https://neetcode.io/problems/lru-cache
rating: 2
last_attempt: 2025-05-13
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- If we want `O(1)` to get and put, then we need to use a dictionary for the look up and a doubly linked list to update the node in `O(1)` time.

#### Code
---

```python
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # These are dummy nodes (not meant to hold values)
        self.head = self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: ListNode):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    
    def _add_to_front(self, node: ListNode):
        oldhead = self.head.next
        self.head.next = node
        node.next = oldhead
        node.prev = self.head
        oldhead.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])       
        
        node = ListNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            node_to_remove = self.tail.prev
            self._remove(node_to_remove)
            del self.cache[node_to_remove.key]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Make sure that you attach the dummy head to the tail in the initialization step.
- Use the helper methods, they simplify the logic greatly.

#### Takeaways
---
**Lessons Learned?**
Use dummy head and tail nodes.