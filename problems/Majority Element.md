---
tags:
  - medium
  - hashing
pattern: Frequency dict, return top n / 3 most frequent elements
link: https://neetcode.io/problems/majority-element-ii?list=neetcode250
rating: 1000
last_attempt: 2025-09-15
---
#### Problem
You are given an integer array `nums` of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times. You can return the result in any order.

**Example 1:**

```java
Input: nums = [5,2,3,2,2,2,2,5,5,5]
Output: [2,5]
```

**Example 2:**

```java
Input: nums = [4,4,4,4,4]
Output: [4]
```

#### Notes
---
- Keep frequency dict.
- Loop through, calculate frequency.
- Add any elements that have N // 3 `freq` to the result list.

#### Code
---

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        N = len(nums)
        for n in nums:
            freq[n] += 1
        return [n for n, freq in freq.items() if freq > (N // 3)]
```
