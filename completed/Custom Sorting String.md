---
tags:
  - meta
  - medium
  - hashing
link: https://leetcode.com/problems/custom-sort-string/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-14
rate:
  - ★★★
---
#### Problem
You are given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return _any permutation of_ `s` _that satisfies this property_.

**Example 1:**
>**Input:** order = "cba", s = "acbacad"
**Output:** "ccbaaad"

#### Notes
---
The idea is pretty straight forward. Since they give us the `order`, we can simply use a frequency table to figure out how many of each letter we need to add so that the string will be in the correct order according to `order`. 

In other words, they literally give you the answer, you just need to input how many times each letter appears.

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
		# Get the frequency of all the characters in the string
        freqs = Counter(s)
        res = []
		# Go through the order and amount of that letter according to the frequency
        for char in order:
            res.append(char * freqs[char])
            del freqs[char]

		# Attach any remaining unaccounted letters to the end
        for char, freq in freqs.items():
            res.append(char * freq)
        return ''.join(res)
```


#### Follow Up: *""*

```python

```