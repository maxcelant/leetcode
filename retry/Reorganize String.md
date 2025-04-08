---
tags:
  - heaps
---

#### Intuition
---
- Feels like a heap question.
- Keep track of the chars, and the frequency of each.
- Pop from the heap, add it to the string and then re-add it after a delay (one turn).
- When heap is empty, our string is done.
- If the previously popped is the last thing in the heap and there is more than one on the frequency count then we return `""`.

#### Code
---

```python
class Solution:
  def reorganizeString(self, s: str) -> str:
    c = Counter(s)
    h = [(-v,k) for k,v in c.items()]
    heapq.heapify(h)
    prev = None # (freq, char)
    res = []

    while h or prev:
      # If there's a prev but the heap is empty that means that the
      # last character was the prev, so this fails
      if prev and not h:
        return ""
      
      freq, char = heapq.heappop(h)

      res.append(char)
      freq += 1 # Since it's technically a min heap, we add 1

      # Add previously waiting character
      if prev:
        heapq.heappush(h, prev)   
        prev = None

      # If there are more occurences, save for later
      if freq < 0:
        prev = (freq, char)

    return "".join(res)
```

#### Insight
---
- We should immediately null out our `prev` value, since this could be the last time it's needed.
- Only assign `prev` if there is a value to assign it to.

#### Takeaways
---
- **Where did I go wrong?**
	- Got a little confused with the `prev` assignment. 
	- I should've known to only set `prev` if there is one to set.
	- Also need to work on my error condition.
- **Lessons Learned?**
	- Work on the handling of those temporary variables.
- **Aha Moments?**