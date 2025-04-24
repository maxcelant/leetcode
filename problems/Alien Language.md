---
tags:
  - graphs
  - dfs
pattern: Build adjacency list by find the first differing letter in adjacent words, traverse with dfs and post-order.
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- We need to find the order of the letters of this language
- Traverse the strings and find which letters come before others.
- Use DFS and post order

#### Code
---

```python
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = collections.defaultdict(list)
		# We need traverse all characters, regardless of whether they 
		# have neighbors or not
        all_chars = set(c for w in words for c in w)

		# Create the adjacency list
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]

            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ''
            # Go through the letters of both words
            for j in range(min_len):
				# The first one they don't have in common will be
				# become a connection. c1 -> c2
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        path = {}
        res = []
        # Use dfs with post order traversal so that we ensure 
        # we see the order from the bottom up.
        def dfs(c):
	        # If we have seen this character,
	        # this checks whether or not we have seen it in the path so far.
            if c in path:
                return path[c]
            
            path[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            path[c] = False
            res.append(c)
        
        for c in all_chars:
            if dfs(c):
                return ""

		# We reverse it at the end to get the correct
		# beginning to end order
        return ''.join(res[::-1])
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- The creation of the adjacency list is the most important aspect here.
- Basically traversing the from `i...len(smaller)` makes sense because we don't want to have a out of bounds error.
- Post order is necessary so that we get it from the end all the way to the beginning since it ensures that all prerequisites are processed first.
	- If A depends on B, then it will be `B` then `A` in post order.

#### Takeaways
---
**Lessons Learned?**