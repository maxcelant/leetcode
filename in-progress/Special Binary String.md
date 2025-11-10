---
tags:
  - nvidia
  - hard
link: https://leetcode.com/problems/special-binary-string/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-thirty-days
last_attempt: 2025-11-03
rate:
  - ★
---
#### Variants


#### Problem
**Special binary strings** are binary strings with the following two properties:

- The number of `0`'s is equal to the number of `1`'s.
- Every prefix of the binary string has at least as many `1`'s as `0`'s.

You are given a **special binary** string `s`.

A move consists of choosing two consecutive, non-empty, special substrings of `s`, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return _the lexicographically largest resulting string possible after applying the mentioned operations on the string_.

**Example 1:**

>**Input:** s = "11011000"
**Output:** "11100100"
**Explanation:** The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

**Example 2:**

>**Input:** s = "10"
**Output:** "10"

#### Notes


#### Code
**Time Complexity**:
**Space Complexity**: 

```go

```
