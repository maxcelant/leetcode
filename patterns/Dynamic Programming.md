#### Intuition
- What is the subproblem? 
	- Try to think creatively here because the subproblem isn't always obvious.
	- Think in terms of, "What is a smaller solution of the problem look like? What changes?"
- What is the base case for the problem?
- Is there any sort of initialization I need to perform on the DP table?
- How can I use that subproblem to get the final solution?
- In iterative solutions, we typically want to get `N+1` locations and set the `0-th` position to a default—this is the placeholder for empty sets which are typically "true"/the equivalent for a given problem.

#### Advice
- Usually the return type is equal to the type of DP table you need to create.
- In scenarios where you have two values you are keeping track of—one that is `N-1` and the other that is `N-2`, I think naming them `prev` and `prevprev` is a clear approach.
	- **Examples:**
		- [[Climbing Stairs]]
		- [[House Robber]]
		- [[House Robber II]]
- Looping through all possible substrings.
- If possible, use the dp template for a recursive bottom up approach.
	- **Examples:**
		- [[Decode Ways]]
		- [[Coin Change]]
		- [[Word Break]]

#### Templates(s)
- From this [video](https://youtu.be/ccYOPENsvU0?si=b0I5-N29kItcAvBE)

**Recursive Template**
```python
def func(n):
	dp = {}

	def dfs(i):
		# Base case (out of bounds)
		if i == n:
			return 0
		# Base case (in cache)
		if i in dp:
			return dp[i]

		# Recursive case
		option1 = dfs(i + 1)
        option2 = dfs(i + 2)
        
        # Choose the best option (min/max depending on the problem)
        dp[i] = min(option1, option2)  # or max(), or option1 + value[i], etc.
        return dp[i]
		
    return dfs(n)
```

**Iterative Template**

```python
def func(n):
    # Initialize DP array with base cases
    dp = [0] * (n + 1)
    
    # Set base cases explicitly
    dp[0] = 0  # or some other value depending on the problem
    # dp[1] = ...  # Optional, based on the problem

    # Build up the solution from smaller to larger subproblems
    for i in range(1, n + 1):
        # Compute dp[i] based on previous states
        option1 = dp[i - 1]
        option2 = dp[i - 2] if i - 2 >= 0 else float('inf')  # or 0, depending on the problem

        dp[i] = min(option1, option2)  # or max(), sum, etc.
    
    return dp[n]

```