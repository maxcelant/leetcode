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

#### Code
**Time Complexity**: O(N^2)
**Space Complexity**: O(N^2)

```python
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
		if k == 0:
			return self.isPalindrome(0, len(s) - 1)
		
		dp = {}
		def find(l, r, k):
			if (l, r, k) in dp:
				return dp[(l, r, k)]
			
			if k == 0:
				dp[(l, r, k)] = self.isPalindrome(l, r)
				return dp[(l, r, k)]
			
			while l < r:
				if self.s[l] != self.s[r]:
					dp[(l,r,k)] = find(l + 1, r, k - 1) or find(l, r - 1, k -1)
					
				l, r = l + 1, r - 1
		
	def isPalindrome(l, r) -> bool:
		while l < r:
			if self.s[l] != self.s[r]:
				return False
			l, r = l + 1, r - 1
		return True
```