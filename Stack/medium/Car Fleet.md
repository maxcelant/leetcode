#### Approach
---
- 

#### Code
---

```python
class Solution:
	def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
		pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
		stack = []
		for pos, speed in pairs:
			# Find out how quickly a car reaches the target.
			timeToReachTarget = (target - pos) / speed
			stack.append(timeToReachTarget)
			# Did a following car reach the target first?
			# If so, we can remove it from the stack since it's 
			# Now stuck behind a slower car.
			if len(stack) >= 2 and stack[-1] <= stack[-2]:
				stack.pop()
	
		return len(stack)
```

#### Where did I go wrong?
---
- We need to sort the array by the starting position.
- We will calculate this starting from the furthest along car and moving backwards.
- We need to figure out at what **time-step** each car reaches the target.
	- We can do this doing `target - starting_position / speed`.
- If a car with an earlier starting position reaches the target at a time step _before_ a later car, then they will collide into a car fleet.
- This means that the time step of the following car needs to be _smaller_ than the leading car, because that means it reached the target _faster_.
	- Ex: Blue car reached the ending in 2.3 time steps, whereas Red car reached it in 2.5 seconds, so now Blue car is behind Red car.

![[Pasted image 20250213172320.png|]]

- We always remove the car that is "behind" the leading car in the fleet.
- We use the stack to always compare the time steps with leading car.