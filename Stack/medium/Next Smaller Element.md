#### Approach
---
-  I think we are going to need a monotonic increasing stack for this
- I don't want the difference in index positions, i just want to index of the next smaller element.
- So i just need to store the index position of that element, not the element itself.

#### Code
---

```python
def nextSmallerElement(nums):
	res = [-1] * len(nums)
	stack = []
	for i in range(len(nums)):
		while stack and nums[i] < nums[stack[-1]]:
			j = stack.pop()
			res[j] = nums[i]
		stack.append(i)
	return res
```


#### Where did I go wrong?
---
- 