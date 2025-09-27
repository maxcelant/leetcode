---
tags:
  - stack
  - medium
rating: 3
pattern: Use monotonic
---

#### Intuition
---
- Honestly I was completely lost on how to approach this problem.
- This is definitely one to retry later.

#### Code
---
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We keep track of the position as well as the temperature of that position
        # When we pop, that means WE HAVE FOUND A WARMER TEMPERATURE
        # so that means that the value for that popped temp is the distance between itself and the 
        # temperature that popped it
        
        res = [0] * len(temperatures)
        stk = [] # stored as (temp, index position)

        for i in range(len(temperatures)):
            while stk and stk[-1][0] < temperatures[i]:
                _, idx = stk.pop()
                res[idx] = i - idx 
            stk.append((temperatures[i], i))

        return res

```

#### Insight
---
#### Takeaways
---
- Add values to the stack. 
- When a value that is found is greater than the top of the stack, we pop the top and get the diff.
- We place that output of that diff at the index of the popped value.
	- **important:** We will do this until the top of the stack is _greater_ than the current value.
- The stack will always be in monotonic decreasing order.
	- `(top) 1, 2, 3, 4, 5 (bottom)`
- If a value is smaller than the current top of the stack, we simply add it to the top of the stack.