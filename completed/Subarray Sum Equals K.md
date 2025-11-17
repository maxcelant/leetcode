---
tags:
  - hashing
  - medium
  - meta
link: https://neetcode.io/problems/subarray-sum-equals-k?list=neetcode250
last_attempt: 2025-10-14
rate:
  - ★★★★★
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
We are accumulating as we go along. At each iteration, we add an entry to our indicating the current sum. 

Remember: the goal is to find all subarrays that sum to `k`. So if I know the sum of a subarray then I can check if _removing it from the total_ will result in `k`.


>[!important] Example
>The current sum is 3 and k is 5 ( diff=sum-k ). That would mean that removing ANY past subarrays with a total of 2 would result the total k.

#### Code
---

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        subarray_sums = defaultdict(int)
        subarray_sums[0] = 1
        res = 0
        for n in nums:
            cursum += n
            diff = cursum - k
            # Removing subarrays of sum `diff` will result in a total of k
            # Starting from the current sum
            res += subarray_sums[diff]
            # Accumulate the number of times this sum is seen
            subarray_sums[cursum] += 1
        return res
```
