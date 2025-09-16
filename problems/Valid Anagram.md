---
tags:
  - arrays
  - easy
rating: 1000
last_attempt: 2025-04-30
---

#### Intuition
---
- 

#### Code
---

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

```go
func isAnagram(s string, t string) bool {
	c1 := make(map[rune]int)
	c2 := make(map[rune]int)

	for _, c := range s {
		if _, ok := c1[c]; !ok {
			c1[c] = 1
		}
		c1[c]++

	}

	for _, c := range t {
		if _, ok := c2[c]; !ok {
			c2[c] = 1
		}
		c2[c]++
	}

	return maps.Equal(c1, c2)
}

```

#### Insight
---
- 

#### Takeaways
---
- **Where did I go wrong?**
- **Lessons Learned?**
- **Aha Moments?**

#### Insight
---
