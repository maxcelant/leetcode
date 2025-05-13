---
tags:
  - two-pointers
  - medium
target: "3"
pattern: Use floyds tortoise and hare algorithm
last_attempt: 2025-05-13
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- This one is unique in that, you kind of need to see it to know how it works.

#### Code
---

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use a fast and slow pointer
        # To find where they intersect
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Use Floyd's algorithm to find the intersection from the 
        # starting position and the slow position
        start = 0
        while True:
            slow = nums[slow]
            start = nums[start]
            if slow == start:
                return slow
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Finding a cycle involves using a fast and slow pointer, and going around until the two meet.
- Once they meet, we stop that section and move one to the second part of the algorithm. 
- We need to have one pointer that starts at the beginning of the list called `start` and one that starts from the previous fast/slow intersection point.
- We need to continue looping and updating each value until the `start` and `slow` values finally meet!

#### Takeaways
---
**Where did I go wrong?**
- Didn't know this algorithm prior to performing this problem.
**Lessons Learned?**
- You can use fast/slow pointers to find where they intersect to find cycles.
- More info [[Linked Lists|here]].