- When you need to merge two lists into one, this is what you usually need to do:

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