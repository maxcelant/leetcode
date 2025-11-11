---
tags:
  - dfs
  - meta
  - medium
link: https://leetcode.com/problems/nested-list-weight-sum/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-08
rate:
  - ★★★★★
---
#### Problem


#### Notes
---
Just think about traversing a file system. If it's a folder, you recursively call it, if it's a file aka an integer, then you multiply it by it's depth and add that to the result.

#### Code
---
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.res = 0
        def traverse(ni: NestedInteger, depth: int):
            if ni.isInteger():
                self.res += ni.getInteger() * depth
                return

            for l in ni.getList():
                traverse(l, depth + 1)
        
        [ traverse(ni, 1) for ni in nestedList ]
        return self.res

```

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def traverse(nestedlist, depth) -> int:
            res = 0
            for ele in nestedlist:
                if ele.isInteger():
                    res += ele.getInteger() * depth
                else:
                    res += traverse(ele.getList(), depth + 1)
            return res
        return traverse(nestedList, 1)
```

#### Follow Up: *"Create the interface"*

```python
class NestedInteger:
	def __init__(self, value=None):
		self.value = value if value is not None else []
		self.is_integer = value.isnumeric()
	
	def isInteger(self):
		return self.is_integer
	
	def add(self, value):
		if self.is_integer:
			self.value = []
			self.is_integer = False
		self.value.append(value)
	
	def setInteger(self, value):
		self.value = value
	
	def getInteger(self) -> int:
		if not self.is_integer:
			return None
		return self.value
	
	def getList(self):
		if self.is_integer:
			return None
		return self.value
```