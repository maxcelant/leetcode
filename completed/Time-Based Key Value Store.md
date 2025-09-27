---
tags:
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Since the pairs are in sorted order, and I need to be able to return values that are <= to a given timestamp—binary search is a great approach to avoid having to loop through the list in reverse order.
#### Code
---

```python
class TimeMap:

    class TimestampValuePair:
        def __init__(self, value: str, timestamp: int):
            self.value = value
            self.timestamp = timestamp

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(
            self.TimestampValuePair(value=value, timestamp=timestamp)
        )

    def get(self, key: str, timestamp: int) -> str:
        # Search through the timestamps for the key
        # We want to find the "latest" key, so we will use 
        # binary search to find the latest key that exists.
        pairs = self.map.get(key, [])
        if pairs == []:
            return ""
        res = ""
        l, r = 0, len(pairs) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            # A timestamp is only valid if it's less
            # than or equal to the entered timestamp
            # because we cannot have a value that is
            # greater than our timestamp
            if pairs[m].timestamp <= timestamp:
                res = pairs[m].value
                l = m + 1
            else:
                r = m - 1
        return res
```

#### Insight
---
_"What are the important aspects of the solution?"_
- Realize that the key are inserted in increasing order, meaning they are sorted!
- `map.get(t)` works such that `timestamp <= t` are valid, this means that anything larger than `t` cannot be a valid return value.

#### Takeaways
---
- **Where did I go wrong?**
- **Lessons Learned?**
- **Aha Moments?**