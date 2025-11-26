---
tags:
  - linked-list
  - medium
  - meta
  - nvidia
link: https://neetcode.io/problems/lru-cache
last_attempt: 2025-11-25
rate:
  - ★★★★★
---
#### Problem
Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

#### Notes
---
In this problem, the `head` acts as the back of the list and the `tail` is the front of the list. The LRU would be the `head.next` value since `head` and `tail` are both dummy nodes.

#### Code
---

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(-1,-1), Node(-1,-1)
		# Link the head and tail together
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
		# Make the prev pointer point to the next
		# And vice versa
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node: Node):
		# Shift the tail by one
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
		# Remove if before re-adding it
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
        
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
```
