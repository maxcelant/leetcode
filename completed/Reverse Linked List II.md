---
tags:
  - medium
  - linked-list
  - nvidia
link: https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-11-23
rate:
  - ★★★
---
#### Variants

#### Problem

#### Notes

There are lots of edge cases to think about in this problem.

1. Traverse the linked list using `prev` and `cur` as normal until we reach the `left` barrier.
2. Set the `con` at the `prev` position and `tail` at the `cur` position.
3. Reverse until we reach _after_ the `right`-th node.
4. Update the pointers so that `con.next = prev` and `tail.next = cur`.
![[Pasted image 20251123233109.png]]

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur = None, head
        i = 1
        # Move forward two pointers until we reach left barrier
        while i < left:
            prev = cur
            cur = cur.next
            i += 1

		# Keep track of pointers to make connections later to update the
		# orientation of the list
        newHead, tail = prev, cur
        while i <= right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1
        # If left = 0, then prev and thus newHead will be None
        # So this is handling that edge case.
        if newHead:
            newHead.next = prev
        else:
            head = prev
        tail.next = cur
        return head
```
