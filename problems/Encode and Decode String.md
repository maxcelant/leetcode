---
tags:
  - arrays
  - strings
pattern:
link:
rating:
last_attempt:
---
#### Problem
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement `encode` and `decode`

**Example 1:**

```java
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
```

**Example 2:**

```java
Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
```

#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Each word in the array becomes '{LENGTH}#{WORD}'

#### Code
---

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return re

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Just draw it out. Using two pointers this isn't super difficult, if you are off by one, just debug until you have it correct.

#### Lessons Learned
---
- 

#### Video Breakdown
---