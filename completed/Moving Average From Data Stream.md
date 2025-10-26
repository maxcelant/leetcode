---
tags:
  - queue
  - meta
  - easy
link: https://leetcode.com/problems/moving-average-from-data-stream/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-23
rate:
  - ★★★★★
---
#### Variants
- [[K Radius Subarray Averages]]

#### Problem
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:

- `MovingAverage(int size)` Initializes the object with the size of the window `size`.
- `double next(int val)` Returns the moving average of the last `size` values of the stream.

**Example 1:**

**Input**
```
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
**Output**
[null, 1.0, 5.5, 4.66667, 6.0]

**Explanation**
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

#### Notes


#### Code
**Time Complexity**: O(M) for how many times `next()`  is called.
**Space Complexity**: O(N) for the size of the queue.

```python
class MovingAverage:
    def __init__(self, size: int):
        self.q = deque([])
        self.total = 0
        self.k = size

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val
        if len(self.q) > self.k:
            removed = self.q.popleft()
            self.total -= removed
        return self.total / len(self.q)
```


#### Follow Up: *""*

```python

```