#### Arrays
- You can sort the letters of a string by doing `sorted(string)`. Which means you can use this as a key in a dictionary.
- By default, `heapq` is a min-heap, which means the 0th index is always the smallest number.
- You can make a `heapq` node a tuple, it will always use the first value in the tuple to determine its position in the heap.
- When it comes to prefix-suffix arrays, just remember, the result for each element is everything before (or after) _excluding_ itself.
- Biggest advice for prefix-suffix arrays is take it a step at a time and whiteboard it.
#### Two Pointers
- Remember the the left pointer should "catch up" to the right one in most cases. So do `l = r`.
- Use a `for r in range(len(nums))` for the right pointer since the right pointer is usually just on track while the left one drags.
- Figure out if you want to start your left and right pointers from the same side or start one on each side! That will be dictated most likely by whether the list is sorted or not.
- Be weary of stupid mistakes! Like getting the index instead of the element at the index position
- If you want to skip duplicates in a list, simple loop until `n-1 != n`. This fixes some edge-cases where you don't want duplicates.

#### Sliding Window
- Because of the nature of sliding window problems. You usually only need to have a left pointer, the right can made in the loop.

```python

l = 0
for r in range(len(foo)):
    ...

```

- The window doesn't always need to necessarily be a data structure, sometimes a counter will do!
- The most important thing is answering _"what causes the window to shrink?"_.

#### Stack
- Monotonic stacks maintain a certain order and will "pop" elements in order to maintain that order by comparing with the current value. If you see "Next Greater" or "Next Smallest", then you are probably dealing with a monotonic stack.
	- "Next Smaller" indicates a monotonic increasing stack, and vice-versa for decreasing stack.
	- Example: Let's say we have an decreasing monotonic stack with `[12, 8, 7] (top)` and the newest element is a `9`. This would mean we would `pop` the `7` and `8`, since the newest element is _greater_ than those elements. In order to maintain this "decreasing" order, we need to get rid of those.

![[Pasted image 20250218211756.png|monotonic increasing stack example]]

##### Problems 
- [[Daily Temperatures]]
- [[Next Smaller Element]]
- [[Remove K Digits to Form Smallest Number]]

---

#### Binary Search
- Use `l + ((r - l) // 2)` to find the middle index.
- Put the `target` on the left-hand side of the comparison to help orient it in your brain.

