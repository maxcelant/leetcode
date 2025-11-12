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
        l, r = 0, len(self.points) - 1
        pivot_index = len(self.points)
        while pivot_index != k:
            pivot_index = self.partition(l, r)
            if pivot_index > k:
                r = pivot_index - 1
            else:
                l = pivot_index
        return self.points[:k]

    def partition(self, l, r):
        pivot_val = self.dist(self.points[l + (r - l) // 2])
        while l < r:
            if self.dist(self.points[l]) < pivot_val:
                l += 1
            else:
                self.points[l], self.points[r] = self.points[r], self.points[l]
                r -= 1
        
        if self.dist(self.points[l]) < pivot_val:
            l += 1
        return l
    
    def dist(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2
```
