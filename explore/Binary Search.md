Using  `l <= r` means that we want to continue even when `l` and `r` are equal. So that means that `l` needs to be strictly larger than `r` for the loop to end.

>[!question]
What does this means when `len(arr) == 1`?

There are three primary sections:
1. Sort (if not sorted).
2. Loop and cut search space in half.
3. Determine viable candidates in remaining space.

#### Binary Search Template I

```python
def search(nums: list[int], target: int) -> int:
	if len(nums) == 0: 
		return -1
	l, r = 0, len(nums) - 1
	while l <= r:
		m = l + (r - l) // 2
		if nums[m] == target:
			return m
		if nums[m] < target:
			l = m + 1
		else:
			r = m - 1
	return -1
```

##### Problem 1: Sqrt(x)
Given a non-negative integer `x`, return _the square root of_ `x` _rounded down to the nearest integer_. The returned integer should be **non-negative** as well.

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            if m**2 == x:
                return m
            if m**2 > x:
                r = m - 1
            else:
                l = m + 1
        return r
```

##### Problem 2: Guess Number
We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
- `1`: Your guess is lower than the number I picked (i.e. `num < pick`).
- `0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return _the number that I picked_.
```python
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = l + (r - l) // 2
            res = guess(m)
            if res == 0:
                return m
            if res == 1:
                l = m + 1
            else:
                r = m - 1
        return -1
```

##### 