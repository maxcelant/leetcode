---
tags:
  - meta
  - medium
  - binary-search
link: https://leetcode.com/problems/random-pick-with-weight/submissions/1802015201/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-14
rate:
  - ★★
---
#### Problem
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range `[0, w.length - 1]` (inclusive) and returns it. The probability of picking an index i is `w[i] / sum(w)`.

For example, if w = `[1, 3]`, the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:
```
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]
```

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

```
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]
```

Explanation
```
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
```

#### Notes
---
A value at the index position dictates it's probability of being picked e.g. `[1,9]` means we have a 9/10 chance of choosing index 1.

We can use a prefix sum array where we each index is a sum of the total so far. Then when we get a random target, it's easy to see where it lands because you see which prefix sum it falls into.

We multiply the target (which is between 0 and 1) by the total sum of the weights.

Example:
- nums = `[1, 9]`
- prefix sum = `[1, 10]`
- Let's say the target is `0.34`, multiply this by 10 (bc total sum is 10) and we get `3.4`.
- `3.4` is larger than 1, so we know it won't fall into the range of index 0.
- `3.4` is less than 10, so we know it DOES fall into the range of index 1.

Taking this approach, we can do this faster using binary search. We simply close in on both sides until `left` and `right` meet.

>[!important]
>`m` is biased towards `l` because we round down. So we need to do `r = m` to not cause an infinite loop while shrinking towards `l == r`. We can confidently reduce `r` it doesn't have this issue. We must strictly increment `l`!

#### Code
---
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        cursum = 0
        for n in w:
            cursum += n
            self.prefix_sums.append(cursum)
        self.total = cursum

    def pickIndex(self) -> int:
		# Get a random number 0 -> 1 then mul by total
        target = self.total * random.random()
        l, r = 0, len(self.prefix_sums)
        while l < r:
            m = l + (r - l) // 2
			# Shrink until l, r pointers converge
            if target <= self.prefix_sums[m]:
                r = m
            else:
                l = m + 1 # Strictly increment l! left bias
        return l
```


#### Follow Up: *""*

```python

```