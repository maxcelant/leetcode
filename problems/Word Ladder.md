---
tags:
  - bfs
  - hard
---

#### Intuition
---
- I did not attempt this problem. I jumped straight to the solution.

#### Code
---

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)

        # Create the common_words dict
        common_words = defaultdict(list)
        for w in wordList:
            for i in range(n):
                common_words[f'{w[:i]}*{w[i+1:]}'].append(w)

        # Use visited set
        visited = set()

        # Create queue
        q = deque([(beginWord, 1)]) # (word, depth)
        visited.add(beginWord)

        # Use BFS to find endWord
        while q:
            cur, depth = q.popleft()
            for i in range(n):
                intermediate = f'{cur[:i]}*{cur[i+1:]}'
                for neighbor in common_words[intermediate]:
                    if neighbor == endWord:
                        return depth + 1
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        q.append((neighbor, depth + 1))

        return 0
```

#### Analysis
---
- "Find shortest path" was a good indicator that BFS was the answer here.
- Creating that `all_combo_dict` is super interesting, it allows you to find "alike words". 
- Building the graph is the creative / difficult part. You had to determine _how_ the nodes should be related.

#### Takeaways
---
- **Where did I go wrong?**
	- I need to mark neighbors as visited right before I add them to the queue, not right when I pop them from the queue.
	- This ensures that each node is only added to the queue once. 
	- Doing it the other way means that I could have it in the queue multiple times since it'll only be marked visited when it's popped!
- **Lessons Learned?** 
	- I can solve this using BFS with the intermediate nodes being neighboring words.
- **Aha Moments?**