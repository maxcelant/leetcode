>[!quote]
>Anytime we are tasked with finding the k (or kth) [smallest/largest/etc.] element(s), we should always consider whether the QuickSelect algorithm can be applied

Remember, the goal is quickselect is not to give you the smallest elements in perfect sorted order, just the ones that are definitely the smallest/largest in the set.

There are three parts to the algorithm.
1. Choose a pivot.
2. Swap values around the pivot.
3. Shift left or right pointer inwards.

We **_partition_** our array into two halves. Are pivot is in the center of these two halves. The values in the left partition should all be smaller than the pivot. The right partition should have values larger than the pivot.

If the pivot index is greater than `k`, then we move the right pointer to `pivot - 1`. 

>[!important] Think about it...
>We start by checking the entire array. Now everything _smaller_ than the pivot value should be _before_ the pivot index. So we can confidently move the `right` pointer to `pivot - 1` because those are the elements we care about.

>[!important] Key insight
>If the pivot is larger than `k` (let's say it's `k+N` values), then that tells us that the first `k+N` values are smaller than the `k+Nth` index, but it doesn't tell us anything about the **relative order of those values**, that's why we need to shrink to the left.


![[Pasted image 20251111151228.png]]

On the flip side, if `pivot` index is less than `k`, then we need to move the left pointer. This means that the first `left` values are correctly sorted, but it also means we haven't reached `k` sorted values yet.

#### Partition Breakdown
- `left` and `right` act as our boundaries.
- Our `pivot` is the right most value. 
- As long as `nums[i]` is less than or equal, we will swap it's value with `nums[j]`. This ensures that the smaller values are on the left side.
- At the end we swap `nums[i]` back to it's original and correct spot.

>[!important]
>The idea here is that we want everything `nums[l:i]` to be smaller than the pivot and everything from `nums[i:j]` to be larger or unprocessed.

```python
def quickselect(nums, k):
	pass

def partition(nums, l, r):
	pivot = nums[r] # Choose rightmost value as pivot
	i = l           # Position to put next "<= pivot"
	# Iterate from start of range to end
	for j in range(l, r):
		if nums[j] <= pivot:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
	
	# The pivot is now in the correct spot
	# All values less than it are to the left
	# All greater are to the right
	nums[i], nums[r] = nums[r], nums[i]
	return i
```

