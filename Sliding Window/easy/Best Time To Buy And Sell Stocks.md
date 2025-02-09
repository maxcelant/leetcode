
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l += 1
            res = max(res, (prices[r] - prices[l]))
        return res

s = Solution()
print(s.maxProfit([10, 1, 5, 6, 7, 1]))
```
