---
tags:
  - strings
  - medium
pattern: Calculate prefix sum for each cell, subtract the outside left and top cells
link: https://neetcode.io/problems/range-sum-query-2d-immutable?list=neetcode250
rating: 2
last_attempt: 2025-09-07
---
#### Problem
You are given a 2D matrix `matrix`, handle multiple queries of the following type:

- Calculate the `sum` of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.  
    You must design an algorithm where `sumRegion` works on `O(1)` time complexity.

**Example 1:**

```java
Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]

Output: [null, 8, 11, 12]
```

Explanation:  
```
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);  
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)  
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)  
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
```

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use prefix sum to pre-calculate the area of each square.

#### Code
---

```python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        orig = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        # Build the prefix matrix
        # Look at left value and top value
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                # Add prefix for just this row
                # If you try adding to the left value, you'll be dealing with duplicates
                # bc the left value also includes it's top value.
                prefix += orig[r][c]
                top = self.matrix[r][c+1]
                self.matrix[r+1][c+1] = prefix + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        # The actual value of the whole rectangle
        bot_right = self.matrix[r2][c2]

        # The top right corner
        top_right = self.matrix[r1 - 1][c2]

        # The bottom left corner
        bot_left = self.matrix[r2][c1 - 1]

        # We re-add this corner value to undo the duplication of subtraction
        # from removing the bottom left and top right
        top_corner = self.matrix[r1 - 1][c1 - 1]

        return bot_right - top_right - bot_left + top_corner
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- For each row in the new matrix, we should take a fresh prefix value and add to that and not use the existing left value to calculate the new value because that will create overlap.

```
When calculating sum at X:

[A][B][C]
[D][E][F]
[G][H][X]

top = A+B+C+D+E+F (everything above X)
left = A+D+G+B+E+H (everything left of X)

top + left counts the overlap region (A+B+D+E) twice!
```

- Add a buffer around the original matrix to make it easier to deal with out of bounds values.
- We **remove** the value to the outside left and the outside top and re-add the top left outside corner to undo the double subtraction.

>![[Pasted image 20250907095648.png]]

#### Lessons Learned
---
- Use inflated matrix

#### Video Breakdown
---