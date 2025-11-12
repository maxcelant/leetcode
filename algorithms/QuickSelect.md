>[!quote]
>Anytime we are tasked with finding the k (or kth) [smallest/largest/etc.] element(s), we should always consider whether the QuickSelect algorithm can be applied

Remember, the goal is quickselect is not to give you the smallest elements in perfect sorted order, just the ones that are definitely the smallest/largest in the set.

There are three parts to the algorithm.
1. Choose a pivot.
2. Swap values around the pivot.
3. Shift left or right pointer inwards.

```python

class QuickSelect:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def select(self):
        l, r = 0, len(self.arr) - 1
        pivot_index = len(self.arr)
        while pivot_index != self.k:
            pivot_index = self.partition(l, r)
            # If the pivot is too high, shift the right pointer to the left
            if pivot_index > self.k:
                r = pivot_index - 1
            # The pivot is too low, move the left pointer to the right
            else:
                l = pivot_index
        return self.arr[:self.k]

    def partition(self, l, r):
	    # Choose pivot in the middle
        pivot_val = self.arr[l + (r - l) // 2]
        while l < r:
	        # if the left value is smaller than the pivot, just shift left ptr
            if self.arr[l] < pivot_val:
                l += 1
            else:
	            # if left value is larger, swap left and right ptrs
                self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
                r -= 1
		
		# Handle when l == r, shift the left ptr if its larger than pivot
        if self.arr[l] < pivot_val:
            l += 1

        # Return l as the new pivot because we know the first l
        # values are less than the pivot
        return l
        
qs = QuickSelect(arr=[3, 7, 2, 4, 6, 8, 10], k=3)
print(qs.select()) # [3,2,4]
```

We **_partition_** our array into two halves. Are pivot is in the center of these two halves. The values in the left partition should all be smaller than the pivot. The right partition should have values larger than the pivot.

If the pivot index is greater than `k`, then we move the right pointer to `pivot - 1`. 

>[!important] Think about it...
>We start by checking the entire array. Now everything _smaller_ than the pivot value should be _before_ the pivot index. So we can confidently move the `right` pointer to `pivot - 1` because those are the elements we care about.

>[!important] Key insight
>If the pivot is larger than `k` (let's say it's `k+N` values), then that tells us that the first `k+N` values are smaller than the `k+Nth` index, but it doesn't tell us anything about the **relative order of those values**, that's why we need to shrink to the left.


![[Pasted image 20251111151228.png]]

On the flip side, if `pivot` index is less than `k`, then we need to move the left pointer. This means that the first `left` values are correctly sorted, but it also means we haven't reached `k` sorted values yet.

