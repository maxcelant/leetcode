---
tags:
  - meta
  - stack
  - medium
link: https://leetcode.com/problems/simplify-path/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 4
last_attempt: 2025-10-09
rate:
  - ★★★★
---
#### Problem
You are given an _absolute_ path for a Unix-style file system, which always begins with a slash `'/'`. Your task is to transform this absolute path into its **simplified canonical path**.

The _rules_ of a Unix-style file system are as follows:

- A single period `'.'` represents the current directory.
- A double period `'..'` represents the previous/parent directory.
- Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single slash `'/'`.
- Any sequence of periods that does **not match** the rules above should be treated as a **valid directory or** **file** **name**. For example, `'...'` and `'....'` are valid directory or file names.

The simplified canonical path should follow these _rules_:

- The path must start with a single slash `'/'`.
- Directories within the path must be separated by exactly one slash `'/'`.
- The path must not end with a slash `'/'`, unless it is the root directory.
- The path must not have any single or double periods (`'.'` and `'..'`) used to denote current or parent directories.

Return the **simplified canonical path**.

**Example 1:**
```
**Input:** path = "/home/"

**Output:** "/home"
```

**Explanation:**

The trailing slash should be removed.

#### Notes
---
The idea stems from thinking of the file system path as a stack. Any time we do a `..`, we want to move back to the parent dir. This is equivalent to popping from the stack of directories.

The end is some edge case handling

#### Code
---

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for c in path.split("/"):
	        # If it's an empty space or single dot, we simply skip
            if c == "": continue
            if c == ".": continue
			# In this case, we pop from the stack because we are going
			# out one dir
            if c == ".." and stack:
                stack.pop()
			# if the stack is empty, then we are already at the root
            elif c == ".." and not stack:
                continue
			# In all other cases, we simply append to the stack
            else:
                stack.append(c)
        res = "/".join(stack)
        if len(res) > 1 and res[-1] == "/":
            res = res[:-1]
        res = f'/{res}'
        return res if stack else "/"
```
