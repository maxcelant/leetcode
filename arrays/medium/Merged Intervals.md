#### Approach
---
- My approach was to sort them and to combine them when the right value overlaps with the left of the next pair.

#### Code
---

```python
class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # Sort the pairs
    intervals.sort()
    res = []
    prev = intervals[0]
    for intr in intervals[1:]:
      # There's overlap, update end of pair
      if prev[1] >= intr[0]: 
        prev[1] = max(prev[1], intr[1])
      # No overlap, prev to be the current value
      else: 
        res.append(prev)
        prev = intr
    res.append(prev)
    return res
```


#### Where did I go wrong?
---
- I got stuck figuring out how to efficiently "merge" them. 
- The answer was using `prev` value and adding to it, and _only_ merging once we the next pair was not part of the merged sequence.
- I was trying to add directly to `res` instead of having a temporary data structure before adding to `res` to store the current in-progress values.