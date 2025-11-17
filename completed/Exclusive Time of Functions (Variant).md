---
tags:
  - meta
  - medium
  - stack
link:
last_attempt: 2025-10-22
rate:
  - ★★★★★
---
#### Variants
- [[Exclusive Time of Functions]]

#### Problem

You are tasked to profile the performance of an application. Specifically, you are given a list of logs representing the execution of function calls in the single-threaded application. Each log records the function name, the event type ("start" or "end"), and the timestamp when the event occurred.

A function's exclusive time is defined as the total time it spends executing, excluding any time spent in its sub-functions (i.e., functions it calls directly).

Write a function `profile_app` that takes in the list of logs and returns a dictionary mapping each function name to its exclusive execution time. You may define the schema of each log however you choose.

```
Input: logs = [["foo","start",10],["bar","start",20],
               ["bar","end",50],["foo","end",100]]
Output: ["foo": 60, "bar": 30]
```

#### Notes
There are really two states to think about:
1. When we reach a start
	1. We need to calculate the previous functions run time
	2. Add the new function to the stack
2. When we reach an end
	1. We need to remove the function and calculate it's runtime
3. No matter what, we update prev

`prev` will always point to the last seen value.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
def exclusive_func_time(logs: list[any]) -> dict[str, int]:
    res = {name: 0 for name, _, _ in logs }
    stack = []
    prev = 0
    for log in logs:
        name, state, time = log
        match state:
            case "start":
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(name)
            case "end":
                removed_name = stack.pop()
                res[removed_name] += time - prev
        prev = time
    return res
```


#### Follow Up: *""*

```python

```