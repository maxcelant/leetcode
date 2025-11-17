---
tags:
  - dfs
  - graphs
  - medium
  - meta
rate:
  - ★★★★★
last_attempt: 2025-11-16
---
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = { i: [] for i in range(numCourses) }
        for prq, crs in prerequisites:
            adj_list[crs].append(prq)
        visited = set()

        def traverse(crs, stack) -> bool:
            visited.add(crs)
            for prq in adj_list[crs]:
                if prq in stack:
                    return False
                if prq not in visited:
                    stack.append(prq)
                    if not traverse(prq, stack):
                        return False
                    stack.pop()
            return True
        
        for crs in range(numCourses):
            if not traverse(crs, stack=[crs]):
                return False
        
        return len(visited) == numCourses
```