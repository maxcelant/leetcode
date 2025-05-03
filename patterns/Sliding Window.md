#### Intuition
- Find out the condition to move the left pointer forward to the right's position or shrinking the window by 1
- Usually that condition will be:
	1. Window size is too large.
	2. Something is in the window that shouldn't be.
	3. The value of the left pointer is made invalid in some way.

#### Helpful Tidbits
- Typically sliding window problems will include a `Counter`, `Dict`, or `Set`. Since they typically need to store some information about frequencies, or about what's inside in the window.

#### Boilerplate

```python
def func(s):
	l = 0
	for r in range(len(s)):
		if (SOME CONDITION):
			l = r

def func(s):
	l = 0
	for r in range(len(s)):
		if (SOME CONDITION)
			l += 1
```