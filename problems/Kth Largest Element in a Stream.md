---
tags:
  - heaps
  - easy
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We only "need" the K-th largest elements, so we can get rid of anything smaller.
- We can use a min-heap and "pop" elements until the length of the list is K in size because this will determine that the "first" element will be the Kth largest element

#### Code
---

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        # Pop nums until heap is K in size
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the kth largest num 
        # Since it's a min heap, this will be the first value
        return self.heap[0]

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Since we only care about the largest K nodes, we just remove the the smaller nodes until the heap is of size K, and that will guarantee that the 0th value is the kth largest node.

#### Takeaways
---
**Where did I go wrong?**
- I was trying to create a max heap and get the  Kth largest from the top, but it's easier to use a min heap and just remove until you get to K.
**Lessons Learned?**
- If you need the Kth largest element, use a min heap and pop the smaller nodes.