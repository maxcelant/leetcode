---
tags:
  - 1d-dynamic-programming
  - easy
pattern: This is just factorial in disguise
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that I need previous sub-steps for the current solution.
- This is exactly what DP is for.

#### Code
---

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        x, y, z = 1, 0, 0
        for _ in range(n+1):
            y = x
            x = z
            z = x + y
        return z
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- `z` is the next step, `x` is the current step, `y` is the previous step.
- We just continue to move one forward, updating all three as we go.

#### Takeaways
---
**Lessons Learned?**