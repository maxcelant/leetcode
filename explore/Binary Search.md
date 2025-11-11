#### Use Cases
**1. When data is sorted or can be made sorted**
- Find `x` in a sorted array
**2. When you need to find the first or last occurrence of something**
- First occurrence of a number
- Last occurrence
- First index where a condition becomes true
**3. You need to minimize or maximize something (answer lies in a range)**
- Minimum speed to arrive on time
- Smallest radius to cover all points
- Maximum value that satisfies a condition
**4. When the search space is huge**
- Dead give away. Linear solutions won't work.

Using  `l <= r` means that we want to continue even when `l` and `r` are equal. So that means that `l` needs to be strictly larger than `r` for the loop to end.

>[!question]
What does this means when `len(arr) == 1`?

There are three primary sections:
1. Sort (if not sorted).
2. Loop and cut search space in half.
3. Determine viable candidates in remaining space.

#### Binary Search Template I
With this template we are typically looking for a target value.
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

##### Problem 3: Search in Rotated Sorted Array

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
```

#### Binary Template II
The idea with this template is that we aren't looking for a specific value per se, we are finding the _lower boundary_.

This is important in situations where moving the right pointer _past the middle_ could mean you miss the correct value.

```python
def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left
    return -1
```

##### Problem 1: First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
```

##### Problem 2: Find Peak Element
- [[Find Peak Element]]
##### Problem 3: Find Minimum in Sorted Array
- [[Find Minimum in Rotated Sorted Array]]


#### Template Analysis
Templates II and III are used when you need to look at the neighbors of the left and right pointers.

