---
tags:
  - hashing
  - medium
pattern:
link: https://neetcode.io/problems/subarray-sum-equals-k?list=neetcode250
rating: 3
last_attempt: 2025-09-15
---
#### Problem
You are given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

**Example 1:**

```java
Input: nums = [2,-1,1,2], k = 2

Output: 4
```

Explanation: `[2]`, `[2,-1,1]`, `[-1,1,2]`, `[2]` are the subarrays whose sum is equals to `k`.

**Example 2:**

```java
Input: nums = [4,4,4,4,4,4], k = 4

Output: 6
```

#### Notes
---
- Keep a dictionary of the prefix sums which is the _number of occurrences of a given sum_.
- This will allow us to subtract the current sum - k, and see how many times that result has been seen before.

##### Example
Let's say you have `nums=[1,2,2,-1]`, and `k=3`.
1. `cursum=1`, `diff=2`, since `prefix_sums[2]` is 0, nothing changes, but we add `prefix_sums[1]=1` because what we are saying is "There is one prefix that exists that equals 1".
2. `cursum=3, diff=0`, since `prefix_sums[0]` is 1 (set on line 7), we are saying "There is one way prefix that exists that equals 0". We increase the result by that value. We add `prefix_sums[3]=1`, because we now know that there is a prefix array that adds up to 3.


#### Code
---

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        # By default, there is one occurence of 0
        # Because removing nothing is still something
        # 3 (cursum) - 3 (k) = 0
        prefix_sums[0] = 1
        res = cursum = 0
        for n in nums:
            cursum += n
            diff = cursum - k
            # The number of prefixes that IF REMOVED
            # would give us the value `k`
            res += prefix_sums.get(diff, 0)
            # This is the sum for this subarray
            # It'll become a prefix for a future value
            prefix_sums[cursum] += 1
        return res
```
