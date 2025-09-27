---
tags:
  - heaps
  - easy
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We should use a heap so that we can always have the top to greatest stones
- When we insert, it will heapify that list, maintaining the order

#### Code
---

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if res := (-y) - (-x):
                heapq.heappush(heap, res)
        return -(heap[0]) if len(heap) == 1 else 0
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Heapify the stones and don't forget to negate so that we have a max heap.
- Loop until we have 1 value left (or zero)
- Pop the first two stones from heap.
- Subtract `y` from `x` and then re-add the result if it's greater than 0.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**
- Used a walrus operator to get the result from the condition directly.