---
tags:
  - binary-search
  - medium
rating: 3
pattern: Use binary search to find the optimal k rate, from 0-max(piles). Keep track of the min result
link: https://neetcode.io/problems/eating-bananas
last_attempt: 2025-05-09
---
#### Intuition
---
- We want to find the _minimum_ number of bananas that koko needs to eat per hour, such that she will eat all the bananas in `h` hours or less—and we want the min number of bananas she should eat.
- We know for sure that the max value in the list will do it in less than `h` hours, since koko can eat 1 pile per hour.
- So to find the minimum bananas per hour, we can use binary search.
- Our binary search

#### Code
---

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l < r:
            eating_rate = l + ((r - l + 1) // 2)
            total_hours_needed = 0
            for p in piles:
                total_hours_needed += math.ceil(p / eating_rate)
            if total_hours_needed > h:
                l = eating_rate + 1
            else:
                res = eating_rate
                r = eating_rate - 1
        return res
```

#### Insight
---
- If we are not able to eat all bananas within the allotted `h` hours, then that means we are eating too slow. Which means we need to increase the eating rate.
	- This is our binary search condition.

#### Takeaways
---
- **Where did I go wrong?**
	- The problem itself is written kind of strangely and it was difficult to decipher the intention.
- **Lessons Learned?**
	- `math.ceil` will return the rounded-up answer no matter what. so `2.2` becomes `3`.
		- This is key because if the eating rate is `4`, and there are `9` bananas in a pile, it will take `3` hours. `4 -> 8 -> 9`
- **Aha Moments?**
	- Our binary search is not on the piles of bananas, but on the different eating/hour rates!
	- Starting from 1 banana per hour -> max(piles) per hour.
	- ★ Because again, we know for certain that if we eat the number of bananas equal to the largest pile of bananas then we will be able to eat all other piles in 1 hour.