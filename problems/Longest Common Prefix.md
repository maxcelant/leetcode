---
tags:
  - strings
  - easy
pattern: Use first string as prefix, keep shrinking it until string is empty or we match the prefix
link: https://leetcode.com/problems/longest-common-prefix
rating: 4
last_attempt: 2025-09-01
---
#### Problem


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- 

#### Code
---

```go
import "strings"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 1 {
		return strs[0]
	}

	prefix := strs[0]
	for _, s := range strs {
		for len(prefix) > 0 && !strings.HasPrefix(s, prefix) {
			prefix = prefix[:len(prefix)-1]
		}
		if prefix == "" {
			break
		}
	}
	return prefix
}
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- 

#### Lessons Learned
---
- 

#### Video Breakdown
---