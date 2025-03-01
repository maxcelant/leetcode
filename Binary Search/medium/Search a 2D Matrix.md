#### Approach
---
- If the value is larger than the right-most value in a column, increment column by 1
- If the value is smaller than the left-most value in a column, decrement column by 1.
- If the value is within the confines of this row, use binary search to find it.

#### Code
---

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # Find the row that has the target
        top, bot = 0, m - 1
        row = []
        while top <= bot:
            m = top + ((bot - top) // 2)
            # If the target is GREATER than the biggest value on this row
            if target > matrix[m][-1]:
                # move down
                top = m + 1
            # If the target is LESS than the smallest value on this row
            elif target < matrix[m][0]:
                # move up
                bot = m - 1
            else:
                # Store the correct row 
                row = matrix[m]
                break
        
        # Edge case: if we can't find the correct row, return False
        if top > bot or bot < top:
            return False

        # Find the target using plain binary search
        l, r = 0, n - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target == row[m]:
                return True
            elif target > row[m]:
                l = m + 1
            else:
                r = m - 1

        return False
     

```


#### Post-Attempt Thoughts
---
- The key to this problem is to use binary search to find the correct row, then using it again to find the correct value.