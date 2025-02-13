#### Approach
---
- Add values to the stack.
- When you see an operator, pop the top two from the stack and perform the operation which was found.
- Add that value back into the stack.
- Do this until all tokens are expended.

#### Pseudocode
---
```
CREATE stack []
CREATE operand (+,-,/,*)
FOR value IN input
	IF value is NOT operand
		THEN push onto stack
	IF value is operand
		THEN 
			pop left value from stack
			pop right value from stack
			calculate left (operand) right
			push result onto stack
RETURN stack[0]
```

#### Code
---

```python
class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		operands = {'*', '/', '+', '-'}
		for t in tokens:
			if t not in operands:
				stack.append(int(t))
				continue
			right = stack.pop()
			left = stack.pop()
			if t == '*':
				stack.append(left * right)
			elif t == '/':
				stack.append(int(float(left / right)))
			elif t == '+':
				stack.append(left + right)
			else:
				stack.append(left - right)
		return stack[0]
```


#### Post-Attempt Thoughts
---
- Since the stack is in reverse order to the input array. When we pop, the first value will actually be the right value, and then the left.