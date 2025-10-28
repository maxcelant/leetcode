---
tags:
  - greedy
  - heaps
  - nvidia
  - medium
link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-10-25
rate:
  - ★★★
---
#### Variants
- 

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
func maxEvents(events [][]int) int {
    res := 0
    pq := &IntHeap{}
    heap.Init(pq)
    slices.SortFunc(events, func(a []int, b []int) int {
        return a[0] - b[0]
    })
    lastDay := 0
    for _, event := range events {
        lastDay = max(lastDay, event[1])
    }
    i := 0
    for day := 1; day < lastDay + 1; day++ {
        for i < len(events) && events[i][0] <= day {
            heap.Push(pq, events[i][1])
            i++
        }
        for pq.Len() != 0 && pq.Peek() < day {
            heap.Pop(pq)
        }
        if pq.Len() != 0 {
            heap.Pop(pq)
            res++
        }
    }
    return res
}

type IntHeap []int

func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any) { 
    *h = append(*h, x.(int))
}
func (h IntHeap) Peek() int { return h[0]}
func (h *IntHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}
```


#### Follow Up: *""*

```python

```