---
tags:
  - heaps
  - medium
  - meta
link: https://leetcode.com/problems/k-closest-points-to-origin/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 5
last_attempt: 2025-10-11
rate:
  - ★★★★★
---
#### Problem
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:
>Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


#### Notes
---
Calculate the distance and store the distance and original index in a `minheap`. Pop `k` values from the `minheap` and use index to get original pair.

#### Code
---

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean(x, y):
            return sqrt(pow(x, 2) + pow(y, 2))
            
        minheap = []
        for i, p in enumerate(points): 
            x, y = p
            heapq.heappush(minheap, (euclidean(x, y), i))
        
        res = []
        while k:
            i = heapq.heappop(minheap)[1]
            res.append(points[i])
            k -= 1
        return res
```


#### Follow Up: *""*

```python

```