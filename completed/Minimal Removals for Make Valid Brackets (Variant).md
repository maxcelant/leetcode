---
tags:
  - meta
  - medium
  - strings
  - variant
link:
last_attempt: 2025-11-02
rate:
  - ★★★★
---
#### Variants
- [[Minimum Remove To Make Valid Parenthesis]]
- [[Minimum Add to Make Parentheses Valid]]

#### Problem
It's a variant of the above mentioned but now you have all three enclosing bracket types: `{}`, `()`, `[]`.

#### Notes
Use a map to recall the open parens of each kind. Use a map to map between the open and close brackets.

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
def minimum_removals(s: str) -> str:
    pairs = { '{': '}', '(':')', '[':']'}
    open_counts = {']': 0, ')': 0, '}': 0}
    res = []
    for c in s:
        if c in pairs:
            open_counts[pairs[c]] += 1
            res.append(c)
        elif c in pairs.values():
            if open_counts[c] > 0:
                res.append(c)
                open_counts[c] -= 1
        else:
            res.append(c)
        
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        if c in pairs:
            if open_counts[pairs[c]] > 0:
                res.pop(i)
                open_counts[pairs[c]] -= 1
    
    return ''.join(res)
```
