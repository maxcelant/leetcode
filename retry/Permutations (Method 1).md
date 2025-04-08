---
tags:
  - backtracking
  - dfs
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- New permutations can be created by inserting the current element in all postions of the existing permutations!

#### Code
---

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(start):
	        # base case, we build from the bottom
            if start == len(nums):
                return [[]]
            
            perms = dfs(start + 1)
            new_perms = []
            # Loop through existing permutations
            for perm in perms:
	            # Add the current element at all
	            # positions for this permutation
                for i in range(len(perm) + 1):
                    c = perm.copy()
                    c.insert(i, nums[start])
                    new_perms.append(c)
            return new_perms
        
        return dfs(0)
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- The idea is that we build it permutations from the bottom up.
- At each step, we split the list by exluding the first element
- We do this until we hit the base case, which is NO elements in the list
- From there, we create the permutations by taking the previous permutations and simply inserting the current element (`nums[0]`) in all of the locations it can go.
	- For example: if current element is 3, and the permutations are `[0, 1], [1, 0]`, then it will become `[3,0,1],[0,3,1],[0,1,3]`.
- Since we also add the element to the end, we need to make sure that our loop accounts for that
- **Note:** for EACH permutation, there are `len(perm)` number of positions to place the new element.
	- So for N values in the existing permutation, it will create N! permutations.
- We continue to propagate the updated permutations up to the parent.

#### Takeaways
---
**Where did I go wrong?**

**Lessons Learned?**