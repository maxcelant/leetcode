---
tags:
  - meta
  - easy
  - two-pointers
link: https://leetcode.com/problems/valid-word-abbreviation/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-27
rate:
  - ★★★★
---
#### Problem
A string can be **abbreviated** by replacing any number of **non-adjacent**, **non-empty** substrings with their lengths. The lengths **should not** have leading zeros.

For example, a string such as `"substitution"` could be abbreviated as (but not limited to):

- `"s10n"` (`"s ubstitutio n"`)
- `"sub4u4"` (`"sub stit u tion"`)
- `"12"` (`"substitution"`)
- `"su3i1u2on"` (`"su bst i t u ti on"`)
- `"substitution"` (no substrings replaced)

The following are **not valid** abbreviations:

- `"s55n"` (`"s ubsti tutio n"`, the replaced substrings are adjacent)
- `"s010n"` (has leading zeros)
- `"s0ubstitution"` (replaces an empty substring)

Given a string `word` and an abbreviation `abbr`, return _whether the string **matches** the given abbreviation_.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

**Example 1:**

>**Input:** word = "internationalization", abbr = "i12iz4n"
**Output:** true
**Explanation:** The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

#### Notes
---
The general idea is simple. Have a pointer for each word. Move `p` (pointer for `abbr`) along and when you find a number, evaluate it and move `q` that amount.

This problem is a little annoying with edge cases. Here are some good pointers:
1. You either create the number OR evaluate the current char—not both.
2. At the end, you ensure that the pointers both point to the end of their respective words.

#### Code
---

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p = q = 0
        while p < len(abbr) and q < len(word):
            if abbr[p].isnumeric():
                if abbr[p] == "0":
                    return False
                num = 0
                while p < len(abbr) and abbr[p].isnumeric():
                    num = num * 10 + int(abbr[p])
                    p += 1
                q += num
            else:
                if abbr[p] != word[q]:
                    return False
                p += 1
                q += 1
        return p == len(abbr) and q == len(word)
```
