#### Fundamentals
- The idea is that it incrementally builds candidates towards a solution and abandons them when a it is determined that a candidate cannot lead to a valid solution.
- The boilerplate looks like the following:
```python
function dfs(start_index, path):
  if is_leaf(start_index):
    report(path)
    return
  for edge in get_edges(start_index):
    path.add(edge)
    dfs(start_index + 1, path)
    path.pop()
```
- A very small `n` value may indicate a backtracking problem.
- 
- Backtracking problems are usually exhaustive: "Find all X"
- When looking at a backtracking problem, you should think about three things:
	1. What is the target/end goal?
	2. How do we generate possible children?
	3. How do I prune bad nodes?