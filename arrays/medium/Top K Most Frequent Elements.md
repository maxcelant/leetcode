#### Approach
---
- Keep track of the value and its frequency.
- Use a heap to continuously keep the most frequent at the top
- Heaps are min heap by default, so we can make it negative to fix it.
- Find frequencies first 
- Then insert them in heap.

#### Code
---
```python
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        for v, f in freqs.items():
            heapq.heappush(h, (-f, v))

        res = []
        while k > 0:
            res.append(heapq.heappop(h)[1])
            k -= 1
        return re
```

#### Where did I go wrong?
---
- 