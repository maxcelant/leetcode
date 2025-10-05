---
tags:
  - stack
  - easy
link: https://neetcode.io/problems/implement-stack-using-queues?list=neetcode250
rating: 5
last_attempt: 2025-09-28
---
#### Problem
# Implement Stack Using Queues

Solved 

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element `x` to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns true if the stack is empty, false otherwise.

#### Notes
---
The idea is that when you push to the stack you have to basically reverse the queue so that the new element is at the top. 
#### Code
---

```python
class MyStack:
    def __init__(self):
        self.q = collections.deque([])

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
```
