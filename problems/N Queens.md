---
tags:
  - backtracking
  - dfs
  - hard
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Notice that there are going to be a lot of branching sub-paths that will not work, so pruning / backtracking is the best approach.

#### Code
---

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        pos_diag = set() 
        neg_diag = set()

        def solve(r: int):
            # Base case: cur = n
            if r == n:
                copy = [ ''.join(row) for row in board ]
                res.append(copy)
                return
            
            for c in range(n):
                # Ignore 
                if c in cols:
                    continue
                if (r + c) in pos_diag:
                    continue
                if (r - c) in neg_diag:
                    continue

                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add((r + c))
                neg_diag.add((r - c))
                # Move to next row and try all the columns
                solve(r + 1)
                # Backtrack and remove the queen
                cols.remove(c)
                pos_diag.remove((r + c))
                neg_diag.remove((r - c))
                board[r][c] = '.'
        
        solve(0)
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- In order to calculate the positive diagonal and negative diagonal values for the sets, we need to use "slope", `mx+b`, but in this case `m=0`, so it's just `x + b` for positive, and `x - b` for negative, so `r + c` for `posDiag` and `r - c` for `negDiag`.
- Since only one queen should exist on a given row, we can simply just increase the row value on every backtracking dfs call.
- We keep track of each queens `col`, `posDiag`, and `negDiag` to make sure we backtrack if one already exists in that position.
#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**