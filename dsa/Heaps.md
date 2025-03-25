#### Fundamentals
- 
#### Two Heap Median
- You can use two heaps to keep track of the median of a list.
- One contains the greater top half elements and the other the lower half elements.
- The lower half will always have `k + 1` elements whereas  upper will have`k` elements.
- **Lift and Shift Maneuver** 
	- In order to stay properly sorted and balanced, we usually add the newest element to the `lower` heap first, and pop the top element from the `lower` and add it to the `upper`.
	- Once we do this and there is an in-balance in which the `lower` is less than the `upper`, then we move the top element from the `upper` to the `lower`.
		- Remember the rule above.

![[Pasted image 20250325164334.png|Lift and Shift ]]