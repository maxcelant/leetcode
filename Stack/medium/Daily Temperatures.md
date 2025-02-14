#### Approach
---
- Honestly I was completely lost on how to approach this problem.
- This is definitely one to retry later.

#### Code
---
```python
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		stack = []
		# We need to pre-fill this so we can later update them.
		res = [0] * len(temperatures)
		for i, temp in enumerate(temperatures):
			# If the current temperature is greater than the top of the stack
			# Then we will continously pop until we hit a value larger than current
			while stack and temp > stack[len(stack) - 1][1]:
				j, _ = stack.pop()
				res[j] = i - j
			# No matter what, we add the value to the stack
            # We just need to do so once when we can guarentee that it's the smallest
			stack.append((i, temp))  
		return res	
```
#### Post-Attempt Thoughts
---
- Add values to the stack. 
- When a value that is found is greater than the top of the stack, we pop the top and get the diff.
- We place that output of that diff at the index of the popped value.
	- **important:** We will do this until the top of the stack is _greater_ than the current value.
- The stack will always be in monotonic decreasing order.
	- `(top) 1, 2, 3, 4, 5 (bottom)`
- If a value is smaller than the current top of the stack, we simply add it to the top of the stack.