---
tags:
  - graphs
  - dfs
  - medium
---
#### Intuition
---
_"How could I make the insight that leads to discovering the solution?"_
- Realize that this is a directed dependency graph problem.
- We need to build the dependency adjacency list so that we can traverse down from one course to the children that we need to take before it.

#### Code
---

```python

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereqs = collections.defaultdict(list)
		# Create adjacency list of [key: course]: [value: listof prereqs]
        for (course, prereq) in prerequisites:
            prereqs[course].append(prereq)

        path, visited = set(), set()
        def dfs(course) -> bool:
            if course in path:
                return True
            if course in visited:
                return False
            
            path.add(course)

            for c in prereqs[course]:
                if dfs(c):
                    return True
            
            path.remove(course)
            visited.add(course)
            res.append(course)
            return False

        for course in range(numCourses):
            if dfs(course):
                return []
        return res
```

#### Insight  
---
_"What are the important aspects of the solution?"_
- We build an adjacency list of `{ course: [ ...prereqs ]}` so that we find what every node depends on.
- ★ We add to `visited` set _after_ looping since we are doing a post-order traversal!
- We then travel backwards until we get to the node that has no dependencies, that will be the first one added to the result, hence why we are doing a post-order traversal here.
- We use `for course in range(numCourses)` because we need to check all the courses, not matter what.

```litegal
![[Pasted image 20250410150132.png]]
![[Pasted image 20250410150144.png]]
![[Pasted image 20250410150201.png]]
![[Pasted image 20250410150208.png]]
![[Pasted image 20250410150212.png]]
![[Pasted image 20250410150222.png]]
![[Pasted image 20250410150229.png]]
![[Pasted image 20250410150241.png]]
![[Pasted image 20250410150247.png]]
![[Pasted image 20250410150254.png]]
![[Pasted image 20250410150300.png]]
```

#### Takeaways
---
**Where did I go wrong?**
- I wasn't adding to the result in a post-order fashion.
**Lessons Learned?**
- In dependency graph situations, the leaf nodes of our DFS will be the nodes that don't depend on anything else!