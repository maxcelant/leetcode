#### Intuition
- The idea is that it incrementally builds candidates towards a solution and prunes them when a it is determined that a candidate cannot lead to a valid solution.
- A very small `n` value may indicate a backtracking problem.
- The idea behind the `for` loop approach is that the children of a node
- Backtracking problems are usually exhaustive: "Find all X"
- When looking at a backtracking problem, you should think about three things:
	1. What is the target/base case to create leaf nodes?
	2. How do we generate possible children?
	3. (optional) How do I prune bad nodes?
- The non-for loop approach is more intuitive for me.
- I'm saying pruning is optional because there are cases like [[retry/Subsets]] and [[retry/Subsets II]] where we want ALL of the subsets created.

#### Formatting Tips
- If you are always moving the first value, name the param `start`.
- If you are creating groups and adding them the result, name the param it `subset`.

#### Understanding the For Loop Approach
```python title:"Template for backtracking" 
def dfs(start, subset):
  if is_leaf(start):
    report(subset)
    return
  for edge in get_edges(start, len(input)):
    subset.add(edge)
    dfs(start + 1, subset)
    subset.pop()
```

- The for loop represents all possibilities with the current path as a parent node. 
- Each loop creates a new "edge", with the parent being the current `start_index` 
- Example:
	- We have combination sum, and `arr = [1, 1, 2, 3], target = 4`
	- The code would look like this:

	```python
	def comboSum(arr: List[int], target: int) -> List[int]:
		res = []
		def findTargets(start: int, total: int, subset: List[int]):
			if total == target:
				res.append(subset.copy())
				return
			if total > target:
				return
	
			# This creates all the edges with start
			for i in range(start, len(arr)):
				# This is the parent node being created
				subset.append(arr[i])
				# DFS into first child immediately
				findTargets(i + 1, total + arr[i], subset)
				# Remove the parent
				subset.pop()
		...
	```

	- So you might be able to imagine that when we get to `[1]` as the parent, then the edges become `[1,1], [1,2], and [1,3]`.
	- And since we are doing this DFS style, we would immediately drill into `[1,1]` which would have edges `[1, 1, 2] and [1, 1, 3]`.
	- Note: the reason we do `total + arr[i]` is because we are saying "for these children, the total is already set to X from the parent.", with the parent being `arr[i]`.
	- Picture below will help illustrate.

![[Pasted image 20250331172319.png|Backtracking For Loop Example]]
