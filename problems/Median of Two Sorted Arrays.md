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
        n, m = len(nums1), len(nums2)
        p1, p2 = 0, 0
        def get_next():
            nonlocal p1, p2
            if p1 < n and p2 < m:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p1 == n:
                ans = nums2[p2]
                p2 += 1
            else:
                ans = nums1[p1]
                p1 += 1
            return ans
        
        if (n+m) % 2 == 1: # Odd case
            for _ in range((n+m) // 2):
                get_next()
            return get_next()
        else:              # Even case
            for _ in range((n+m) // 2 - 1):
                get_next()
            return (get_next() + get_next()) / 2

```

#### Insight
---
- Use a pointer on each list, increment the smaller one until we reach `(n+m)//2` for odd and `((n+m // 2) + (n+m // 2) + 1) // 2` for even.
- We use this helper function to always get the next value that's pointed to.
	- This is important because it let's us use the same function for odd and even lengths.

#### Takeaways
---
- **Where did I go wrong?**
- **Lessons Learned?**
	- When the lists are already sorted for you, a lightbulb should go off in your head that some kind of "two pointers" will be helpful.
- **Aha Moments?**