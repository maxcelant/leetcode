```python
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a dict of sets for rows, cols, and grid squares.
        # This allows us to do a quick look up to see if the 
        # current number is in the set of the given row/col/grid
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".": continue
                if board[r][c] in rows[r]: return False
                if board[r][c] in cols[c]: return False
                if board[r][c] in grids[(r // 3, c // 3)]: return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # There are 9 unique cells,
                # Remember that tuples can be 
                grids[(r // 3, c // 3)].add(board[r][c])

        return True

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
s = Solution()
print(s.isValidSudoku(board))

```