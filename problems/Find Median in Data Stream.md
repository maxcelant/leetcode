---
tags:
  - hard
  - heaps
  - retry
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- I need to maintain where the median is as I add more elements so i can use the [[Heaps#Two Heap Median|dual heap median]] method.

#### Code
---

```python
class MedianFinder:

    def __init__(self):
        self.hi, self.lo = [], []

    def addNum(self, num: int) -> None:
        # We add to lo first and re-order so that we can maintain balance and length of each heap.
        heapq.heappush(self.lo, -num)
        val = -1 * heapq.heappop(self.lo)
        heapq.heappush(self.hi, val)
        if len(self.lo) < len(self.hi):
            val = -1 * heapq.heappop(self.hi)
            heapq.heappush(self.lo, val)
        
    def findMedian(self) -> float:
        if (len(self.lo) > len(self.hi)) % 2 == 1: # Odd case
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2  # Even case
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Look at the dual heap median notes for details

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**