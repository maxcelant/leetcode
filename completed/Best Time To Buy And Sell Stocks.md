---
tags:
  - sliding-window
  - easy
  - nvidia
pattern: if right pointer is smaller than left, move pointer forward, calc max of cur and max
last_attempt: 2025-09-21
link: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode250
rate:
  - ★★★★★
---
#### Problem
You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the `ith` day.

You may choose a **single day** to buy one NeetCoin and choose a **different day in the future** to sell it.

Return the maximum profit you can achieve. You may choose to **not make any transactions**, in which case the profit would be `0`.

**Example 1:**

```java
Input: prices = [10,1,5,6,7,1]

Output: 6
```

Explanation: Buy `prices[1]` and sell `prices[4]`, `profit = 7 - 1 = 6`.

**Example 2:**

```java
Input: prices = [10,8,7,5,2]

Output: 0
```

Explanation: No profitable transactions can be made, thus the max profit is 0.

#### Notes
---

#### Code
---

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res
```

```go
func maxProfit(prices []int) int {
    res := 0
    l := 0
    for r, _ := range prices {
        if prices[r] < prices[l] {
            l = r
        }
        res = max(res, prices[r] - prices[l])
    }
    return res
}
```