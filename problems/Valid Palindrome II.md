---
tags:
  - easy
  - two-pointers
pattern: Traverse string, if no match, check L + 1 and R - 1 versions of match
link: https://neetcode.io/problems/valid-palindrome-ii?list=neetcode250
rating: 4
last_attempt: 2025-09-20
---
#### Problem
You are given a string `s`, return true if the `s` can be a palindrome after deleting at most one character from it.

A **palindrome** is a string that reads the same forward and backward.

**Note:** Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

**Example 1:**

```java
Input: s = "aca"

Output: true
```

Explanation: "aca" is already a palindrome.

**Example 2:**

```java
Input: s = "abbadc"

Output: false
```

Explanation: "abbadc" is not a palindrome and can't be made a palindrome after deleting at most one character.

**Example 3:**

```java
Input: s = "abbda"

Output: true
```

Explanation: "We can delete the character 'd'.

#### Notes
---
- 

#### Code
---

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pali(l + 1, r) or is_pali(l, r - 1)
            l, r = l + 1, r - 1
        return True
        
```
