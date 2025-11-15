---
tags:
  - linked-list
  - medium
  - meta
  - nvidia
last_attempt: 2025-11-15
rate:
  - ★★★★★
link: https://leetcode.com/problems/add-two-numbers/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
---
#### Variants
- [[Add Strings]]

#### Problem
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

#### Notes


#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = (v1+v2+carry) % 10
            carry = (v1+v2+carry) // 10
            cur.next = ListNode(val=val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            cur.next = ListNode(val=carry)

        return dummy.next
```

```go
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{Val:-1}
    cur := dummy
    carry := 0
    for l1 != nil || l2 != nil {
        val := 0
        if l1 != nil {
            val += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            val += l2.Val
            l2 = l2.Next
        }
        cur.Next = &ListNode{Val: (val + carry) % 10}
        cur = cur.Next
        carry = (val + carry) / 10
    }

    if carry != 0 {
        cur.Next = &ListNode{Val:carry}
    }

    return dummy.Next
}
```