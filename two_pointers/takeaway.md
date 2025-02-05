### Key Takeaways

- Remember the the left pointer should "catch up" to the right one in most cases. So do `l = r`.
- Use a `for r in range(len(nums))` for the right pointer since the right pointer is usually just on track while the left one drags.
- Figure out if you want to start your left and right pointers from the same side or start one on each side! That will be dictated most likely by whether the list is sorted or not.
