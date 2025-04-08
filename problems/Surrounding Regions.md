---
tags:
  - graphs
  - dfs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Capture everything except the un-surrounded regions.
- Find all the cells that can't be captured and note them, everything else will turn into an 'X'.

#### Code
---

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

		# DFS on all the bordering 'O' to find the unsurrounded cells
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            
            if board[r][c] != 'O':
                return
            
            board[r][c] = 'T' # Convert any 'O' to 'T'
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        # Search the top and bottom borders for any '0' and run DFS from it
        # Since these cells and any border '0' will be unsurrounded
        # row = 0, c = 0..M
        # row = N-1, c = 0..M
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)
        
        # Search the left and rigth borders for the same reason
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)
        
        # Turn all the remaning 'O' to 'X', since they are technically surrounded!
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We only want to run DFS on nodes on the borders that are `O`, since those we know for sure are un-surroundable.
- Any nodes that are `O` attached to those we know for sure are also unsurrounded.

#### Takeaways
---
**Where did I go wrong?**
- I had to think in reverse. Instead of finding all the surrounded cells, I should've thought "capture all EXCEPT the un-surrounded"
**Lessons Learned?**