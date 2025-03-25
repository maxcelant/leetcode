---
tags:
  - hard
  - heaps
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```python
class MedianFinder:

    def __init__(self):
        '''
        - hi is the larger half  -> [8, 12, 15, 20]
        - lo is the smaller half -> [7, 5,  3,  1]
        - To make this work, `lo` needs to be a max heap, so all values will be negative
        - `lo` may have 1 more element than `hi`
        '''
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
- 

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**