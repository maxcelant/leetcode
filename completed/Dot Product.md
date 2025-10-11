---
tags:
  - meta
  - medium
  - two-pointers
link: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
rating: 4
last_attempt: 2025-10-10
---
#### Problem
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

>Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

#### Notes
---
Create a list of non-zero pairs (index, value). Iterate through both lists and multiply if BOTH of the indexes match, otherwise move the list that is behind.

#### Code
---

```python
class Pair:
    def __init__(self, i, n):
        self.index = i
        self.val = n

class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append(Pair(i, n))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, other: 'SparseVector') -> int:
        res = 0
        p = q = 0
        while p < len(self.pairs) and q < len(other.pairs):
            if self.pairs[p].index == other.pairs[q].index:
                res += self.pairs[p].val * other.pairs[q].val
                p, q = p + 1, q + 1
            elif self.pairs[p].index > other.pairs[q].index:
                q += 1
            else:
                p += 1
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
		
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```
