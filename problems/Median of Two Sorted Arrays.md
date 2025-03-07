---
tags:
  - two-pointers
  - hard
---
#### Intuition
---
- Since the arrays are sorted, we don't need to merge them to figure out the median.
- Just use a pointer in each list, and increment the smaller pointer on each iteration. 
- Iterate `(n+m // 2)` times.

#### Code
---

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We want to have a pointer at the start of both nums1 and nums2
        # Increment the smaller one
        # When we reach the end of one of the lists, we just want to increment the other
        # We will simply just make a helper func that returns the "next" value in the list
        # We loop through (n+m)/2 times.
        # If its an odd number of values, we return the middle
        # If its an even number of values, then we take the middle values and 
        # so loop (n+m - 1) times and take the next two and divide by 2
        n = len(nums1) 
        m = len(nums2)
        p1, p2 = 0, 0

        def next() -> int:
            nonlocal p1, p2
            res = None
            if p1 < n and p2 < m:
                if nums1[p1] < nums2[p2]:
                    res = nums1[p1]
                    p1 += 1
                else:
                    res = nums2[p2]
                    p2 += 1
            else:
                if p1 == n:
                    res = nums2[p2]
                    p2 += 1
                else:
                    res = nums1[p1]
                    p1 += 1
            return res
        
        if (n + m) % 2 == 0: # Even case
            for _ in range(((n+m) // 2) - 1):
                next()
            return (next() + next()) / 2
        else:              # Odd case
            for _ in range((n+m) // 2):
                next()
            return next()
```

#### Insight
---
- We use this helper function to always get the next value that's pointed to.
	- This is important because it let's us use the same function for odd and even lengths.
- Since we need two values for even cases, we need to stop the loop one value early so we can grab the **next two**—Hence the `((n+m)//2)-1`

#### Takeaways
---
- **Where did I go wrong?**
- **Lessons Learned?**
	- When the lists are already sorted for you, a lightbulb should go off in your head that some kind of "two pointers" will be helpful.
- **Aha Moments?**