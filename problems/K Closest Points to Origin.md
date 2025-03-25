---
tags:
  - heaps
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Since we need the K smallest, let's use a min heap.
- We should use the euclidean distance as our min heap key.

#### Code
---

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        For each pair of points, calc euclidean distance
        Create a min heap
        data struct in heap is (dist, [x, y]) for each val, where dist is the sorting key
        Pop k points
        '''
        def euclidean(pair) -> int:
            x, y = pair
            return abs(math.sqrt((x ** 2) + (y ** 2)))

        heap = [(euclidean(pair), pair) for pair in points]
        heapq.heapify(heap)
        k_smallest = heapq.nsmallest(k, heap)
        return [pair for (dist, pair) in k_smallest]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- For each pair of points, calculate the euclidean distance.
- Create a min heap
- Since min heap needs a key, we will use the euclidean distance as the key.
- We still want to store the pair so our data structure in the heap will be `(dist, [x, y])`, since `heapq` uses the first value as the key.
- Use `heapq.nsmallest` to get the K smallest values from heap.
- Grab the pairs from the data structure.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**