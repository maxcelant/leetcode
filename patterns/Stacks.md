#### Fundamentals


#### Helpful Tidbits
- Monotonic stacks want to maintain a certain order. For decreasing stacks, the top element always needs to be the smallest, so it will kick out any bigger ones.

#### Boilerplate
##### Monotonic Increasing Stack
- Two things need to be true:
	1. The stack needs to always be increasing.
	2. The current element always needs to be added to the stack.
- So if the current element is just bigger than the top of the stack, then we simply add it.
- If it's smaller, we continue to pop until all larger elements are removed.

```python
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
	    # pop elements bigger than num
        while stack and num < stack[-1]:
            stack.pop()
        stack.append(num)
    return ans

fn([5, 6, 3, 2, 1, 8])

'''
[5]
[5,6]
[3]
[2]
[1]
[1,8]
'''
```

