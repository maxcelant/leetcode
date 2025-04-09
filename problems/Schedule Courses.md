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

'''

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the adjacency list [key prereq]: [courseA, courseB,...]
        prereqs = collections.defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[prereq].append(course)
        
        # Return true if we find a cycle
        def dfs(course, visited, recstack) -> bool:
            if course in recstack:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            recstack.add(course)
            
            for c in prereqs[course]:
                if dfs(c, visited, recstack):
                    return True
            # Remove from the recstack when we backtrack
            recstack.remove(course)
            return False

        visited = set()
        recstack = set()
        # DFS through all of the courses until we find one that 
        # completes the correct amount of courses required.
        for course in range(numCourses):
            if dfs(course, visited, recstack):
                return False
        
        return True


```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We need to construct the adjacency list for this traversal by finding all courses for a given requisite. 
- We use a `recstack` and visited set to find a cycle in the graph

#### Takeaways
---
**Where did I go wrong?**
- I fundamentally misunderstood the problem at first.
**Lessons Learned?**