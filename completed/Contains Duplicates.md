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
class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
      return len(nums) != len(set(nums))
```

```go
func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)
	for _, n := range nums {
		if _, ok := seen[n]; ok {
			return true
		}
		seen[n] = true
	}
	return false
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

#### Insight
---
