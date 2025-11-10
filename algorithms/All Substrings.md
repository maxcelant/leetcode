This is used in dynamic programming to find all substrings.

```python
n = len(word)
for diff in range(1, n):
	for i in range(n - diff):
		j = i + diff
		print(s[i:j])
```

```go
n := len(s)
for size := 1; size < n; size++ {
	for i := 0; i < n - size + 1; i++ {
		j := i + size
		fmt.Println(s[i:j])
	}
}
```

`diff`/`size` is the length of the substring, we start at `1` because we don't really care for substrings of length `0` (empty strings). 

```ad-example
For instance, if `diff` was `3`, and the word was `"faux"`, then it would produce strings of length`"fau", "aux"`.
```

We use `range(n - diff)` because we only want substrings of length `diff`. 

```ad-example
If the word was "power" and `diff = 2`, then that would mean `i = {0..3}`, which makes sense because we want `s[i:j]` and `j` should never be out of bounds.

Example:
- `s[0:2]` -> "po"
- `s[1:3]` -> "ow"
- `s[2:4]` -> "we"
- `s[3:5]` -> "er"
```

