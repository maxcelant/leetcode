---
tags:
  - arrays
  - medium
rating: 1000
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

```go
func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)
	for _, s := range strs {
		ss := strings.Split(s, "")
		slices.Sort(ss)
		sw := strings.Join(ss, "")
		gr, ok := groups[sw]
		if !ok {
			gr = make([]string, 0)
		}
		gr = append(gr, s)
		groups[sw] = gr
	}

	res := make([][]string, 0)
	for _, v := range groups {
		res = append(res, v)
	}
	return res
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