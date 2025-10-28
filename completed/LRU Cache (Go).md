---
tags:
  - nvidia
  - medium
  - linked-list
link: https://leetcode.com/problems/lru-cache/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-10-26
rate:
  - ★★★★
---
#### Variants


#### Problem
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```
 

#### Notes
Make the helper functions work on the NODES, not values. These helper functions should not create or add the nodes themselves, or even touch the cache at all. Just simply node level operations.

For `Get()`:
- We simply see if the key is in the cache, if it isn't we return -1.
- If it is, then we first remove and re-insert the node to the front of the list.

For `Put()`:
- A bit more complex.
- First we see if the key already exists, if it does, we simply update the value, remove and re-insert the node into the cache. (moving to the front). We can simply return after this.
- If the key isn't in the cache, we create the node, insert it and add it to the cache.
- Finally, we check to see if we've reached our capacity, if we have, then we evict the LRU node, which sits at `tail.prev`. Don't forget to remove it from the cache.

#### Code
**Time Complexity**:
**Space Complexity**: 

```go
type Node struct {
    key int
    val int
    next *Node
    prev *Node
}

type LRUCache struct {
    capacity int
    head, tail *Node
    cache map[int]*Node
}

func Constructor(capacity int) LRUCache {
    head := &Node{key:-1, val:-1}
    tail := &Node{key:-1, val:-1}
    head.next = tail
    tail.prev = head
    return LRUCache{
        capacity: capacity,
        head: head,
        tail: tail,
        cache: make(map[int]*Node),
    }
}

func (lru *LRUCache) insert(n *Node) {
    // make the node the first one in the lru cache
    prevHead := lru.head.next
    n.next = prevHead
    n.prev = lru.head
    lru.head.next = n
    prevHead.prev = n
}

func (lru *LRUCache) remove(n *Node) {
    n.prev.next = n.next
    n.next.prev = n.prev
}

func (lru *LRUCache) Get(key int) int {
    node, ok := lru.cache[key]
    if !ok {
        return -1
    }
    lru.remove(node)
    lru.insert(node)
    return node.val
}

func (lru *LRUCache) Put(key int, value int)  {
    if node, ok := lru.cache[key]; ok {
        node.val = value
        lru.remove(node)
        lru.insert(node)
        return
    } 
    node := &Node{val: value, key: key}
    lru.cache[key] = node
    lru.insert(node)

    if len(lru.cache) > lru.capacity {
        evictedNode := lru.tail.prev
        lru.remove(evictedNode)
        delete(lru.cache, evictedNode.key)
    }
}
```


#### Follow Up: *""*

```python

```