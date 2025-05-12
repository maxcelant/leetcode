#### Intuition
- If you need to keep track of the start of list, use a `dummy` node.




#### Reversing a Linked List using Recursion
###### Code
```python title="Reversing a linked list (recursive)"
def reverse_list(head: ListNode):
    if not head or not head.next:
        return head
    
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

###### Insight
- `new_head` will always point to the last node.
- With each step, we make the current node's `next` node point to itself.
- Since we are popping off the stack, we don't lose access to the previous nodes.

###### Example
![[Pasted image 20250310165855.png|Reversing a Linked List]]

#### Cycle Detection
###### Code
```python
def has_cycle(head):
    slow = fast = head
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    start = head
    while True:
        start = start.next
        slow = slow.next
        if start == slow:
            break

    return slow.val

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l3 # Cycle here!!

print(has_cycle(l1))
```

###### Insight
- If the `fast` and `slow` pointers eventually intersect on the same node, then we have a cycle.
- To find which node it is that caused the intersection, we can start one node at the beginning of the list and the other where the intersection is found. These two will intersect on the cycling node.

###### Example

