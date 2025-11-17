---
tags:
  - medium
  - stack
  - meta
link: https://leetcode.com/problems/merge-intervals/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 3
last_attempt: 2025-10-12
rate:
  - ★★★★★
---
#### Problem
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

>Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

>Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

>Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

#### Notes
---
Sorting is important for this problem otherwise this method doesn't work.

This problem is deceptively simple. If you think about it as a stack problem then it makes sense. You are basically trying to merge all possible intervals that fit into the current interval. If they don't then that becomes the new top of the stack because we have exhausted all possibilities of merging with the previous pair.

#### Code
---
**Time Complexity**: O(nlogn) because of sorting
**Space Complexity**: O(n)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # Add the first interval to the stack
        stack = [intervals[0]]
        for itr in intervals[1:]:
            # Compare the END of the previous pair with the START of the current pair
            # ex: [1, 3], [2, 6] -> [1, 6] BC 3 >= 2
            if stack[-1][1] >= itr[0]:
                stack[-1][1] = max(stack[-1][1], itr[1])
            # In all other cases we simply just append the interval to the stack
            else:
                stack.append(itr)
        return stack
```


#### Follow Up: *""*

```python

```