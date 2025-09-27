#### Intuition
---
- the edges can't contain any water. Just start at 1 and N - 1
- keep track of max on left and right
- the amount of water at a specific column is the min of the maxes (from L and R) - the current height
- if its negative, just ignore it basically
- move up the smaller of the two
#### Code
---
```python
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r] 
        res = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                area = min(max_right, max_left) - height[l]
                if area > 0: res += area
            else:
                r -= 1
                max_right = max(max_right, height[r])
                area = min(max_right, max_left) - height[r]
                if area > 0: res += area
        return res
```

#### Insight
---
- 

#### Takeaways
---
- **Where did I go wrong?**
- **Lessons Learned?**
- **Aha Moments?**

#### Insight
---
