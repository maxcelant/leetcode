#### Intuition
- What is the subproblem?
- What is the base case for the problem?
- Is there any sort of initialization I need to perform on the DP table?
- How can I use that subproblem to get the final solution?

#### Helpful Tidbits
- In scenarios where you have two values you are keeping track of—one that is `N-1` and the other that is `N-2`, I think naming them `prev` and `prevprev` is a clear approach.
	- Examples:
		- [[House Robber]]
		- [[House Robber II]]
- Looping through all possible substrings.