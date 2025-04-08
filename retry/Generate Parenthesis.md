---
tags:
  - backtracking
  - medium
---

#### Intuition
---
- Use a DFS type approach, when we need more open parenthesis, we add them, when we need more closed, we add them.
- We do this by calling the function recursively.
#### Code
---

```python

class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		res = []

		def backtrack(open_paren, closed_paren, s):
			if open_paren == n and closed_paren == n:
				res.append(s)
				return

			if open_paren < n:
				backtrack(open_paren + 1, closed_paren, s + "(")
			if closed_paren < n and open_paren > closed_paren:
				backtrack(open_paren, closed_paren + 1, s + ")")

		backtrack(0, 0, "")
		return res
```

#### Insight
---

#### Takeaways
---
- When you are dealing with different permutations of a thing, it's most likely recursion
- You don't actually need to use a stack here. You can just add to the string and that would work.