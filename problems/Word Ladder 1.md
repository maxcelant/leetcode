---
tags:
  - bfs
  - hard
pattern:
---
#### Video Breakdown


#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Use an adjacency list where we blank out one letter at a time from each word so that we group them by what they have in common
- Use a level order BFS strategy.

#### Code
---

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                adj[f'{w[:i]}*{w[i+1:]}'].append(w)

        q = collections.deque([beginWord])
        visited = set()
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                if word in visited:
                    continue
                visited.add(word)
                for i in range(len(word)):
                    for neigh in adj[f'{word[:i]}*{word[i+1:]}']:
                        if neigh in visited:
                            continue
                        q.append(neigh)
            res += 1
        return 0
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- Make sure you get that adjacency list correct.
- We need to go a level at a time and keep track of that as `res`.
- We need to loop through all the character groups of a word
	- Example: `cat -> *at, c*t, ca*`

#### Takeaways
---
**Where did I go wrong?**
- I thought i could use `len(visited)` as the answer but it's actually the levels in the traversal instead.
**Lessons Learned?**