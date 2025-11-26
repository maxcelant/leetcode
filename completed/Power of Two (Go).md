---
tags:
  - nvidia
  - bitwise
  - easy
link: https://leetcode.com/problems/power-of-two/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-10-30
rate:
  - ★★★
---
#### Variants


#### Problem
Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

**Example 1:**

**Input:** n = 1
**Output:** true
**Explanation:** 20 = 1

**Example 2:**

**Input:** n = 16
**Output:** true
**Explanation:** 24 = 16

#### Notes
The idea is that if you do `n & -n` then you should get `n` if it's a power of two because it only has single 1 bit e.g. `0010`.

**Example (Success)**
1. Take `n = 0010`
2. 2's complement, first inverse the bits `n = 1101`
3. Then add 1, `n = 1110`.
4. AND them, `0010 & 1110 = 0010`. Which means 2 is a power of 2!

**Example (Fail)**
1. Take `n = 0110`
2. 2's complement, first inverse the bits `n = 1001`
3. Add 1, `n = 1010`
4. AND them, `0110 & 1010 = 0010`, which does not match `n`.

#### Code
**Time Complexity**:
**Space Complexity**: 

```go
func isPowerOfTwo(n int) bool {
    if n == 0 { return false }
    if n == 1 { return true }
    return n & -n == n
}
```


#### Follow Up: *""*

```python

```