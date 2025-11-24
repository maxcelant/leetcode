---
tags:
  - heaps
  - nvidia
  - medium
link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-11-23
rate:
  - ★★★
---
#### Problem
You are given an array of `events` where `events[i] = [startDayi, endDayi]`. Every event `i` starts at `startDayi` and ends at `endDayi`.

You can attend an event `i` at any day `d` where `startDayi <= d <= endDayi`. You can only attend one event at any time `d`.

Return _the maximum number of events you can attend_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/02/05/e1.png)

**Input:** events = [[1,2],[2,3],[3,4]]
**Output:** 3
**Explanation:** You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

#### Notes
We loop from day 1 to max(endDay).

The goal is to prioritize events by the earliest end date, since they have a smaller window of possibly attending.

We use a min heap to always pick events with a closer end date.
We add events to the min heap that have a start time less than or equal to the current day (i).

>[!note] 
>This means that the events are still within their attendable time. We haven't reached their end date yet.

We pop from the heap and events that have an end date less than `i`, because this means we've missed the chance of attending that event.

>[!note]
>Imagine its day 4 and the event ended on day 3, we've missed the opportunity to attend that event.


#### Code
**Time Complexity**: O(TlogN)
**Space Complexity**: O(N)

```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        minHeap = []
        events.sort()
        # Find the last possible day to attend an event
        maxDay = max([ e[1] for e in events ])
        res = i = 0
        for day in range(maxDay + 1):
            # Add all the events with a start day that is
            # within the range
            while i < len(events) and events[i][0] <= day:
                # Use the end date at the minheap key
                heapq.heappush(minHeap, events[i][1])
                i += 1
            
            # Remove any events that are passed their attendable date
            while len(minHeap) != 0 and minHeap[0] < day:
                heapq.heappop(minHeap)
            
            # If there is at least one available event, attend it
            if len(minHeap) != 0:
                res += 1
                heapq.heappop(minHeap)
        return res
```
