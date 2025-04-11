---
tags:
  - dfs
  - graphs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- This is a directed graph cycle problem.
- The `numCourses` is the courses the person has to complete from 0...N (no matter what), so the only thing that would stop them from completing it would be a cycle!

#### Code
---

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = collections.defaultdict(list)
		# Adjacency list of [key: course]: [val: listof prereqs]
        for (course, prereq) in prerequisites:
            prereqs[course].append(prereq)
        
        visited, recstack = set(), set()
        def dfs(course) -> bool:
            if course in recstack: # We found a cycle!
                return True
            if course in visited:
                return False
            
            visited.add(course)
            recstack.add(course)
            for c in prereqs[course]:
                if dfs(c):
                    return True
            recstack.remove(course)
            return False

		# Go through each course
        for course in range(numCourses):
            if dfs(course):
                return False
        return True

```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to construct the adjacency list for this traversal which maps a course with ALL of it's prerequisites. This allows us to basically "go backwards" from a course and find all that need to come before it. 
- We use a `recstack` and visited set to find a cycle in the graph.

#### Takeaways
---
**Where did I go wrong?**
- I fundamentally misunderstood the problem at first.
**Lessons Learned?**