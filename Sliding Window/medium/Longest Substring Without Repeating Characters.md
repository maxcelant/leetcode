
```python
'''
- Use sliding window, add characters to a set
- Check if the character on the right you are adding is already in the set,
- if it is, then we remove from the left until its not in the set.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set() 
        l, r = 0, 0
        count = 0
        while r <= len(s) - 1:
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
            count = max(count, len(window))
        return count
```



