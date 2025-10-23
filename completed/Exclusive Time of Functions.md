---
tags:
  - stack
  - meta
  - medium
link: https://leetcode.com/problems/exclusive-time-of-functions/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-21
rate:
  - ★★
---
#### Variants
- [[Exclusive Time of Functions (Variant)]]

#### Problem
On a **single-threaded** CPU, we execute a program containing `n` functions. Each function has a unique ID between `0` and `n-1`.

Function calls are **stored in a [call stack](https://en.wikipedia.org/wiki/Call_stack)**: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is **the current function being executed**. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

#### Notes
As functions are started, we add their ids to a `stack`.

We use a `prev` value to denote the value of the previous point so that we can calculate the difference between the current and the previous. This will tell us how much time the previous function was executing before the new one was called.

When we reach a start, we calculate the diff and add that diff to whatever is at the top of the stack. We then proceed to add the current function to the stack.

When we reach an end, we calculate the diff and add that diff to the top of the stack, which should be the current function. We then pop it from the stack because it ended.

**Example**

>![[Pasted image 20251021230309.png]]
>`foo` was started at 10s and at 20s, `bar` was called. Since `prev` was set to 10s, we know that the duration of `foo` was 10s (20 - 10 = 10).


#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prev = 0
        stack = []
        res = [0] * n
        for log in logs:
            fn_id, state, time = log.split(":") 
            fn_id, time = int(fn_id), int(time)
            if state == "start":
                # The stack will be empty on the first value
                if stack:
                    # Add the diff in time to the function at the top
                    # of the stack (which should be the previous one since
                    # we haven't added this new one yet)
                    res[stack[-1]] += time - prev
                # Add new function id to stack
                stack.append(fn_id)
                # Update prev to current
                prev = time
            elif state == "end":
                # If the function is done, then we pop it but we want to calculate the
                # total time that it was running
                popped_fn_id = stack.pop()
                res[popped_fn_id] += time - prev + 1
                prev = time + 1
        return res
```


#### Follow Up: *""*

```python

```