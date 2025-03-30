#### Fundamentals
- The idea is that it incrementally builds candidates towards a solution and prunes them when a it is determined that a candidate cannot lead to a valid solution.
- A very small `n` value may indicate a backtracking problem.
- Backtracking problems are usually exhaustive: "Find all X"
- When looking at a backtracking problem, you should think about three things:
	1. What is the target/base case to create leaf nodes?
	2. How do we generate possible children?
	3. (optional) How do I prune bad nodes?
- The non-for loop approach is more intuitive for me.
- I'm saying pruning is optional because there are cases like [[Subsets]] and [[Subsets II]] where we want ALL of the subsets created.
