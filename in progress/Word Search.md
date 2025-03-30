---
tags:
  - backtracking
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use backtracking to go down a path, when a letter is wrong, backtrack
- **Base Case:** current is equal to length of `word`
	- This means we have "finished" the word
- **Possible Paths:**
	- `board[r][c] == word[current]`, so we increment current and continue
	- `board[r][c] != word[current]`, so we backtrack, we keep `current` the same and we try a different direction.

#### Code
---
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0,-1], [1,0], [-1,0]]
        visited = set()
        def path_found(r: int, c: int, curr: int):
            if curr == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[curr] or (r, c) in visited):
                return False
            
            visited.add((r,c))
            for dx, dy in directions:
                if path_found(r + dx, c + dy, curr + 1):
                    return True
            visited.remove((r,c))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if path_found(r, c, 0):
                    return True
        return False
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- For each row, col we need to potentially run dfs on it.
- We use `curr` to keep track of which letter we want from the word.
- If a path ends up being wrong, we simply return and try a different path.
- Keep doing this until we get to the base case which means `curr` has reached the last letter and it's correct!

#### Takeaways
---
**Where did I go wrong?**
- I wasn't using a visited set to keep track of directions i've already gone.
- I didn't correctly organize the pruning condition.
**Lessons Learned?**