---
tags:
  - hard
  - meta
  - 2d-dynamic-programming
link: https://leetcode.com/problems/valid-palindrome-iii/description/
last_attempt: 2025-10-29
rate:
  - ★★★
---
#### Variants
- [[Valid Palindrome]]
- [[Valid Palindrome II]]

#### Problem
Given a string `s` and an integer `k`, return `true` if `s` is a `k`**-palindrome**.

A string is `k`**-palindrome** if it can be transformed into a palindrome by removing at most `k` characters from it.

**Example 1:**

**Input:** s = "abcdeca", k = 2
**Output:** true
**Explanation:** Remove 'b' and 'e' characters.

**Example 2:**

**Input:** s = "abbababa", k = 1
**Output:** true

#### Notes
Each cell is a subproblem that represents the number of letters that don't match _so far_. Once we get to the final cell, `i == j`, then we that will tell us the _least amount of changes_ to make a valid palindrome. If that value is over `k`, then we know we can't create a valid palindrome with `k` changes.

#### Code
**Time Complexity**: O(N^2)
**Space Complexity**: O(N^2)

```python
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        
        def find_k(i: int, j: int) -> int:
            # Base case, only 1 letter remaining
            if i == j:
                return 0
            
            # Base case 2: two letters remaining
            if i == j - 1:
                return s[i] != s[j]

            # Avoid doing extra work if we already computed it
            if memo[i][j] != -1:
                return memo[i][j]
            
            # The letters match so we don't add anything to the cell
            if s[i] == s[j]:
                memo[i][j] = find_k(i + 1, j - 1)
                return memo[i][j]
            
            # Since they don't match, we add one to the cell and
            # Check the palindrome shifting the left by one and right by one
            # in separate subtrees.
            # We take the min of the two + 1
            memo[i][j] = 1 + min(find_k(i + 1, j), find_k(i, j - 1))
            return memo[i][j]
        
        return find_k(0, len(s) - 1) <= k
```


#### Follow Up: *""*

```python

```