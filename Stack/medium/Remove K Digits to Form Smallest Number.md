#### Approach
---
- We want to use an increasing stack, and pop the higher elements when we find a smaller one!
#### Code
---

```python
def removeKdigits(num: str, k: int) -> str:
	stack = []
	for n in num:
		while stack and k > 0 and n <= stack[-1]:
			stack.pop()
			k -= 1
		stack.append(n)

	# If we have any removals left, remove them from the end.
	while k > 0 and stack:
		stack.pop()
		k -= 1

	# Strip off any leading zeros.
	return "".join(stack.lstrip("0"))
```


#### Where did I go wrong?
---
- `lstrip` is helpful.
- Instead  of using a separate variable to keep track of removals, just decrement `k` itself is cleaner.
- Don't forget edge-cases.