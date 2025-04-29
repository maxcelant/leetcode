---
tags:
  - 1d-dynamic-programming
  - medium
pattern: 
link:
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- If `s[i] == s[j]` AND the substring `s[i+1:j-1]` is a palindrome, then `s[i:j]` is a palindrome as well.
- We know all substrings of length 1 are palindromes.
- We can use this to find substrings of length 3.
- Check every `i,j` pair where `j - i = 2`.
- We can then use that knowledge to find length 5, then 7, etc.
- 

#### Code
---

```python


```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Takeaways
---
**Lessons Learned?**