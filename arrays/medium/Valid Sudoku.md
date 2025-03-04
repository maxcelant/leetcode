#### Approach
---
- Make a set for each row, col and square. The keys are the actual row/col/square number and the "list" (which is actually a set for quick lookups), is the value.
- Add the value to the correct row/col/square.

#### Code
---

```python
class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Create a set for rows, cols, and squares
    rowSet = defaultdict(set)
    colSet = defaultdict(set)
    squareSet = defaultdict(set)

    rows, cols = len(board), len(board[0])
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == ".": continue
        if ( 
          board[r][c] in rowSet[r] or \
          board[r][c] in colSet[c] or \
          board[r][c] in squareSet[(r // 3, c // 3)]
        ):
          return False

        rowSet[r].add(board[r][c])
        colSet[c].add(board[r][c])
        squareSet[(r // 3, c // 3)].add(board[r][c])
      
    return True
```


#### Where did I go wrong?
---
Forgot that tuples can be used as keys in a dictionary.