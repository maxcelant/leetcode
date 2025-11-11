---
tags:
  - arrays
  - medium
  - meta
  - bucket-sort
  - heaps
last_attempt: 2025-11-07
link: https://leetcode.com/problems/top-k-frequent-elements/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rate:
  - ★★★★★
---
#### Problem
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

>Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

>Input: nums = [1], k = 1
Output: [1]

Example 3:

>Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

#### Notes
---
Use bucket sort where each bucket is the frequency of that element in the list.

The buckets go from 1 to N, where N is the length of the nums array. Each bucket is a list, because it can hold multiple values.

>[!important]
>We create N buckets because AT MOST an element can show up N times in the list.

To get the top K elements, we simply iterate over the buckets in reverse order (top to bottom).
#### Code
---
**Time Complexity**: O(NlogK)
**Space Complexity**: O(K)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): 
            return nums
        # Get frequencies of all the elements
        freqs = Counter(nums)
		# Create N buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        # Add the element to the correct bucket based on its frequency
        for n, f in freqs.items():
            buckets[f].append(n)
        res = []
        # Flatten the buckets from highest to lowest
        for b in reversed(buckets):
            res.extend(b)
        return res[:k]
```


#### Follow Up: *"Can you make it faster?"*

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): 
            return nums
        # Get frequencies of all the elements
        freqs = Counter(nums)
		# Create N buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        # Add the element to the correct bucket based on its frequency
        for n, f in freqs.items():
            buckets[f].append(n)
        res = []
        # Flatten the buckets from highest to lowest
        for b in reversed(buckets):
            res.extend(b)
        return res[:k]
```