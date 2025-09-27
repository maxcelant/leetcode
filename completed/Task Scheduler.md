---
tags:
  - medium
  - heaps
  - queue
  - retry
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We will need the frequency of each task, so that we always prioritize the one with the most left.
- Use a max heap, so that we can pop from the top.
- Use a queue, so that we can put tasks that are in cooldown into it.

#### Code
---

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-freq for freq in counter.values()]
        heapq.heapify(max_heap)
		
        cooldowns = deque()

        # Keeping track of the current time interval
        time = 0
        # We want to loop until all the tasks are handled
        while max_heap or q:
            time += 1
            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq:
                    # "time + n" dictates the timestep when we can remove it from queue.
                    q.append((freq, time + n))
            if cooldowns and cooldowns[0][1] == time: # See if cooldown timestep is now!
                freq, _ = cooldowns.popleft()
                heapq.heappush(max_heap, freq)
        return time 
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We want to use a queue for our cooldowns in combination with a "cooldown time step" which basically tells us at what `time` we can re-add the top of the queue to the heap.
- We need to ensure that both are empty before we end.

#### Takeaways
---
**Where did I go wrong?**
- I tried using a normal list instead of a queue so it was super inefficient.
- I was keeping track of the `task` name itself which isn't necessary in this case.
**Lessons Learned?**
- I can use a queue to keep track of values that are in cooldown, and pop them according to a set time in the future.