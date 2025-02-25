#### Monotonic Stacks
A monotonic stack maintains an increasing/decreasing order by popping elements from the stack depending on if the newest value being added would "mess up" the order. 

**Example:** Let's say we have an decreasing monotonic stack with `[12, 8, 7] (top)` and the newest element is a `9`. This would mean we would `pop` the `7` and `8`, since the newest element is _greater_ than those elements. In order to maintain this "decreasing" order, we need to get rid of those.

**Signs:** If you see "Next Greater" or "Next Smallest", then you are probably dealing with a monotonic stack.

"Next Smaller" indicates a monotonic increasing stack, and vice-versa for decreasing stack.

![[Pasted image 20250218211756.png|monotonic increasing stack example]]

##### Problems 
- [[Daily Temperatures]]
- [[Next Smaller Element]]
- [[Remove K Digits to Form Smallest Number]]

---

