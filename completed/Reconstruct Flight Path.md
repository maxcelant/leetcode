---
tags:
  - graphs
  - hard
pattern: Sort, reverse the edges. Pop edge at current destination, continue til graph is empty
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need an adjacency list.
- Since we need to lexicographical order, we need to sort and reverse it.

#### Code
---

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create the adjacency list, but we store the edges in reverse, so we can pop them easily
        adj = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        stk = ["JFK"]
        res = []

        # We travese starting from JFK, and pop from the graph until the whole graph is empty
        # Because this signifies us "visiting" a location.
        # We pop from then adj because that is the lexicographically smallest one (at the end).
        while stk:
            # We continuously look at the top of the stack and find it's edges
            if adj[stk[-1]]:
                # We pop the lexicographically smallest edge
                popped = adj[stk[-1]].pop()
                # That is our "new" source, so we iterate from here
                stk.append(popped)
            # If the current location has no further destinations,
            # it means we've reached the end of that path,
            # so we add it to the itinerary (res).
            # This is effectively post-order traversal — we backtrack.
            # Previous locations on the stack may still have unexplored destinations.
            else:
                res.append(stk.pop())
        
        return res[::-1]
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- By sorting and reversing the edges, we make sure that we can pop from them in O(1) time.
- We are appending to the result in post-order, so we only add it to the result once a node has no more children to visit.
- We always start at JFK.
- Without a popping mechanism, we would visit each node indefinitely in a cycle!

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**