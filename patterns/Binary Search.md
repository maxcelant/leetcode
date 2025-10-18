- Remember that middle is **left biased**! So in scenarios where you want l and r to meet, make sure you do `l = m + 1` so that you're not stuck in an infinite loop.
	- Examples:
		- [[Find Peak Element]]
- If you want to return the "most up to date" value, then it'll need to be either `r` or `l`, since the loop will end before `m` is updated for the final time. Note: This is sort of an edge-case but good to know.
	- Examples:
		- [[Search in Rotated Sorted Array]]
	
