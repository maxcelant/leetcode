---
tags:
  - 2d-matrix
  - medium
  - meta
link: https://leetcode.com/problems/diagonal-traverse-ii/description/
last_attempt: 2025-10-20
rate:
  - ★★★
---
#### Problem
Given a 2D integer array `nums`, return _all elements of_ `nums` _in diagonal order as shown in the below images_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png)

>**Input:** nums = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,4,2,7,5,3,8,6,9]

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png)

>**Input:** nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
**Output:** [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

#### Notes
---
The problem is much simpler once we start picturing it rotated.

![[Pasted image 20251020150128.png]]

We don't need a visited set or anything because we don't revisit nodes. We simply scan and add to the result.

To avoid adding the same cell twice, we only add the left child if it's the first column and we will always add the right child, assuming it's not out of bounds.

#### Code
---
**Time Complexity**: O(N*M)
**Space Complexity**: O(sqrt(N))

```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([])
        q.append((0, 0))
        res = []
        while q:
            r, c = q.popleft()
            res.append(nums[r][c])
            # Only the first column should add the 
            # next row cell (left child if rotated)
            if c == 0 and r + 1 < len(nums):
                q.append((r + 1, c))
            # Adding the right child (if you think about this rotated)
            if c + 1 < len(nums[r]):
                q.append((r, c + 1))
        return res
```


#### Follow Up: *"What about anti-diagonal?"*

```python
def findDiagonalOrder(nums: list[list[int]]) -> list[int]:
    q = deque([])
    q.append((0, 0))
    res = []
    while q:
        level = []
        for _ in range(len(q)):
            r, c = q.popleft()
            level.append(nums[r][c])
            # Only the first column should add the next row cell (left child if rotated)
            if c == 0 and r + 1 < len(nums):
                q.append((r + 1, c))
            # Adding the right child
            if c + 1 < len(nums[r]):
                q.append((r, c + 1))
            res.append(level[::-1])
    return res
```