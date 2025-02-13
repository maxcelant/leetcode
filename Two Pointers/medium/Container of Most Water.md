
```python
'''
- The volume of the water will be the diff between the pointers X the min of the two heights
'''


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            diff = r - l
            area = diff * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

s = Solution()
print(s.maxArea([1,7,2,5,4,7,3,6]))
```
