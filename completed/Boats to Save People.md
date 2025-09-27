---
tags:
  - medium
  - two-pointers
link: https://neetcode.io/problems/boats-to-save-people?list=neetcode250
rating: 4
last_attempt: 2025-09-21
---
#### Problem
You are given an integer array `people` where `people[i]` is the weight of the `ith` person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries **at most** two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return the **minimum** number of boats to carry every given person.

**Example 1:**

```java
Input: people = [5,1,4,2], limit = 6

Output: 2
```

Explanation:  
First boat `[5,1]`.  
Second boat `[4,2]`.

#### Notes
---
At most there can be two people, get the heaviest person on the boat no matter what, then check to see if the light person can also fit. If not, then the heavy person gets their own boat.
#### Code
---

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            res += 1
            r -= 1
        return res
```
