---
tags:
  - backtracking
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We want the position (`pos`) to be updated every time we call to "move" to the next digit grouping in the input string
- **Base Case:** Our position reaches the same length as the input digit.
- **Branching Paths:** We add the next character for that grouping to the string.

#### Code
---

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }

        def dfs(pos: int, subset: str):
            if pos == len(digits):
                res.append(subset)
                return

            for c in digit_to_char[digits[pos]]:
                dfs(pos + 1, subset + c)
        if digits:
            dfs(0, '')
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We loop through each letter in that grouping, and we recursively call to the next grouping. The image helps drive this point home.

![[Pasted image 20250402151939.png|Finding all subsets]]

#### Takeaways
---
**Where did I go wrong?**
- I was unsure how to structure the recursive nature of the problem.
**Lessons Learned?**
- If i notice that the tree created from the problem very obviously has a "looping through all the elements for a given subtree" then i should know a for loop is the way to go. 