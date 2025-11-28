---
tags:
  - linked-list
  - easy
  - nvidia
link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-more-than-six-months
last_attempt: 2025-11-25
rate:
  - ★★★★★
---
#### Variants
- [[Lowest Common Ancestor of a Binary Tree III]]

#### Problem
Given the heads of two singly linked-lists `headA` and `headB`, return _the node at which the two lists intersect_. If the two linked lists have no intersection at all, return `null`.

For example, the following two linked lists begin to intersect at node `c1`:

![](https://assets.leetcode.com/uploads/2021/03/05/160_statement.png)

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

**Note** that the linked lists must **retain their original structure** after the function returns.

#### Notes
The idea is the same as the LCA problem, but for linked lists.

#### Code
Time Complexity**: O(N)
**Space Complexity**: O(1)
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def distance(head: ListNode):
            dist = 0
            while head:
                head = head.next
                dist += 1
            return dist
        
        distA, distB = distance(headA), distance(headB)
        if distA > distB:
            headA, headB = headB, headA
        
        diff = abs(distA - distB)
        while headB and diff != 0:
            headB = headB.next
            diff -= 1
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA if headA == headB else None
```

**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        cur = headA
        while cur:
            seen.add(cur)
            cur = cur.next
        cur = headB
        while cur and cur not in seen:
            cur = cur.next
        return cur if cur in seen else None
```

