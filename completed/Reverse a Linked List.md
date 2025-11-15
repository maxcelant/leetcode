---
tags:
  - linked-list
  - easy
  - nvidia
pattern: use temp node for next, swap until you reach end of list
last_attempt: 2025-11-15
rate:
  - ★★★★★
---
#### Variants


#### Problem


#### Notes


#### Code
**Time Complexity**:
**Space Complexity**: 

```go
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode = nil
    cur := head
    for cur != nil {
        nxt := cur.Next
        cur.Next = prev
        prev = cur
        cur = nxt
    }
    return prev
}
```
