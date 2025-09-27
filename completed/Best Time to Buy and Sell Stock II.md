---
tags:
  - greedy
  - medium
pattern: Iterate thru list, add the diff to a result variable
link: https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii?list=neetcode250
rating: 3
last_attempt: 2025-09-15
---
#### Problem
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the **same day**. Also, you are allowed to perform any number of transactions but can hold **at most one** share of the stock at any time.

Find and return the **maximum** profit you can achieve.

**Example 1:**

```java
Input: prices = [7,1,5,3,6,4]

Output: 7
```

Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

**Example 2:**

```java
Input: prices = [1,2,3,4,5]

Output: 4
```

Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

#### Notes
---
- If the next number is larger than the current number, add the diff to a `result` variable.

#### Code
---

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += (prices[i] - prices[i - 1])
        return res
```
