This algorithm is used to find the maximum/minimum sum/product of a **contiguous subarray**.

```python title:"Finding the max sum"
def kedanes(nums):
	maxsum = nums[0]
	cursum = 0
	for n in nums:
		cursum = max(n, cursum + n)
		maxsum = max(maxsum, cursum)
	return maxsum
```

The important aspect of this relatively simple algorithm is the idea that at every index, we can choose to ignore the previously cached sum, and just take the current value.

>[!example]
If we had `nums = [-3, -1, 5]` and our `cursum = -4`, then why would we want to include that with `5`? It would just be better to ignore the `cursum` and take `5` by itself.

This algorithm has a lot of overlap with [[Sliding Window]].

```python title:"Find the left and right indices for max subarray"
def sliding(nums):
	maxsum = nums[0]
	cursum = 0
	max_indices = (0, 0) # left and right maxes
	
	L = 0
	for R in range(len(nums)):
		# Reset the window
		if cursum < 0:
			cursum = 0
			L = R

		# Add current value to cursum
		cursum += nums[R]
		# Recalculate the max sum
		if cursum > maxsum:
			# Update the left and right indices.
			max_indices = (L, R)
			maxsum = cursum
	
	return max_indices
		
```
#### Problems
- [[Maximum Product Subarray]]