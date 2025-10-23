Boundary-based binary search is when you aren't looking for the middle value. You simply want to figure out the lower bound when the `left ` and `right` pointers cross.

#### Lower Boundary Binary Search
If we want to find the lower boundary, then we need to move the right pointer when the target is LESS THAN OR EQUAL TO. We are giving the right pointer more power because it includes the EQUALS.

The lower bound will be the right pointer when the pointers meet.

```python
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
l, r = 0, len(arr) - 1
t = 8

while l <= r: # Because we want to make sure they pass each other!
    m = l + (r - l) // 2
    if t <= arr[m]:
        r = m - 1
    else:
        l = m + 1
print(r) # index 3, value 7
```

**Side note about the left bias**:
Because we do `m = l + (r - l) // 2`, we always round down the number. Which means that if you do:

```python
if t > m:
	l = m
else:
	r = m
```

You will cause an infinite loop! To avoid this, always do `l = m + 1`.