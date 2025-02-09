### Key Takeaways

- Remember the the left pointer should "catch up" to the right one in most cases. So do `l = r`.
- Use a `for r in range(len(nums))` for the right pointer since the right pointer is usually just on track while the left one drags.
- Figure out if you want to start your left and right pointers from the same side or start one on each side! That will be dictated most likely by whether the list is sorted or not.
- Be weary of stupid mistakes! Like getting the index instead of the element at the index position
- If you want to skip duplicates in a list, simple loop until `n-1 != n`. This fixes some edge-cases where you don't want duplicates.
