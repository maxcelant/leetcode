---
tags:
  - iteration
  - arrays
pattern: sort cars and find finish time, keep track of slowest, any time you see a new slowest, increment fleets by 1
rating: 2
last_attempt: 2025-05-05
---
#### Video Breakdown
![[carfleet.mov]]

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort(reverse=True)
        slowest = float('-inf')
        res = 0
        for pos, speed in cars:
            finish_time = (target - pos) / speed
            if finish_time > slowest:
                slowest = finish_time
                res += 1
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**