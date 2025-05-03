---
tags:
  - arrays
  - medium
rating: 5
last_attempt: 2025-04-30
---

#### Intuition
---
- 

#### Code
---

```python
from collections import defaultdict

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
      sortedStr = "".join(sorted(s))
      groups[sortedStr].append(s)
    return [ g for g in groups.values() ]
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