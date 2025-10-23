---
tags:
  - stack
  - meta
  - medium
link: https://leetcode.com/problems/buildings-with-an-ocean-view/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-19
rate:
  - ★★★★
---
#### Problem
There are `n` buildings in a line. You are given an integer array `heights` of size `n` that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a **smaller** height.

Return a list of indices **(0-indexed)** of buildings that have an ocean view, sorted in increasing order.

**Example 1:**

>**Input:** heights = [4,2,3,1]
**Output:** [0,2,3]
**Explanation:** Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

**Example 2:**

>**Input:** heights = [4,3,2,1]
**Output:** [0,1,2,3]
**Explanation:** All the buildings have an ocean view.

#### Notes
---
Since the ocean is facing the right, we can start from the right side of the array. As we go left, we keep track of the max height so far in a `stack`.

![[Pasted image 20251019110408.png]]

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        stack = []
        for i, height in enumerate(reversed(heights)):
            if not stack:
                stack.append(height)
                res.append(len(heights) - 1 - i)
                continue
            if height > stack[-1]:
                res.append(len(heights) - 1 - i)
            stack.append(max(stack[-1], height))
        return res[::-1]
```


#### Follow Up: *"Can you use O(1) space?"*

```python
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxHeight = -1 
        for i, height in enumerate(reversed(heights)):
            if maxHeight == -1:
                maxHeight = height
                res.append(len(heights) - 1 - i)
                continue
            if height > maxHeight:
                res.append(len(heights) - 1 - i)
                maxHeight = height
        return res[::-1]
```