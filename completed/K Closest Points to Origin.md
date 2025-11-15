---
tags:
  - medium
  - meta
  - quickselect
link: https://leetcode.com/problems/k-closest-points-to-origin/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-12
rate:
  - ★★★
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
First of all, check out [[QuickSelect]]. It is the majority of the difficulty of this problem.

Since we want the first `k` points in no particular order, quickselect is the way to go.

We stop once we reach the first `k` values. We know this is true when the pivot returns as `k`.

#### Code
---

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.points = points
        l, r = 0, len(points) - 1
        while l <= r:
            p = self.partition(l, r)
            if p == k:
                break
            elif p < k:
                l = p + 1
            else:
                r = p - 1
        return self.points[:k]
    
    def partition(self, l, r):
        pivot = self.dist(self.points[r])
        i = l
        for j in range(l, r):
            if self.dist(self.points[j]) <= pivot:
                self.points[i], self.points[j] = self.points[j], self.points[i]
                i += 1
        self.points[i], self.points[r] = self.points[r], self.points[i]
        return i

    def dist(self, point):
        return point[0]**2 + point[1]**2
```
