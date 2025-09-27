---
tags:
  - greedy
  - medium
---

#### Intuition
---
- Integer conversions usually involve some division/modulo work.
- Use `divmod` or write by hand.

#### Code
---

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        ]
        res = []   
        for symbol, value in numerals:
            count = num // value
            num = num % value
            res.append(symbol * count)
        return "".join(res)
```

#### Insight
---
- With this greedy approach, we start from the highest roman numeral (`M`) and work our way down. 
- On each iteration of the loop, we divide by roman numeral digit and keep both the quotient and remainder.
- The quotient acts as our "count", and the remainder is our "new" total.
	- Example: `309 // 100 -> count: 3, remainder: 9`

#### Takeaways
---
- **Where did I go wrong?**
	- I was trying to start from the bottom and going up.
	- I wasn't sure how to connect the roman numerals to the values I was getting.
	- I think the hardest part is going to remember to add those subtractive symbols to the greedy list.
- **Lessons Learned?**
	- Using the quotient and remainder pair gives me what I need.
	- The quotient represents _how many times_ the symbol is added.
	- I should account for symbols like `CM` and `IX`, which represent the subtractive symbols.
		- We don't create about the additive symbols `VI` because those will be picked up by the greedy list.
> ![[Pasted image 20250305150757.png|500]]
- **Aha Moments?**