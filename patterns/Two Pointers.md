Use `l <= r`, when you want to include when `l == r`. This will be important for certain questions in which you don't need to distinct values for a grouping.

Cases:
- 

When you need to merge two lists into one, this is what you usually need to do:

```python
def test(arr1, arr2):
	p1, p2 = 0, 0
	while p1 < len(arr1) and p2 < len(arr2):
		# Do thing
	
	while p1 < len(arr1):
		# Clean up arr 1
	while p2 < len(arr2):
		# Clean up arr 2
```

Cases:
- [[Merge Sorted Arrays]]
- [[Merge Strings Alternatively]]

No always, but usually two pointers problems are used on arrays that are sorted.